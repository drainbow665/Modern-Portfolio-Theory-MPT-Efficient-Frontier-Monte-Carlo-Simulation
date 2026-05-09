# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ==============================
# 2. DEFINE ASSETS
# ==============================
tickers = ['SPY','QQQ','VTI','GLD','AGG']

# ==============================
# 3. DEFINE TIME (LAST 5 YEARS)
# ==============================
end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

# ==============================
# 4. DOWNLOAD DATA
# ==============================
data = yf.download(tickers, start=start_date, end=end_date)['Close']
data = data.dropna()

# ==============================
# 5. CALCULATE RETURNS
# ==============================
returns = data.pct_change().dropna()

mean_returns = returns.mean()
cov_matrix = returns.cov()

# ==============================
# 6. MONTE CARLO SIMULATION
# ==============================
num_portfolios = 50000
results = np.zeros((3, num_portfolios))
weights_record = []

risk_free_rate = 0.03

for i in range(num_portfolios):

    weights = np.random.random(len(tickers))
    weights /= np.sum(weights)
    weights_record.append(weights)

    portfolio_return = np.dot(weights, mean_returns) * 252
    portfolio_volatility = np.sqrt(
        np.dot(weights.T, np.dot(cov_matrix, weights))
    ) * np.sqrt(252)

    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

    results[0,i] = portfolio_return
    results[1,i] = portfolio_volatility
    results[2,i] = sharpe_ratio

# ==============================
# 7. CREATE DATAFRAME
# ==============================
results_df = pd.DataFrame(results.T, columns=['Return','Volatility','Sharpe'])

# ==============================
# 8. FIND BEST PORTFOLIOS
# ==============================
max_sharpe_idx = results_df['Sharpe'].idxmax()
min_vol_idx = results_df['Volatility'].idxmin()

best_weights = pd.Series(weights_record[max_sharpe_idx], index=tickers)

print("\n🔥 OPTIMAL PORTFOLIO (MAX SHARPE):\n")
print(best_weights.sort_values(ascending=False))

# ==============================
# 9. EFFICIENT FRONTIER
# ==============================
sorted_df = results_df.sort_values('Volatility')
efficient_frontier = sorted_df['Return'].cummax()

# ==============================
# 10. PLOT GRAPH
# ==============================
plt.figure(figsize=(10,6))

plt.scatter(results_df['Volatility'], results_df['Return'],
            c=results_df['Sharpe'], cmap='viridis', s=5)

plt.plot(sorted_df['Volatility'], efficient_frontier,
         color='orange', linewidth=3, label='Efficient Frontier')

plt.scatter(results_df.loc[max_sharpe_idx,'Volatility'],
            results_df.loc[max_sharpe_idx,'Return'],
            color='red', s=200, label='Max Sharpe')

plt.scatter(results_df.loc[min_vol_idx,'Volatility'],
            results_df.loc[min_vol_idx,'Return'],
            color='green', s=200, label='Min Risk')

plt.xlabel("Risk (Volatility)")
plt.ylabel("Return")
plt.title("Efficient Frontier (SPY, QQQ, VTI, GLD, AGG)")
plt.legend()
plt.grid()

plt.show()
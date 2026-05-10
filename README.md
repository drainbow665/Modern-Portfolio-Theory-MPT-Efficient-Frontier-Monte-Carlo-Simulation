# Portfolio Optimization via Monte Carlo Simulation

## Problem Statement
The objective of this project is to determine the optimal allocation of assets that maximizes return while minimizing risk. Investors often face difficulty in selecting the best combination of assets, and this project solves that problem using data-driven techniques.

---

## Dataset Description
The dataset consists of 5 years of historical price data for the following assets:
- SPY (S&P 500 ETF)
- QQQ (NASDAQ ETF)
- VTI (Total Market ETF)
- GLD (Gold ETF)
- AGG (Bond ETF)

Data is collected using the yfinance library.

---

## Methodology
This project is based on Modern Portfolio Theory.

Steps:
1. Calculate daily returns from price data
2. Compute mean returns and covariance matrix
3. Annualize returns and volatility
4. Generate 10,000 random portfolios using Monte Carlo simulation
5. Calculate return, risk, and Sharpe ratio for each portfolio
6. Identify:
   - Maximum Sharpe Ratio Portfolio
   - Minimum Volatility Portfolio
   - Equal Weight Portfolio
7. Construct the Efficient Frontier

---

## Code Implementation
The project is implemented in Python using the following libraries:
- NumPy
- Pandas
- Matplotlib
- Seaborn
- yfinance

The code performs:
- Data collection
- Statistical calculations
- Simulation of portfolios
- Visualization of results

---

## Results and Insights
The project provides the following insights:

- The Maximum Sharpe Portfolio gives the best risk-adjusted return
- The Minimum Volatility Portfolio minimizes risk
- Diversification reduces overall portfolio risk
- The Efficient Frontier shows the optimal risk-return trade-off

Visualizations include:
- Efficient Frontier
- Portfolio Allocations
- Correlation Matrix
- Return Distribution
- Sharpe Ratio Distribution
- Risk vs Return Graph

---

## Conclusion
This project demonstrates how investors can use quantitative methods to make better investment decisions by optimizing their portfolios.

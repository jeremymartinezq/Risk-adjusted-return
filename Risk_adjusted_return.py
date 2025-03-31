def sharpe_ratio(returns, risk_free_rate, std_dev):
    excess_return = returns - risk_free_rate
    return excess_return / std_dev


def treynor_ratio(returns, risk_free_rate, beta):
    excess_return = returns - risk_free_rate
    return excess_return / beta


# Example inputs
returns = 0.17  # Annual return
risk_free_rate = 0.03  # Risk-free rate
std_dev = 0.2  # Standard deviation of returns
beta = 1.2  # Beta of the investment

sr = sharpe_ratio(returns, risk_free_rate, std_dev)
tr = treynor_ratio(returns, risk_free_rate, beta)
print(f"Sharpe Ratio: {sr:.2f}")
print(f"Treynor Ratio: {tr:.2f}")



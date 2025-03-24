# Import the necessary libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

nvda = yf.Ticker("NVDA")

expiration_dates = nvda.options
closest_expiration = expiration_dates[0]
option_chain = nvda.option_chain(closest_expiration)

calls = option_chain.calls
puts = option_chain.puts
current_price = nvda.info['regularMarketPrice']
print(f"\nCurrent NVDA price: ${current_price:.2f}")

calls['moneyness'] = calls['strike'] / current_price
puts['moneyness'] = puts['strike'] / current_price

plt.figure(figsize=(12, 6))
plt.scatter(calls['moneyness'], calls['impliedVolatility'] * 100, label='calls', color="green")
plt.scatter(puts['moneyness'], puts['impliedVolatility'] * 100, label='puts', color="red")


plt.title(f'NVDA volatility smile ({closest_expiration})')
plt.xlabel('moneyness')
plt.ylabel('IV')
plt.axvline(x=1.0, color='r', linestyle='--', label='At-the-money')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
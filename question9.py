import math
import numpy

stock_price = 20
expected_return = .12
volatility = .25
days_in_year = 365

daily_volatility = volatility / math.sqrt(days_in_year)
#print(f"Daily volatility: {daily_volatility}")

daily_std = stock_price * daily_volatility
print(f"Daily stddev of price: {daily_std}")

daily_expected_return = expected_return / days_in_year
#print(f"Daily expected return: {daily_expected_return}")

price_tmrw = stock_price * (1 + daily_expected_return) 
#print(f"Price tmrw: {price_tmrw}")

z_score_for_975_percentile = 1.96
price_tmrw_975_percentile = (z_score_for_975_percentile * daily_std)+price_tmrw
print(f"Price tmrw 97.5 percentile: {price_tmrw_975_percentile}")

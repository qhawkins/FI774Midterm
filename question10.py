import math 

price_of_call = 6
stock_price = 51
rfr = .06
ttm = 1
put_price = 2.09

discount_factor = math.exp(-rfr * ttm)
#print(f"discount factor: {discount_factor}")

strike_price = (put_price + stock_price - price_of_call) / discount_factor
print(f"strike price: {round(strike_price)}")


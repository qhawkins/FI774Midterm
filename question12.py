import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def calculate_put_greeks(S, K, r, T, sigma):
    #d1 and d2 from black scholes
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    #delta from rate of change of price
    delta = -norm.cdf(-d1)
    
    #gamma from rate of change of delta
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    
    #theta from rate of change of time
    theta = -(S * sigma * norm.pdf(d1)) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2)
    theta = theta / 365  # Convert to per day
    
    return delta, gamma, theta

prices = np.arange(20, 200, 20)

deltas = []
gammas = []
thetas = []

for price in prices:
    delta, gamma, theta = calculate_put_greeks(price, 100, 0.05, 1, 0.25)
    deltas.append(delta)
    gammas.append(gamma)
    thetas.append(theta)

fig, ax = plt.subplots(3, 1)
ax[0].plot(prices, deltas, label='Delta', color='red')
ax[1].plot(prices, gammas, label='Gamma', color='green')
ax[2].plot(prices, thetas, label='Theta', color='blue')
fig.legend()
plt.show()
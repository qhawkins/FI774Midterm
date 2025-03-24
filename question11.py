import numpy as np
import math

#option c
c_delta = .6
c_gamma = 0.05
c_vega = 20

#option a
a_delta = 0.4
a_gamma = 0.03
a_vega = 15

#option b
b_delta = -0.5
b_gamma = 0.04
b_vega = 18

#underlying
u_delta = 1
u_gamma = 0
u_vega = 0


def calculate_neutral_portfolio():
    # scaling for contracts
    current_delta = 100 * c_delta
    current_gamma = 100 * c_gamma
    current_vega = 100 * c_vega

    #creating matries to solve system of equations
    a_sub = np.array([
        [a_gamma, b_gamma],
        [a_vega, b_vega]
    ])

    b_sub = np.array([-current_gamma, -current_vega])

    # solve for allocations
    option_ab_solution = np.linalg.solve(a_sub, b_sub)
    
    option_a_allocation = option_ab_solution[0]
    option_b_allocation = option_ab_solution[1]

    #solving for delta
    stock_allocation = -(current_delta + 
                                option_a_allocation * a_delta + 
                                option_b_allocation * b_delta)

    #calculating exposures.
    resulting_delta = current_delta + stock_allocation * u_delta + \
                      option_a_allocation * a_delta + \
                      option_b_allocation * b_delta
                     
    resulting_gamma = current_gamma + stock_allocation * u_gamma + \
                      option_a_allocation * a_gamma + \
                      option_b_allocation * b_gamma
                     
    resulting_vega = current_vega + stock_allocation * u_vega + \
                     option_a_allocation * a_vega + \
                     option_b_allocation * b_vega
    
    return (stock_allocation, option_a_allocation, option_b_allocation, 
            resulting_delta, resulting_gamma, resulting_vega)

def main():
    stock, option_a, option_b, delta, gamma, vega = calculate_neutral_portfolio()
    print(f"stock allocation: {stock*100}")
    print(f"option a allocation: {option_a*100}")
    print(f"option b allocation: {option_b*100}")
    print(f"resulting delta: {delta*100}")
    print(f"resulting gamma: {gamma*100}")
    print(f"resulting vega: {vega*100}")

if __name__ == "__main__":
    main()
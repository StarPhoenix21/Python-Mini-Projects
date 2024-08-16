import numpy as np
from scipy.optimize import minimize

def calculate_portfolio_performance(weights, returns, cov_matrix):
    """Calculate the expected return and risk (standard deviation) of the portfolio."""
    portfolio_return = np.dot(weights, returns)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return portfolio_return, portfolio_risk

def optimizePortfolio(returns, cov_matrix):
    """Optimize the portfolio based on risk and return using Mean-Variance Optimization."""
    
    num_assets = len(returns)
    
    # Initial guess for weights
    initial_weights = np.ones(num_assets) / num_assets
    
    # Constraints
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # weights sum to 1 (full investment)
    bounds = [(0, 1) for _ in range(num_assets)]
    
    # Objective function (minimize risk)
    def objective(weights):
        _, risk = calculate_portfolio_performance(weights, returns, cov_matrix)
        return risk
    
    # Optimization
    result = minimize(objective, initial_weights, bounds=bounds, constraints=constraints)
    
    if result.success:
        optimized_weights = result.x
        portfolio_return, portfolio_risk = calculate_portfolio_performance(optimized_weights, returns, cov_matrix)
        return (f"Optimized portfolio weights: \n\t{optimized_weights}\n"
                f"Expected Return: {portfolio_return:.2f}\n"
                f"Portfolio Risk (Standard Deviation): {portfolio_risk:.2f}")
    else:
        return "Optimization failed."

def get_input(prompt):
    """Helper function to get and validate user input."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """Run the portfolio optimization application."""
    num_assets = int(get_input("Enter the number of assets(eg: 1, 2, 3): "))
    
    print("\nEnter the expected returns for each asset (in '%'):")
    returns = np.array([get_input(f"\tReturn for asset {i + 1}: ") for i in range(num_assets)])
    
    print("\nEnter the risks for each asset (in '%'):")
    risks = np.array([get_input(f"\tRisk for asset {i + 1}: ") for i in range(num_assets)])
    
    # Creating a dummy covariance matrix based on risks
    # Assuming assets are uncorrelated for simplicity
    cov_matrix = np.diag(risks ** 2)
    
    result = optimizePortfolio(returns, cov_matrix)
    print("\nOptimization Result:")
    print(result)

if __name__ == "__main__":
    main()

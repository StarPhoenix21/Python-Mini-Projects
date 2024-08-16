![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)

![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Advance Stock Portfolio Optimizer

## 🛠️ Description

The Stock Portfolio Optimizer helps you optimize a stock portfolio based on risk and return using Mean-Variance Optimization. It calculates the optimal asset weights to minimize risk while targeting the desired returns.

## ⚙️ Languages or Frameworks Used
- Python
- `numpy`
- `scipy`

## 🌟 How to Run

1. Clone or download the repository.
2. Install the required libraries if you haven't already:
   ```bash
   pip install numpy scipy
   ```
3. Open the file `StockPortfolioOptimizer.py` in your Python IDE or text editor.
4. Run the script:
   ```bash
   python StockPortfolioOptimizer.py
   ```
5. Follow the prompts to input the number of assets, their expected returns, and their risks.

### Example Usage:

```bash
python StockPortfolioOptimizer.py
Enter the number of assets(eg: 1, 2, 3): 3

Enter the expected returns for each asset (in '%'):
    Return for asset 1: 23
    Return for asset 2: 45
    Return for asset 3: 12

Enter the risks for each asset (in '%'):
    Risk for asset 1: 2
    Risk for asset 2: 3
    Risk for asset 3: 8

Optimization Result:
Optimized portfolio weights: 
    [0.6637926  0.29474204 0.04146536]
Expected Return: 29.03
Portfolio Risk (Standard Deviation): 1.63
```

## 🤖 Author
[AtharvaPawar456](https://github.com/AtharvaPawar456)
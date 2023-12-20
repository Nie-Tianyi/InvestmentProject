def split_stock_data(path):
    pass

def generate_lean_stock_code(path):
    list = []
    with open(path,"r") as f:
        for line in f:
            print(line)
            if len(line) == 1:
                continue
            list.append(line.split("(")[1].split(")")[0])
    list.sort()
    with open("lean_stock_codes.txt", "w") as f:
        for item in list:
            f.write(item+"\n")




if __name__ == '__main__':
    generate_lean_stock_code("stock_codes.txt")


import pandas as pd
from scipy import stats

# Load the provided file
file_path = './stock/PERMNO_10104.csv'
data = pd.read_csv(file_path)

# Assuming a risk-free rate for the calculations (can be adjusted as per actual data)
risk_free_rate = 0.02  # Example: 2% annual risk-free rate

# Converting date to datetime format
data['date'] = pd.to_datetime(data['date'])

# Calculate monthly risk-free rate (assuming the provided risk-free rate is annual)
monthly_risk_free_rate = (1 + risk_free_rate)**(1/12) - 1

# Calculating beta using linear regression (stock returns vs market returns)
slope, intercept, r_value, p_value, std_err = stats.linregress(data['sprtrn'], data['RET'])
beta = slope

# Total risk (standard deviation of the stock's returns)
total_risk = data['RET'].std()

# Calculating Ex Post Jensen's Alpha
# CAPM expected return = risk_free_rate + beta * (market return - risk_free_rate)
expected_return = monthly_risk_free_rate + beta * (data['sprtrn'] - monthly_risk_free_rate)
jensens_alpha = (data['RET'] - expected_return).mean()

# Calculating Sharpe Ratio
excess_return = data['RET'] - monthly_risk_free_rate
sharpe_ratio = excess_return.mean() / excess_return.std()

beta, total_risk, jensens_alpha, sharpe_ratio

def analyze_stock(file_path, risk_free_rate=0.02):
    data = pd.read_csv(file_path)
    data['date'] = pd.to_datetime(data['date'])
    monthly_risk_free_rate = (1 + risk_free_rate) ** (1 / 12) - 1
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['sprtrn'], data['RET'])
    beta = slope
    total_risk = data['RET'].std()
    expected_return = monthly_risk_free_rate + beta * (data['sprtrn'] - monthly_risk_free_rate)
    jensens_alpha = (data['RET'] - expected_return).mean()
    excess_return = data['RET'] - monthly_risk_free_rate
    sharpe_ratio = excess_return.mean() / excess_return.std()
    return beta, total_risk, jensens_alpha, sharpe_ratio
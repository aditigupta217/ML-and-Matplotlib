from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

# Sample dataset
data = {
    'studyhours': [1, 2, 3, 4, 5],
    'marks': [60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

# Standard Scaler
standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df)
print("Standard Scaler Output:")
print(pd.DataFrame(standard_scaled, columns=['studyhours', 'marks']))

# Min-Max Scaler
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)
print("\nMin-Max Scaler Output:")
print(pd.DataFrame(minmax_scaled, columns=['studyhours', 'marks']))

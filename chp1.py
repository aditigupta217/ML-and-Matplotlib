import pandas as pd

data = {
    'Name' : ["aditi","nikita","sangeeta","anil"],
    'Age' : [18,None,53,62],
    'Salary': [None,90000,None,30000]
}

df = pd.DataFrame(data)
print("Orignal data")
print(df)

print(df.isnull().sum())
drop = df.dropna()
print(drop)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)
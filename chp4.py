from sklearn.linear_model import LogisticRegression
X = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1]

model = LogisticRegression()
model.fit(X,y)

hours = float(input("Enter the number of hours you study: "))
result = model.predict([[hours]])[0]

if result == 1:
    print(f"You are likely to PASS")
else:
    print(f"You are likely to FAIL")
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
y = [50,60,70,80,90]

model = LinearRegression()
model.fit(X,y)

hours = float(input("Enter the number of hours you study: "))
predicted_marks = model.predict([[hours]])[0]
print(f"Based on your hours {hours} you get {predicted_marks} marks")
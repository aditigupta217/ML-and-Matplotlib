from sklearn.tree import DecisionTreeClassifier

X = [
    [7,2],
    [8,3],
    [9,6],
    [10,7]
]
y = [0,0,1,1]
model = DecisionTreeClassifier()

model.fit(X,y)

weight = float(input("Enter the weight in cm: "))
shade = float(input("Enter the shade in cm: "))

result = model.predict([[weight,shade]])[0]

if result == 0:
    print("This is likely apple")
else:
    print("this is likely orange")
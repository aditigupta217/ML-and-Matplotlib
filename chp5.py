from sklearn.neighbors import KNeighborsClassifier

X = [
    [180,6],
    [190,6.5],
    [230,7],
    [270,7.5],
    [300,8],
    [340,8.5]
]

y = [0,0,0,1,1,1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)

weight = float(input("Enter the weight in grams: "))
size = float(input("Enter the size in cm: "))

prediction = model.predict([[weight,size]])[0]

if prediction==0:
    print("likey to be an apple")
else:
    print("likey to be a orange")
from sklearn import tree
#features = [[140, "smooth"],[130, "smooth"],[150, "bumpy"],[170, "bumpy"]]
#labels = ["apple","apple","orange","orange"]
x = [[140, 1],[130, 1],[150, 0,],[170, 0]]
y = [1,1,0,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
print(clf.predict([[150, 0]]))
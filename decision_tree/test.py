from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeClassifier

data = datasets.load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=1234
)

clf = DecisionTreeClassifier(max_depth=10,criterion="entropy",min_samples_split=2)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

def accuracy(y_test, y_pred):
  return np.sum(y_test == y_pred) / len(y_test)

# acc = accuracy(y_test, predictions)
# print(acc)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))

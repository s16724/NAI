#Autorzy : Jan Rygulski , Dominika Stryjewska
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
'''
Program ma za zadanie  klasyfikować dane za pomocą SVM  i drzew decyzyjnych. 
Baza która postanowilikśmy poddać klasyfikacji są owoce.
zbiór danych został zebrany samodzielnie.
zbiór danych zawiera:
-kolor owocu 
- masa
- wysokość 
- szerokość 
- gatunek 
'''
# definiujemy nazwy dla column
colnames = ["class", "mass", "width", "height", "color"]

#odczytujemy dane z pliku
dataset = pd.read_csv('fruit_data.txt', header=None, names=colnames)
print(dataset)
dataset = dataset.replace({"class": {"apple": 1,
                                     "mandarin": 2,
                                     "orange": 3,
                                     "green apple": 4,
                                     "lemon": 5,
                                     "tomato": 6,
                                     "banana": 7,
                                     "pearl": 8}})
dataset = dataset.replace({"color": {"red": 1,
                                     "orange": 2,
                                     "green": 3,
                                     "yellow": 4}})
print(dataset)

sns.heatmap(dataset.corr())
plt.title('Correlation')
plt.show()

X = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, 0].values
X1 = dataset.iloc[:, 1:].values

X_train, X_test, y_train, y_test = train_test_split(
    X1, y, test_size=0.30, random_state=0)

params = {'random_state': 0, 'max_depth': 4}
classifier = DecisionTreeClassifier(**params)
classifier.fit(X_train, y_train)

X_new_fruit = np.array([[116, 6.3, 7.7, 3]])
prediction = classifier.predict(X_new_fruit)

print(prediction)

print("dokładność zestawu testowego : ", classifier.score(X_test, y_test))

# SVC
svc = svm.SVC(kernel='linear', C=1, gamma=1).fit(X, y)

# create a mesh to plot in
h = 0.02  # step size in the mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('width')
plt.ylabel('height')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('SVC with Linear kernel')
plt.show()

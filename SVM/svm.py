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
baza która postanowilikśmy poddać klasyfikacji są kwiaty irysów
(http://archive.ics.uci.edu/ml/datasets/Iris), 
które dzielą się na trzy gatunki:
*SETOSA
*VIRGINICA
*VERSICOLOUR
Wykorzystany zbiór danych zawiera :
1. długość kielicha  in cm
2. szerokość kielicha in cm
3.długość płatka in cm
4.szerokość płatka 
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica
'''
# definiujemy nazwy dla column
colnames = ["sepal_l", "sepal_w", "petal_l", "petal_w", "class"]

#odczytujemy dane z pliku
dataset = pd.read_csv('iris.txt', header=None, names=colnames)

# Data
print(dataset)

# Enkodowanie poszczególnych danych
dataset = dataset.replace({"class": {"Iris-setosa": 1, "Iris-versicolor": 2, "Iris-virginica": 3}})
# Visualize the new dataset
print(dataset)

X = dataset.iloc[:, -3:-1].values
y = dataset.iloc[:, -1].values
X1 = dataset.iloc[:, :-1].values

#tworzenie heat mapy w celu określenia korelacji dla następujących kolumn
plt.figure(1)
sns.heatmap(dataset.corr())
plt.title('Correlation')
plt.show()

#podział danych na testowe i treningowe
X_train, X_test, y_train, y_test = train_test_split(
    X1, y, test_size=0.30, random_state=0)

params = {'random_state': 0, 'max_depth': 4}
classifier = DecisionTreeClassifier(**params)
classifier.fit(X_train, y_train)

#w tym miejscu wprowadzamy nowy kwiat o paramentrach
# niezwiązanychu z baza by sprawdzić czy
#program jest w stanie oszacować gatunek kwiatu
X_new_flower = np.array([[7.5, 2.5, 7.0, 0.2]])
prediction = classifier.predict(X_new_flower)
print(prediction)
print("dokładność zestawu testowego : ", classifier.score(X_test, y_test))
# SVC
svc = svm.SVC(kernel='linear', C=1, gamma=100).fit(X, y)

# tworzenie wykresu
h = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('SVC with Linear kernel')
plt.show()

#Autorzy : Dominika Stryjewska, Jan Rygulski
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

colnames = ["sepal_l", "sepal_w", "petal_l", "petal_w", "class"]

# odczytujemy dane z pliku
dataset = pd.read_csv('iris.txt', header=None, names=colnames)


# print(dataset)

X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values
# print(y)

encoder = LabelEncoder()
y1 = encoder.fit_transform(y)
# print(y1)

Y = pd.get_dummies(y1).values
#print(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

model = Sequential()
model.add(Dense(4, input_shape=(4,), activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(Adam(lr=0.04), 'categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100)
X_test2 = np.array([[5, 2.5, 3, 1], [5, 3.9, 2, 0.5], [8, 3.5, 6, 2]])  # setosa, versicolor, virginica
y_pred = model.predict(X_test2)

print(np.argmax(y_pred, axis=1))#0 = setosa 1 = versicolor 2 = virginica
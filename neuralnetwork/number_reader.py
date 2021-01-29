#Autorzy : Dominika Stryjewska, Jan Rygulski
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

data = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = data.load_data()
#  sprawdzamy z jakimi danymi mamy do czynienia
plt.figure(figsize=(5, 5))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_train[i], cmap=plt.cm.binary)
plt.show()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())  # obraz 28x28 zmienieamy na 1x784
# input layers
model.add(tf.keras.layers.Dense(128, activation='relu'))
# output layer
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

#przeprowadzamy prognoze pojedynczego obrazka
#i sprawdzamy jego zgodność wyświetlając go plotem
prediction = model.predict(x_test)
print(np.argmax(prediction[0]))

plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.show()

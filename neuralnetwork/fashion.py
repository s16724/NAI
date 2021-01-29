#Autorzy : Dominika Stryjewska, Jan Rygulski
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Imnportujemy zestaw danych Fashion MNIST
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Spodnie', 'Bluza', 'Sukienka', 'Plaszcz',
               'Sandal', 'Koszula', 'Sneaker', 'Torba', 'But do kostki']

# Skalujemy wartości pikseli do zakresu od 0 do 1
train_images = train_images / 255
test_images = test_images / 255

# Konfiguracja warstw
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# kompilacja modelu
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
# Trenowanie danych
model.fit(train_images, train_labels, epochs=10)

img = test_images[8000]
img = (np.expand_dims(img, 0))
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(img)
print(np.argmax(predictions[0]))

plt.imshow(test_images[8000], cmap=plt.cm.binary)
plt.show()

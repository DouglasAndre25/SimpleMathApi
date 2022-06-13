import sys
import tensorflow as tf

data = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = data.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.softmax))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train,y_train, epochs=3)
loss, accuracy = model.evaluate(x_test,y_test)

def calculate(img):
    numbers = model.predict(img)
    return numbers


sys.modules[__name__] = calculate
from typing import Sequence
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

inputs = keras.Input(shape=(200,1), name="digits")
x = tf.keras.layers.AveragePooling1D(pool_size=4,strides=1, padding='same')(inputs)
x = tf.keras.layers.Flatten()(x)
x = layers.Dense(3000, activation="relu", name="dense_1")(x)
x = layers.Dropout(.25)(x)
# x = layers.Dense(32, activation="relu", name="dense_2")(x)
# x = layers.Dense(1800, activation="relu", name="dense_3")(x)
x = layers.Dense(2400, activation="tanh", name="dense_2")(x)
x = layers.Dropout(.25)(x)
x = layers.Dense(2000, activation="tanh", name="dense_3")(x)
x = layers.Dropout(.25)(x)
x = layers.Dense(1600, activation="relu", name="dense_4")(x)
outputs = layers.Dense(951, activation="softmax", name="predictions")(x)


model = keras.Model(inputs=inputs, outputs=outputs)

print(model.summary())

x_train=np.load("x_train_10.npy")
x_test = np.load("x_test_10.npy")
names=open("npy_2/name.txt",'r')
y=[]
y_e=[]
p=0
for i in names.readlines():
  j=[float(p)]*100
  q=[float(p)]*20
  y+=j
  y_e+=q
  p+=1
names.close()
y_train = np.array(y).reshape((95100,1)).astype("float32")
y_test = np.array(y_e).reshape((19020,1)).astype("float32")
# x_train = x_train.astype("float32") / 4
x_train = x_train.reshape([95100,200,1])
x_test = x_test.reshape([19020,200,1])

# print(x_train.shape)
# print(y_train.shape)

# print(x_train[0])

model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.1, momentum=0.0, nesterov=False, name="SGD"),
    # loss=tf.keras.losses.MeanSquaredLogarithmicError(),
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False,name='sparse_categorical_crossentropy'),
    metrics=['accuracy'],
)

print("Fit model on training data")
history = model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=15,
    shuffle = True,
    validation_data=(x_test, y_test),
    # validation_split = 0.5
)

model.save("my_model_v2.h5")



# test = np.load('test.npy')
# test = test.reshape((1,200,1))/4
# # print(test)
# t=model.predict(test)
# # print(x_train[-1].shape)
# t1=np.argmax(t)
# names=open("npy_2/name.txt",'r')
# print(t1)
# o = names.readlines()
# print(o[t1])
# names.close()
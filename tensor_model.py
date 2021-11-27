from typing import Sequence
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

inputs = keras.Input(shape=(198,3), name="digits")
x = layers.Conv1D(filters=64, kernel_size=3, activation='relu')(inputs)
x = layers.Flatten()(x)
x = layers.Dropout(.5)(x)
x = layers.Dense(951, activation="relu", name="dense_1")(x)  # 951
x = layers.Dropout(.5)(x)
x = layers.Dense(951, activation="relu", name="dense_2")(x) # 951 v6:500
x = layers.Dropout(.5)(x)
x = layers.Dense(951, activation="relu", name="dense_3")(x) # 951 v6:500
outputs = layers.Dense(951, activation="softmax", name="predictions")(x)

model = keras.Model(inputs=inputs, outputs=outputs)

print(model.summary())

x_train=np.load("3-mer.npy")
x_test = np.load("3-mer_test.npy")
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
x_train = x_train.astype("float32")/4
x_test = x_test.astype("float32")/4

model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.05, momentum=0.1, nesterov=False, name="SGD"),
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False,name='sparse_categorical_crossentropy'),
    metrics=['accuracy'],
)


print("Fit model on training data")

history = model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=25,
    shuffle = True,
    validation_data=(x_test, y_test),
)

model.save("my_model_v7.h5")

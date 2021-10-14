import tensorflow as tf
import numpy as np
# x = tf.constant([1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12. ,13. ,14. ,15. ,16., 17., 18.])
# x = tf.reshape(x, [2, 9,1])
# max_pool_1d = tf.keras.layers.AveragePooling1D(pool_size=2,strides=1, padding='same')
# print(x)
# print(max_pool_1d(x))

x_train=np.load("x_train_10.npy")
# x = x_train[0].reshape([1,200,1])
# print(x.shape)
# max_pool_1d = tf.keras.layers.AveragePooling1D(pool_size=4,strides=1, padding='same')
# print(max_pool_1d(x))
# print(x)
print(x_train)
import tensorflow as tf
import numpy as np

a = tf.add(3, 5)
sess = tf.Session()
print(sess.run(a))
sess.close()
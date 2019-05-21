'''
Pyhton script for Tensorflow session at CSIR
Author: Vaibhav Bagga
Email: vaibagga@gmail.com
Github: vaibagga

'''

## importing dependency
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


## creating constant tensor

## 0 dimesional constant or scalar constant
a = tf.constant(2.0)
print(a)


## creating 1 dimensional tensor
b = tf.constant([1,2,3,4])
print(b)

## creating session object
sess = tf.Session()
print(sess.run([a, b]))
sess.close()

## vector constant or scalar
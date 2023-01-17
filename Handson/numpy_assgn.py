# #Numpy - np.random.choice
#
# import pandas as pd
# import numpy as np
#
# #Uniform random sample from numpy.arange(5) of size = 3
#
# a = np.random.choice(5, 3)
# print(a)
#
# #Non-Uniform random sample from numpy.arange(5) of size=3
#
# b = np.random.choice(5,3,p=[0.1, 0, 0.3, 0.6, 0])
# print(b)
#
# ##Uniform random sample from numpy.arange(5) of size = 3 without replacement
#
# a = np.random.choice(5,3, replace=False)
# print(a)
#
# #N0n-Uniform random sample from numpy.arange(5) of size = 3 without replacement
#
# a = np.random.choice(5,3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
# print(a)
#
# aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
# x = np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
# print(x)

#
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import tensorflow as tf
# from sklearn import datasets
# from tensorflow.python.framework import ops
# ops.reset_default_graph()
#
# #Splitting the Input and Output from the dataset
#
# iris = datasets.load_iris()
# x_vals = np.array(x[0:3] for x in iris.data)
# y_vals = np.array(x[3] for x in iris.data)
#
# #Create Graph Session
# sess = tf.Session()
#
# #Set Seed
#
# seed = 3
# tf.set_random_seed(seed)
# np.random.random(seed)
#
# #Split data into train-test : 80%-20%
#
# train_indices = np.random.choice(len(x_vals), round(len(x_vals)*0.8), replace=False)
# test_indices = np.array(list(set(range(len(x_vals))) - set(train_indices)))
# x_vals_train  = x_vals[train_indices]
# x_vals_test = x_vals[test_indices]
# y_vals_train = y_vals[train_indices]
# y_vals_test = y_vals[test_indices]
#
# #Normalize by column [Min-Max Norm]
#
# def normalize_cols(m) :
#     cols_max = m.max(axis=0)
#     cols_min = m.min(axis=0)
#     return  (m-cols_min)/(cols_max-cols_min)
#
# x_vals_train = np.nan_to_num(normalize_cols(x_vals_train))
# x_vals_test = np.nan_to_num(normalize_cols(x_vals_test))
#
# #Declare batch size
# batch_size = 50

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import  datasets
from tensorflow.python.framework import ops
ops.reset_default_graph()

iris = datasets.load_iris()
x_vals = np.array(x[0:3] for x in iris)
y_vals = np.array(x[3] for x in iris)

sess = tf.Session()

seed = 3
tf.set_random_seed(seed)
np.random.random(seed)

train_indices = np.random.choice(len(x_vals), round(x_vals)*0.8)
test_indices = np.array(list(set(range(len(x_vals))) - set(train_indices)))
x_vals_train = x_vals[train_indices]
x_vals_test = x_vals[test_indices]
y_vals_train = y_vals[train_indices]
y_vals_test = y_vals[test_indices]

def normalize_cols(m) :
    cols_max = m.max(axis=0)
    cols_min = m.min(axis=0)
    return (m-cols_min)/(cols_max-cols_min)

x_vals_train = np.nan_to_num(normalize_cols(x_vals_train))
x_vals_test = np.nan_to_num(normalize_cols(x_vals_test))

batch_size = 50
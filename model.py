import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Conv2DTranspose
from helper import char_to_index, 

#Constants
LSTM_DIMENSION = 624
VOCAB_SIZE = 59
DENSE_DIMENSION_1 = 16384
DENSE_DIMENSION_2 = 512
DENSE_DIMENSION_3 = 512
DENSE_DIMENSION_4 = 512

class Model(object):
	def __init__(self, N):
		self.DIMENSIONS = DIMENSIONS #Set instance constants
		self.model = Sequential() #Create the model

		self.N = N #The test data size

		#Create the model layers
		self.model.add(LSTM(LSTM_DIMENSION, input_dim=VOCAB_SIZE, kernel_initializer='random_uniform', activation='tanh'))
		self.model.add(Dense(DENSE_DIMENSION_1, activation='relu', kernel_initializer='random_uniform', use_bias=True))
		self.mode.add(Dropout(0.2))
		self.model.add(Reshape(4, 4, 1024)) #This needs to be aligned with the actual images

		#Upsampling
		self.model.add(Conv2DTranspose(strides = (2, 2), kernel_size = (5, 5), data_format="channels_last")) # 8 x 8
		self.model.add(Conv2DTranspose(strides = (2, 2), kernel_size = (5, 5), data_format="channels_last")) # 16 x 16
		self.model.add(Conv2DTranspose(strides = (2, 2), kernel_size = (5, 5), data_format="channels_last")) # 32 x 32
		self.model.add(Conv2DTranspose(strides = (2, 2), kernel_size = (5, 5), data_format="channels_last")) # 64 x 64
		self.model.add(Conv2DTranspose(strides = (2, 2), kernel_size = (5, 5), data_format="channels_last")) # 128 x 128
		self.model.add(Conv2DTranspose(strides = (2, 2), kernel_size = (5, 5), data_format="channels_last")) # 256 x 256
		self.model.add(Conv2DTranspose(strides = (2, 2), kernel_size = (5, 5), data_format="channels_last")) # 512 x 512


	def train(test_data = None):
		#Prepare the test data
		for i in xrange(0, self.N):

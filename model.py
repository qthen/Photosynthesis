import numpy as np
import math
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Conv2DTranspose, Reshape
from helper import char_to_index, create_image, image_array
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.optimizers import Adagrad, Adam

#Constants
LSTM_DIMENSION = 1024
VOCAB_SIZE = 60
DENSE_DIMENSION_1 = 12288
DENSE_DIMENSION_2 = 512
DENSE_DIMENSION_3 = 512
DENSE_DIMENSION_4 = 512
MAX_LENGTH = 42

class Model(object):
	def __init__(self, N, LR = 0.01, optimizer = 'ada', momentum = 0.0):
		self.model = Sequential() #Create the model

		self.N = N #The test data size
		self.LR = LR

		#Create the optimizer
		if (optimizer == 'ada'):
			self.optimizer = Adagrad(lr=LR, epsilon=1e-08, decay=0.0)
		elif (optimizer == 'adam'):
			self.optimizer = Adam(lr=LR, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
		elif (optimizer == 'sgd'):
			self.optimizer = SGD(lr=LR, momentum=momentum, decay=0.0, nesterov=False)
		else:
			self.optimizer = RMSprop(lr=LR, rho=0.9, epsilon=1e-08, decay=0.0)


		#Create the model layers
		self.model.add(LSTM(LSTM_DIMENSION, input_shape=(42,VOCAB_SIZE), kernel_initializer='random_uniform', activation='tanh'))
		self.model.add(Dense(DENSE_DIMENSION_1, activation='relu', kernel_initializer='random_uniform', use_bias=True))
		self.model.add(Dropout(0.2))
		self.model.add(Reshape((4, 4, 768))) #This needs to be aligned with the actual images

		# #Upsampling
		self.model.add(Conv2DTranspose(kernel_initializer = 'random_uniform', filters = 264, strides = (2, 2), kernel_size = (2, 2), data_format="channels_last", activation='relu')) # 8 x 8
		self.model.add(Conv2DTranspose(kernel_initializer = 'random_uniform', filters = 128 ,strides = (2, 2), kernel_size = (2, 2), data_format="channels_last", activation='relu')) # 16 x 16
		self.model.add(Conv2DTranspose(kernel_initializer = 'random_uniform', filters = 64, strides = (2, 2), kernel_size = (2, 2), data_format="channels_last", activation='relu')) # 32 x 32
		self.model.add(Conv2DTranspose(kernel_initializer = 'random_uniform', filters = 32,strides = (2, 2), kernel_size = (2, 2), data_format="channels_last", activation='relu')) # 64 x 64
		self.model.add(Conv2DTranspose(kernel_initializer = 'random_uniform', filters = 8,strides = (2, 2), kernel_size = (2, 2), data_format="channels_last", activation='relu')) # 128 x 128
		self.model.add(Conv2DTranspose(kernel_initializer = 'random_uniform', filters = 8,strides = (2, 2), kernel_size = (2, 2), data_format="channels_last", activation='relu')) # 256 x 256
		self.model.add(Conv2DTranspose(kernel_initializer = 'random_uniform', filters = 3,strides = (2, 2), kernel_size = (2, 2), data_format="channels_last", activation='relu')) # 512 x 512

		#Compiling
		self.model.compile(optimizer=self.optimizer, loss = 'mean_squared_error')

		#Model summary
		self.model.summary()


	def train(self, test_data = None, epochs = 30):

		captions = []
		with open("dataset_captions/captions.txt") as fp:
			for line in fp:
				caption_text = [char_to_index(character) for character in line] #Convert to indices
				#Convert to encoding
				caption_text = to_categorical(caption_text, num_classes = VOCAB_SIZE)
				captions.append(caption_text)
		images = []
		#Prepare the test data and train on batch size = 1
		for i in range(0, self.N):
			rgb_img = image_array("dataset/test_{}.jpg".format(i))
			images.append(rgb_img)

		images = np.array(images)
		captions = np.array(captions)
		captions = pad_sequences(captions, maxlen=42)

		#Train here
		self.model.fit(captions, images, epochs = epochs, batch_size = 4)

		test_data = to_categorical([char_to_index(character) for character in "Red lights in a faraway city."], num_classes = VOCAB_SIZE)
		test_data = np.array([test_data])
		test_data = pad_sequences(test_data, maxlen = 42)

		#Predict a result
		prediction = self.model.predict(test_data, batch_size = 1)

		create_image(prediction[0])






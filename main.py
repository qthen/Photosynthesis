#Run the model
from model import Model
import sys

#Usage
#
# python main.py epochs learning_rate
# Epochs - how many times to train itself
# learning_rate - how fast it learns (faster means it might overstep and slower means takes longer to converge) typically arond 0.001 and 1
# optimizer - Choose between sgd, ada, rmsprop or adam

#System args
epochs, lr,optimizer = 500, 0.01, 'rmsprop'

#Parse command line
if len(sys.argv) >= 2:
	epochs = int(sys.argv[1])
if len(sys.argv) >= 3:
	lr = float(sys.argv[2])
if len(sys.argv) >= 4:
	optimizer = sys.argv[3]

NNModel = Model(N = 4, LR = lr, optimizer = optimizer)
NNModel.train(epochs=epochs)


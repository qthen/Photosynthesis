# Photosynthesis

A simple RNN that attempts to paint a picture based on text input with the goal of eventually being able to understand tangible structures and intangible descriptions and give rise to interesting and inspirational behaviour. Written in Keras and uses the Theano backend

##Layer Explanation

An LSTM layer that reads in each character one by one and outputs a 1024 dimensional vector that is fed into three fully connected layer for a final output of a 4096 vector. This is then upsampled and deconvoluted across 5 layers for a final output of a 256x256x3 matrix (3 channels for RGB) with each entry passed through a tanh activation with domain [0, 1]. This value denotes the percentage of red/green/blue at the current pixel level. The image can easily be reconstructed from this by multiplying the matrix by 255. 

import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from sklearn.metrics import classification_report, confusion_matrix
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image



#global variables
num_of_test_samples = 196
num_of_train_samples = 1190
batch_size = 32
img_dim = (64,64)

###################     network design       ###########################

#sequential classifier
classifier = Sequential()

#convolution layer
classifier.add(Conv2D(32,(2,2),input_shape= (64,64,3)))
classifier.add(Activation('relu'))

#pooling layer
classifier.add(MaxPooling2D(pool_size = (3,3)))
classifier.add(Flatten())

#dense units
classifier.add(Dense(units=1024))
classifier.add(Activation('relu'))

classifier.add(Dropout(0.5))

#output layer
classifier.add(Dense(units=4))
classifier.add(Activation('softmax')) #for multiple classes

classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])


#############        training data on model           ##################

train_dataGeneration = ImageDataGenerator(rescale=1.0/255,shear_range=0.2,zoom_range=0.2,horizontal_flip = True)
train_dataGeneration = ImageDataGenerator(rescale=1.0/255)

#get data
train_data = train_dataGeneration.flow_from_directory('/home/raghu/Desktop/assign2/code/dataSets/train/',target_size=img_dim, batch_size = batch_size,class_mode='categorical')
test_data = train_dataGeneration.flow_from_directory('/home/raghu/Desktop/assign2/code/dataSets/test/',target_size=img_dim,batch_size = batch_size,class_mode='categorical')

#training
classifier.fit_generator( train_data,steps_per_epoch = num_of_train_samples // batch_size, epochs = 15, validation_data=test_data,validation_steps=num_of_test_samples // batch_size)

#model summary
classifier.summary()


##############       confusion matrix            #######################
classPrediction = classifier.predict_generator(test_data, num_of_test_samples // batch_size)
classPrediction = np.argmax(classPrediction, axis=1)

print('Confusion Matrix')
print(confusion_matrix(test_data.classes, classPrediction))

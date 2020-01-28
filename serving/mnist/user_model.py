from tensorflow import keras
import numpy as np
import base64


class UserModel(object):

    def __init__(self):
        self.model = keras.models.load_model('model.h5')

    def predict(self, data):
        '''
        image: base64 encoded 28x28 image
        '''
        print(data)
        image = base64.decodebytes(data.image)
        print(image)

        # Create a batch of 1
        test_batch = image.reshape(1, image.shape[1], image.shape[0])
        print(test_batch.shape)

        softmax = self.model.predict(test_batch)

        return np.argmax(softmax)


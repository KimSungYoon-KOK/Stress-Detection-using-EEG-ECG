import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv1D, MaxPooling1D
from tensorflow.keras.layers import Dense, Flatten, Dropout, GlobalAveragePooling1D
from tensorflow.python.keras.backend import softmax
from tensorflow.python.keras.layers.core import Activation


# https://github.com/Apollo1840/deepECG
def DeepECGNet(input_dim, dropoutRate=0.5):

    # Input
    input1 = Input(shape=(input_dim, 1))

    # Model
    block1 = Conv1D(filters=128, kernel_size=55, activation='relu', input_shape=(input_dim, 1))(input1)
    block1 = MaxPooling1D(pool_size=10)(block1)
    block1 = Dropout(dropoutRate)(block1)

    block2 = Conv1D(128, 25, activation='relu')(block1)
    block2 = MaxPooling1D(5)(block2)
    block2 = Dropout(dropoutRate)(block2)

    block3 = Conv1D(128, 10, activation='relu')(block2)
    block3 = MaxPooling1D(5)(block3)
    block3 = Dropout(dropoutRate)(block3)

    block4 = Conv1D(128, 5, activation='relu')(block3)
    # block4 = GlobalAveragePooling1D()(block4)
    block4 = Flatten()(block4)

    dense = Dense(256, kernel_initializer='normal', activation='relu')(block4)
    dense = Dropout(dropoutRate)(dense)
    dense = Dense(128, kernel_initializer='normal', activation='relu')(dense)
    dense = Dropout(dropoutRate)(dense)
    dense = Dense(64, kernel_initializer='normal', activation='relu')(dense)
    dense = Dropout(dropoutRate)(dense)
    output1 = Dense(2)(dense)

    return Model(inputs=input1, outputs=output1)


import keras
import re
import string
import tensorflow
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

from keras.layers import *
from keras.models import *
from keras import backend as K

from keras_contrib.layers.crf import CRF, crf_loss, crf_viterbi_accuracy
from keras_contrib import losses

from attention import attention

import configparser
import h5py
import config


# LOAD POS TAGGER MODEL
def get_POS_TAGGER_model():
    
    # file = 'config.ini'
    # config = configparser.ConfigParser()
    # config.read(file)
    # pos_h5_filepath = config['PATHS']['pos_h5_filepath']
    
    modelx = h5py.File(config.pos_h5_filepath, 'r')
    
    custom_objects = {'attention': attention}

    model2 = keras.models.load_model(modelx, custom_objects={'attention': attention, "CRF": CRF, 'crf_loss': crf_loss,'crf_viterbi_accuracy': crf_viterbi_accuracy}, compile=True)
    model2.compile(optimizer=tf.optimizers.Adam(lr=0.008), loss=losses.crf_loss, metrics=[tf.keras.metrics.Recall(),tf.keras.metrics.AUC(),tf.keras.metrics.Precision(),'accuracy'])
    model2.summary()
    
    return model2

get_POS_TAGGER_model()
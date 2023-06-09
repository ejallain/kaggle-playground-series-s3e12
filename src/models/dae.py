#functions for denoising autoencoder (dae)
import numpy as np
import pandas as pd
from tensorflow import keras

def swap_noise(col, p=0.15):
    '''
    accepts a data column and probability (p) and returns a
    'noisy' column where each item has a probability = p of being swapped out
    for a random element from the column
    '''
    from random import random

    noisy_col = []
    for i in col:
        if random() <= p:
            noisy_col.append(np.random.choice(col, 1)[0])
        else:
            noisy_col.append(i)
    return noisy_col

def add_noise(df, p=0.15):
    '''
    adds noise to each col of the supplied df according to
    the supplied probability (p) using the swap_noise function
    returns a noisified df
    '''
    noisy_dict = {}
    for col in df.columns:
        noisy_dict[col] = swap_noise(df[col], p)
    return pd.DataFrame(noisy_dict)

def extract_features(model, X_train):
    '''
    accepts a trained dae model and a dataframe of X_train values
    as input and returns as dataframe of features based on the extracted
    node values for this training set
    '''
    feature_extractor = keras.Model(inputs=model.inputs,
                                    outputs=[layer.output for layer in model.layers])
    extracted_node_vals = feature_extractor.predict(X_train)
    feature_nodes = tuple(extracted_node_vals[i] for i in range(len(extracted_node_vals)-1))
    features = np.concatenate(feature_nodes, axis=1)
    features_df = pd.DataFrame(features)
    return(features_df)

import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle



def chat(x):
    # load trained model
    with open("chatbot\intents.json") as file:
        data = json.load(file)
    model = keras.models.load_model('chatbot/chat_model')

    # load tokenizer object
    with open('chatbot/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('chatbot/label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
    inp = x

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))
            return np.random.choice(i['responses'])
        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))



# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:54:50 2022

@author: User
"""

from flask import Flask,request
import tensorflow as tf
#from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import sys 
import os
import base64
sys.path.append(os.path.abspath("./model"))
from load import *
# from . import MDL
from utils import captchaSolverRPA
import json

# load model
from keras.models import model_from_json


# load keras model
def model_():
    try:
        jsonPath = '/model/model.json'
        weightsPath = '/model/model.h5'
        Path = '/model/captchaSolver.h5'
        
        try:
            with resources.open_binary('gimpysolver', modelPath) as model:
                ml = io.BytesIO(model.read())
                captcha_model = keras.models.load_model()
        except:
            globalPath = get_path()
            
            full_weightPath = globalPath + weightsPath
            full_jsonPath = globalPath + jsonPath
            fullPath = globalPath + Path
            
         #    json_file = open(jsonPath,'r')
         #    loaded_model_json = json_file.read()
         #    json_file.close()
         #    loaded_model = model_from_json(loaded_model_json)
        	# #load weights into new model
         #    loaded_model.load_weights(full_weightPath)
         #    print("Loaded Model from disk")
        
        	# #compile and evaluate loaded model
         #    loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
            
            
            captcha_model = keras.models.load_model(fullPath)
        return captcha_model
        # return loaded_model
    except Exception as err:
        print('Error while try to read model CaptchaSolver',err)
        return err

# declare global model
global model
model = model_()

#create the app
app = Flask(__name__)

@app.route("/predict/",methods=['POST'])
def predict():
    content_type = request.headers.get('Content-Type')
    print('json')
    if content_type == 'application/json':
        content = request.get_json(force=True)
        
        # Json to deserialization
        decodeimgArray = json.loads(content)
        # to array
        imgArray = np.asarray(decodeimgArray["array"])
            
        # create object captcha from array
        myCaptcha = captchaSolverRPA.captcha_solver(imgArray,model)
        # predict captcha
        myCaptchaSolved = myCaptcha.predict()
        
        # build response r
        response = {'predict':myCaptchaSolved}
        return response
    else:
        return "No Content-Type Support."
    
@app.route("/",methods=['GET'])
def home():
    return "Hola"

if __name__=="__main__":
    app.run(debug=False)
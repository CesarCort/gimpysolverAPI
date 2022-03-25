# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:07:38 2022

@author: User
"""

#import request
import cv2
import PIL
import json
from json import JSONEncoder
import numpy as np
import requests

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


path = './images/captcha_capture_0.png'
imgArray = cv2.imread(path,cv2.IMREAD_GRAYSCALE)

json_body_array = {"array":imgArray}
# Json to send
encode_numpy_data = json.dumps(json_body_array, cls=NumpyArrayEncoder)


url_post = 'http://127.0.0.1:5000/predict/'

r = requests.post(url_post,json=encode_numpy_data)

#%% receive




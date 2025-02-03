import socketio
import eventlet
import numpy as np
from flask import Flask
import tensorflow as tf
# from tensorflow.keras.models import Model , load_model
import os
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2
from keras.losses import mean_squared_error
from keras.saving import register_keras_serializable
# @K.register_keras_serializable()
# def custom_mse(y_true, y_pred):
#     return K.mean(K.square(y_true - y_pred))
@register_keras_serializable()
def mse(y_true,y_pred):
  return mean_squared_error(y_true,y_pred)

sio=socketio.Server()

app=Flask(__name__)
speed_limit=10

def img_preprocessing(img):
  img=img[60:135,:,:]
  img=cv2.cvtColor(img,cv2.COLOR_RGB2YUV)
  img=cv2.GaussianBlur(img,(3,3),0)
  img=cv2.resize(img,(200,66))
  img=img/255
  return img

@sio.on('connect')
def connect(sid, environ):
  print('Conneted')
  send_control(0,0)

def send_control(steering_angle, throttle):
  sio.emit('steer',data={
    'steering_angle':steering_angle.__str__(),
    'throttle':throttle.__str__()
  })

@sio.on('telemetry')
def telemetry(sid,data):
  speed=float(data['speed'])
  image=Image.open(BytesIO(base64.b64decode(data['image'])))
  image=np.asarray(image)
  image=img_preprocessing(image)
  image=np.array([image])
  steering_angle=float(model.predict(image))
  throttle=1.0-speed/speed_limit
  print('{} {} {}'.format(steering_angle,throttle,speed))
  send_control(steering_angle,throttle)

if __name__=='__main__':
  # model_path=os.path.join('Model','model.h5')
  model=load_model('Model/model.h5',custom_objects={'mse':mse})
  app=socketio.Middleware(sio,app)
  eventlet.wsgi.server(eventlet.listen(('',4567)),app)

import numpy as np
import cv2

IMG_SIZE = 128

def preprocess(img):
    img = np.array(img)
    img = cv2.resize(img,(IMG_SIZE,IMG_SIZE))
    img = img/255.0
    img = np.expand_dims(img,axis=0)
    return img

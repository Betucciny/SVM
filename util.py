import numpy as np
from PIL import Image



def vectorimg(img):
    vec = []
    for i in range(img.shape[0]):
        fila = img[i, :]
        vec += fila.tolist()
    return vec
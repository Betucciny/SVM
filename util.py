import numpy as np
from PIL import Image


def load_test():
    test = []
    path = "dataset/Test/"
    for i in range(1, 101):
        pathmale = path + "new_male/magen (" + str(i) + ").jpg"
        img = Image.open(pathmale)
        # img = img.resize((32, 32))
        img = np.array(img)
        vec = vectorimg(img)
        test.append((0, vec))
        pathfemale = path + "new_female/imagen (" + str(i) + ").jpg"
        img = Image.open(pathfemale)
        # img = img.resize((32, 32))
        img = np.array(img)
        vec = vectorimg(img)
        test.append((1, vec))
    return test


def load_train():
    train = []
    path = "dataset/Train/"
    for i in range(1, 501):
        pathmale = path + "newmale/imagen (" + str(i) + ").jpg"
        img = Image.open(pathmale)
        # img = img.resize((32, 32))
        img = np.array(img)
        vec = vectorimg(img)
        train.append((0, vec))
        pathfemale = path + "newfemale/imagen (" + str(i) + ").jpg"
        img = Image.open(pathfemale)
        # img = img.resize((32, 32))
        img = np.array(img)
        vec = vectorimg(img)
        train.append((1, vec))
    return train

def vectorimg(img):
    vec = []
    for i in range(img.shape[0]):
        fila = img[i, :]
        vec += fila.tolist()
    return vec
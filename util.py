import numpy as np
from PIL import Image


def load_test() -> object:
    x_test = []
    y_test = []
    path = "dataset/Test/"
    for i in range(1, 101):
        pathmale = path + "new_male/imagen (" + str(i) + ").jpg"
        img = Image.open(pathmale).convert('L')
        img = img.resize((32, 32))
        img = np.array(img)
        vec = vectorimg(img)
        x_test.append(vec)
        y_test.append(0)
        pathfemale = path + "new_female/imagen (" + str(i) + ").jpg"
        img = Image.open(pathfemale).convert('L')
        img = img.resize((32, 32))
        img = np.array(img)
        vec = vectorimg(img)
        x_test.append(vec)
        y_test.append(1)
    return np.asarray(x_test), np.asarray(y_test)


def load_train() -> object:
    x_train = []
    y_train = []
    path = "dataset/Training/"
    for i in range(1, 501):
        pathmale = path + "new_male/imagen (" + str(i) + ").jpg"
        img = Image.open(pathmale).convert('L')
        img = img.resize((32, 32))
        img = np.array(img)
        vec = vectorimg(img)
        x_train.append(vec)
        y_train.append(0)
        pathfemale = path + "new_female/imagen (" + str(i) + ").jpg"
        img = Image.open(pathfemale).convert('L')
        img = img.resize((32, 32))
        img = np.array(img)
        vec = vectorimg(img)
        x_train.append(vec)
        y_train.append(1)
    return np.asarray(x_train), np.asarray(y_train)


def load_data():
    x_train, y_train = load_train()
    x_test, y_test = load_test()
    return x_train, y_train, x_test, y_test


def vectorimg(img):
    vec = []
    for fila in img:
        vec += fila.tolist()
    return vec
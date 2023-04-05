from util import load_data
from sklearn.svm import SVC


def main():
    x_train, y_train, x_test, y_test = load_data()
    print(x_train.shape)
    print(y_train.shape)
    print(x_test.shape)
    print(y_test.shape)
    model = SVC()
    model.fit(x_train, y_train)
    buenas = 0
    for muestra, etiqueta in zip(x_test, y_test):
        predict = model.predict([muestra])
        print(f"Prediccion: {predict} - Etiqueta: {etiqueta}")
        if model.predict([muestra]) == etiqueta:
            buenas += 1
    print(buenas / len(x_test))


if __name__ == '__main__':
    main()

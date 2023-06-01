from model import poly_model

def main():
    y = [27, 6, 72, 4, 7, -86, -10, 24, -14, -92]
    x = [13, 66, -3, -99, 22, 38, 57, -85, -92, 85]
    degree = 3

    y_pred, params = poly_model(y, x, degree)

    print("Вектор предсказанных значений:", y_pred)
    print("Вектор параметров модели:", params)


if __name__ == '__main__':
    main()


from model import poly_model
from setting import DatabaseConnection
import logging
import sys


def main():
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(sys.stdout)
    log.addHandler(stdout_handler)

    y = [27, 6, 72, 4, 7, -86, -10, 24, -14, -92]
    x = [13, 66, -3, -99, 22, 38, 57, -85, -92, 85]
    degree = 3

    y_pred, params = poly_model(y, x, degree)

    logging.info("Вектор предсказанных значений:" + str(y_pred))
    logging.info("Вектор параметров модели:" + str(params))


if __name__ == '__main__':
    main()
    DatabaseConnection.close_connection()

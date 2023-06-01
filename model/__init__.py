from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
from db import db_logger
@db_logger
def poly_model(y, x, degree):
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)

    poly = PolynomialFeatures(degree=degree)
    x_poly = poly.fit_transform(x)

    model = LinearRegression()
    model.fit(x_poly, y)


    y_pred = model.predict(x_poly)

    return y_pred, [model.intercept_] + list(model.coef_[1:])
def _poly_model(y, x, degree):
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)

    poly = PolynomialFeatures(degree=degree)
    x_poly = poly.fit_transform(x)

    model = LinearRegression()
    model.fit(x_poly, y)


    y_pred = model.predict(x_poly)

    return y_pred, [model.intercept_] + list(model.coef_[1:])

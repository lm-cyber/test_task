import pytest
import numpy as np
from sklearn.metrics import mean_squared_error
from model import _poly_model


def test_poly_model():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([1, 3, 7, 13, 21])
    degree = 2
    y_pred, params = _poly_model(y, x, degree)
    assert isinstance(y_pred, np.ndarray)
    assert isinstance(params, list)
    assert y_pred.shape == y.shape
    assert params[0] == degree - 1

    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])
    degree = 2
    y_pred, params = _poly_model(y, x, degree)
    assert mean_squared_error(y, y_pred) < 1e-5


pytest.main()

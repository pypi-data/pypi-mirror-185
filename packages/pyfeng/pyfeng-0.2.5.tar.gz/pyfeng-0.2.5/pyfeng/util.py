import numpy as np

def avg_exp(x):
    """
    Integral_0^x exp(x) dx / x = ( exp(x) - 1 ) / x

    Args:
        x: argument

    Returns:
        value
    """
    with np.errstate(invalid="ignore"):
        rv = np.where(np.abs(x) < 1e-6,
                      1. + (x/2.)*(1. + (x/3.)),  # + o(x^3)
                      np.expm1(x)/x)
    return rv

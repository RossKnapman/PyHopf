import pytest
from pyhopf.hopfindex import HopfIndexCalculator
import numpy as np


@pytest.mark.parametrize('method', ['twopointstencil', 'fivepointstencil', 'solidangle', 'solidanglefourier'])
def test_hopf_index(method):

    """
    Test that the calculated Hopf index for a find discretisation (N = 100) is close to 1.
    """

    m = hopfion_compact_support_texture(100)

    hopf_index_calculator = HopfIndexCalculator(m, method)
    hopf_index_python = hopf_index_calculator.hopf_index()
    print(method, hopf_index_python)

    if method == 'twopointstencil':  # This is less accurate so don't expect to be as close to 1
        assert np.abs(hopf_index_python - 1.) < 0.05

    else:
        assert np.abs(hopf_index_python - 1.) < 0.01


def hopfion_compact_support_texture(N):

    """
    Compact support hopfion ansatz with N cells in each direction.
    """

    x = np.linspace(-0.5, 0.5, N)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    L = 0.25
    R = 0.2

    psi            = np.arctan2(Y, X)
    phi            = np.arctan2(Z, X*np.cos(psi) + Y*np.sin(psi) - L)
    Phi            = -phi + psi
    rho            = np.sqrt(Z**2 + (X*np.cos(psi) + Y*np.sin(psi) - L)**2)
    Theta          = np.pi * np.exp(1. - 1. / (1 - (rho / R)**2))
    Theta[rho > R] = 0.

    mx = np.cos(Phi) * np.sin(Theta)
    my = np.sin(Phi) * np.sin(Theta)
    mz = np.cos(Theta)

    m = np.zeros((*mx.shape, 3))
    m[:, :, :, 0] = mx
    m[:, :, :, 1] = my
    m[:, :, :, 2] = mz

    return m

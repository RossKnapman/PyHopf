.. PyHopf documentation master file, created by
   sphinx-quickstart on Tue Nov 12 10:36:13 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyHopf's Documentation!
==================================

This package provides Python implementations of the calculation of the Hopf index of the magnetisation texture for finite-difference micromagnetic simulations. The four methods implemented are `twopointstencil`, `fivepointstencil`, `solidangle`, and `solidanglefourier`. The package assumes NumPy arrays of the shape :math:`(N_x, N_y, N_z, 3)`, where :math:`N_i` are the number of cells in each direction, and the final dimension is for the three components. It is assumed that the vector field is normalised.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   gettingstarted
   api

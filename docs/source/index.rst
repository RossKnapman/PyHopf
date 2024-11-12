.. PyHopf documentation master file, created by
   sphinx-quickstart on Tue Nov 12 10:36:13 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyHopf's Documentation!
==================================

This package provides Python implementations of the calculation of the Hopf index of the magnetisation texture for finite-difference micromagnetic simulations. The four methods implemented are `twopointstencil`, `fivepointstencil`, `solidangle`, and `solidanglefourier`. The package assumes NumPy arrays of the shape :math:`(N_x, N_y, N_z, 3)`, where :math:`N_i` are the number of cells in each direction, and the final dimension is for the three components. It is assumed that the vector field is normalised.

Example usage to calculate the Hopf index, Hopf density :math:`\boldsymbol{F} \cdot \boldsymbol{A}`, and emergent magnetic field of a vector field stored in a file `Magnetisation.npy` using the solid angle method is shown in the following.::

   from PythonHopfIndex.hopfindex import HopfIndexCalculator

   m = np.load('Magnetisation.npy')

   hopf_index_calculator = HopfIndexCalculator(m, 'solidangle')
   hopf_index            = hopf_index_calculator.hopf_index()
   hopf_density          = hopf_index_calculator.hopf_density()
   emergent_field        = hopf_index_calculator.emergent_field()


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   api

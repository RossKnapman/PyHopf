Getting Started
===============

Installation
::::::::::::

.. code-block:: ipython

    pip install --upgrade pyhopf


Example Usage
:::::::::::::

Example usage to calculate the Hopf index, Hopf density :math:`\boldsymbol{F} \cdot \boldsymbol{A}`, and emergent magnetic field of a vector field stored in a file `Magnetisation.npy` using the solid angle method is shown in the following.

.. code-block:: ipython

   from pyhopf.hopfindex import HopfIndexCalculator

   m = np.load('Magnetisation.npy')

   hopf_index_calculator = HopfIndexCalculator(m, 'solidangle')
   hopf_index            = hopf_index_calculator.hopf_index()
   hopf_density          = hopf_index_calculator.hopf_density()
   emergent_field        = hopf_index_calculator.emergent_field()

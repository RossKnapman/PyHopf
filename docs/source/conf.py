import os
import sys
sys.path.insert(0, os.path.abspath('../../pyhopf'))  # Adjust path to point to your code location

project = 'PyHopf'
copyright = '2024, Ross Knapman'
author = 'Ross Knapman'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

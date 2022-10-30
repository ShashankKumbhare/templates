
# ==================================================================================================================================
# START >> FILE INFO
# ==================================================================================================================================
# File        : template_pkg/__dependencies_subpkg__/_dependencies_submod.py
# Author      : Shashank Kumbhare
# Date        : --/--/----
# email       : shashankkumbhare8@gmail.com
# Description : This file is a python submodule for python subpackage
#               'template_pkg.__dependencies_subpkg__'.
# ==================================================================================================================================
# END << FILE INFO
# ==================================================================================================================================



# ==================================================================================================================================
# START >> SUBMODULE >> template_pkg.__dependencies_subpkg__._dependencies_submod
# ==================================================================================================================================
# >>
"""
This submodule imports all the required 3rd party dependency packages/libraries for
the package which are then shared across all the package modules & submodules. All
the 3rd party dependency packages are imported here at one place and any other
dependencies are not to be imported in any module or submodule other than this
submodule.
"""



# ==================================================================================
# START >> IMPORTS
# ==================================================================================
# >>
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('classic')
style.use('seaborn-white')
from matplotlib.ticker import MultipleLocator
import math
import os
import sys
import inspect
import glob                                 # library for loading images from a directory
import matplotlib.image as mpimg
import cv2
import unittest
from scipy.stats import norm, lognorm, truncnorm
from scipy.stats import poisson
from scipy.special import logsumexp
from scipy import optimize
from IPython.display import Markdown, display, Latex
from textwrap import wrap
import random
# <<
# ==================================================================================
# END << IMPORTS
# ==================================================================================



# <<
# ==================================================================================================================================
# END << SUBMODULE << template_pkg.__dependencies_subpkg__._dependencies_submod
# ==================================================================================================================================

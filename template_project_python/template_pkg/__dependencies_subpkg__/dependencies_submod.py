
# ==================================================================================================================================
# START >> FILE INFO
# ==================================================================================================================================
# File        : template_pkg/template_subpackage/template_submodule.py
# Author      : Shashank Kumbhare
# Date        : --/--/----
# email       : shashankkumbhare8@gmail.com
# Description : This file is a python submodule for python subpackage
#               'template_pkg.__dependencies_subpkg__'.
# ==================================================================================================================================
# END << FILE INFO
# ==================================================================================================================================



# ==================================================================================================================================
# START >> SUBMODULE >> template_pkg.__dependencies_subpkg__.dependencies_submod
# ==================================================================================================================================
# >>
"""
This submodule imports all the required 3rd party dependency packages/libraries for
the package which are then shared across all the package modules & submodules. All
the 3rd party dependency packages are imported here at one place and any other
dependencies are not to be imported in any module or submodule other than this
submodule.
"""

_name_submod_ = __name__.partition(".")[-1]
print(f"   + Adding submodule '{_name_submod_}'...")

# ==================================================================================
# START >> IMPORTS
# ==================================================================================
# >>
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('classic')
style.use('seaborn-white')
import math
import os
import sys
import inspect
from progressbar import ProgressBar
# <<
# ==================================================================================
# END >> IMPORTS
# ==================================================================================

print("   - Done!")

# <<
# ==================================================================================================================================
# END << SUBMODULE << template_pkg.__dependencies_subpkg__.dependencies_submod
# ==================================================================================================================================

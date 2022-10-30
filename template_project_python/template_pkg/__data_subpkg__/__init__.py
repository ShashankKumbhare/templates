
# ==================================================================================================================================
# START >> FILE INFO
# ==================================================================================================================================
# File        : template_pkg/__data_subpkg__/__init__.py
# Author      : Shashank Kumbhare
# Date        : --/--/----
# email       : shashankkumbhare8@gmail.com
# Description : This file is a __init__ file for python subpackage
#               'template_pkg.__data_subpkg__'.
# ==================================================================================================================================
# END << FILE INFO
# ==================================================================================================================================



# ==================================================================================================================================
# START >> SUBPACKAGE >> template_pkg.__data_subpkg__
# ==================================================================================================================================
# >>
"""
This subpackage is created to store all the datasets for the package.
"""

_name_subpkg = __name__.partition(".")[-1]
print("")
print(f" + Adding subpackage '{_name_subpkg}'...")

# ==================================================================================
# START >> IMPORTS
# ==================================================================================
# >>
# SUBMODULES >>
from ._data_submod import *
# <<
# ==================================================================================
# END << IMPORTS
# ==================================================================================

print(" - Done!")

# <<
# ==================================================================================================================================
# END << SUBPACKAGE << template_pkg.__data_subpkg__
# ==================================================================================================================================
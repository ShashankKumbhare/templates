
# ==================================================================================================================================
# START >> FILE INFO
# ==================================================================================================================================
# File        : template_pkg/__constants_subpkg__/_constants_submod.py
# Author      : Shashank Kumbhare
# Date        : --/--/----
# email       : shashankkumbhare8@gmail.com
# Description : This file is a python submodule for python subpackage
#               'template_pkg.__constants_subpkg__'.
# ==================================================================================================================================
# END << FILE INFO
# ==================================================================================================================================



# ==================================================================================================================================
# START >> SUBMODULE >> template_pkg.__constants_subpkg__._constants_submod
# ==================================================================================================================================
# >>
"""
This submodule stores all the required constants for the package.
These constants will then be shared across all the package modules & submodules.
"""

_name_submod = __name__.partition(".")[-1]
print(f"   + Adding submodule '{_name_submod}'...")

# ==================================================================================
# START >> IMPORTS
# ==================================================================================
# >>
from ..__dependencies_subpkg__ import *
# <<
# ==================================================================================
# END << IMPORTS
# ==================================================================================


# ==================================================================================================================================
# START >> CONSTANTS
# ==================================================================================================================================
# >>
CONSTANT1 = 1
CONSTANT2 = 2
# <<
# ==================================================================================================================================
# END >> CONSTANTS
# ==================================================================================================================================

print("   - Done!")

# <<
# ==================================================================================================================================
# END << SUBMODULE << template_pkg.__constants_subpkg__._constants_submod
# ==================================================================================================================================


# ==================================================================================================================================
# START >> FILE INFO
# ==================================================================================================================================
# File        : template_pkg/__init__.py
# Author      : Shashank Kumbhare
# Date        : --/--/----
# email       : shashankkumbhare8@gmail.com
# Description : This file is a __init__ file for python package 'template_pkg'.
# ==================================================================================================================================
# END << FILE INFO
# ==================================================================================================================================



# ==================================================================================================================================
# START >> PACKAGE >> template_pkg
# ==================================================================================================================================
# >>s
"""
PACKAGE description PACKAGE description PACKAGE description PACKAGE description
PACKAGE description PACKAGE description.
"""

__version__  = '1.0.0'
_name_pkg    = __name__.partition(".")[0]
print("")
print(f"==========================================================================")
print(f"Importing package '{_name_pkg}'...")
print(f"==========================================================================")

# ==================================================================================
# START >> IMPORTS
# ==================================================================================
# >>
# MODULES >>
from .                        import helpers
# ELEMENTS >>
from .model                   import *
# <<
# ==================================================================================
# END << IMPORTS
# ==================================================================================

print(f"==========================================================================")
print(f"Package '{_name_pkg}' imported sucessfully !!")
print(f"==========================================================================")
print(f"version {__version__}")
print("")

# <<
# ==================================================================================================================================
# END << PACKAGE << template_pkg
# ==================================================================================================================================
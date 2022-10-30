
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
This package is xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
PACKAGE description PACKAGE description PACKAGE description PACKAGE description
PACKAGE description PACKAGE description.
"""

_name_pkg = __name__.partition(".")[0]
print("")
print(f"==========================================================================")
print(f"Importing package '{_name_pkg}'...")
print(f"==========================================================================")

# ==================================================================================
# START >> IMPORTS
# ==================================================================================
# >>
# SUBPACKAGES >>
# from .__dependencies_subpkg__ import *
# from .__constants_subpkg__    import *
# from .__auxil_subpkg__        import *
# from .__data_subpkg__         import *
from ._template_subpkg        import *
# MODULES >>
from ._template_mod           import *
# <<
# ==================================================================================
# END << IMPORTS
# ==================================================================================

print("")
print(f"==========================================================================")
print(f"Package '{_name_pkg}' imported sucessfully !!")
print(f"==========================================================================")
print("")

# <<
# ==================================================================================================================================
# END << PACKAGE << template_pkg
# ==================================================================================================================================

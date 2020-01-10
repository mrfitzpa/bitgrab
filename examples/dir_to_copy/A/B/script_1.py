#!/usr/bin/env python
"""A python script.
"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For finding paths to files, and listing files and directories.
import os



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2020"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mfitzpatrick@dwavesys.com"
__status__     = "Development"



#########################
## Main body of script ##
#########################

path_to_current_file = os.path.abspath(os.path.dirname(__file__))
print("Absolute path to current file =", path_to_current_file)

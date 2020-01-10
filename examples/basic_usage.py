#!/usr/bin/env python
"""Demonstration of the basic usage of ``bitgrab``.

This example includes the following steps:
1) Choose a directory to copy.
2) Store contents of directory into a :class:`bitgrab.Dir` object, i.e.
   construct :class:`bitgrab.Dir` object.
3) Use object's :meth:`bitgrab.Dir.copy_to` method to copy contents of original
   directory into a new directory.
"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For finding paths to files, and listing files and directories.
import os



# Import bitgrab.
import bitgrab



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

dirname = os.path.abspath(os.path.dirname(__file__)) + '/dir_to_copy'
dir_obj = bitgrab.Dir(dirname)  # Store contents of directory in an object.

new_dirname = os.path.abspath(os.path.dirname(__file__)) + '/dir_copy'
dir_obj.copy_to(new_dirname)  # Copy directory contents into a new directory.

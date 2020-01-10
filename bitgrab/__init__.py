#!/usr/bin/env python
"""``bitgrab`` is a small Python module used to read every file in a given
directory (including its subdirectories), store the contents (in the form of
bits) into a data object, which can later be used to copy the same contents into
a new directory, maintaining the subdirectory structure.
"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For file and directory related operations.
import os

# For making directories (i.e. emulating mkdir).
import pathlib



# To get version of bitgrab.
from . import version



############################
## Authorship information ##
############################

__author__       = "Matthew Fitzpatrick"
__copyright__    = "Copyright 2020"
__credits__      = ["Matthew Fitzpatrick"]
__version__      = version.version
__full_version__ = version.full_version
__maintainer__   = "Matthew Fitzpatrick"
__email__        = "mfitzpatrick@dwavesys.com"
__status__       = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in package.
__all__ = ["show_config", "File", "Dir"]



def show_config():
    """Print information about the version of :mod:`bitgrab`.

    Parameters
    ----------

    Returns
    -------
    """
    print(version.version_summary)

    return None



class File():
    r"""Stores data and certain metadata of a file.

    Parameters
    ----------
    filename : `str`
        The relative or absolute filename of the file of interest.

    Attributes
    ----------
    basename : `str`
        Basename of file.
    filename : `str`
        Absolute filename.
    data : `bytes`
        The data content of the file.
    """
    def __init__(self, filename):
        with open(filename, 'rb') as file_handle:
            self.data = file_handle.read()
            
        self.basename = os.path.basename(filename)
        self.filename = os.path.abspath(filename)

        return None


    
    def copy_to(self, new_filename):
        r"""Copy data content to a new file.

        Parameters
        ----------
        new_filename : `str`
            The relative or absolute filename of the new file. If a file already
            exists with the given filename, then it is overwritten with the new
            data content.

        Returns
        -------
        """
        with open(new_filename, 'wb') as file_handle:
            file_handle.write(self.data)

        return None



class Dir():
    r"""Stores data of files within a directory and the subdirectories therein.

    Parameters
    ----------
    dirname : `str`
        The relative or absolute path to the directory.

    Attributes
    ----------
    basename : `str`
        Basename of directory.
    dirname : `str`
        Absolute path to the directory.
    files : array_like(:class:`bitgrab.File`, ndim=1)
        Contains the data of every file within the directory and subdirectories
        therein.
    subdirnames : array_like(`str`, ndim=1)
        The list of absolute paths to all subdirectories.
    """
    def __init__(self, dirname):
        dir_tree = list(os.walk(dirname))  # See doc of os.walk for details.
        if dir_tree == []:
            raise NotADirectoryError("Directory does not exist.")

        self.dirname = os.path.abspath(dir_tree[0][0])
        self.basename = os.path.basename(self.dirname)

        self.files = []
        self.subdirnames = []
        
        for x in dir_tree:
            subdirname = x[0]
            self.subdirnames += [subdirname]

            file_basenames = x[2]
            for file_basename in file_basenames:
                filename = subdirname + '/' + file_basename
                file_obj = File(filename)
                self.files += [file_obj]

        self.subdirnames.pop(0)

        return None


    
    def copy_to(self, new_dirname):
        r"""Copy entire file data content of directory to a new directory.

        Parameters
        ----------
        new_directory : `str`
            The relative or absolute path to the new directory. If the directory
            already exists with the given path, then it is overwritten with the
            new file data content.

        Returns
        -------
        """
        pathlib.Path(new_dirname).mkdir(parents=True, exist_ok=True)

        for subdirname in self.subdirnames:
            new_subdirname = subdirname.replace(self.dirname, new_dirname)
            pathlib.Path(new_subdirname).mkdir(parents=True, exist_ok=True)

        for file_obj in self.files:
            new_filename = file_obj.filename.replace(self.dirname, new_dirname)
            file_obj.copy_to(new_filename)

        return None

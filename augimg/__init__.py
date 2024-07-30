"""Imports for package augimg."""
from __future__ import absolute_import

# this contains some deprecated classes/functions pointing to the new
# classes/functions, hence always place the other imports below this so that
# the deprecated stuff gets overwritten as much as possible
from augimg.augimg import *  # pylint: disable=redefined-builtin

import augimg.augmentables as augmentables
from augimg.augmentables import *
import augimg.augmenters as augmenters
import augimg.parameters as parameters
import augimg.dtypes as dtypes
import augimg.data as data

__version__ = '0.4.0'

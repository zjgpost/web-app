from __future__ import generators

__version_info__=(2,3,0)
__version__='.'.join(map(str,__version__))
__author__="Trent Mick"

import os
import sys
from pprint import pprint,pformat
import re
import logging
try:
    from hashlib import md5
except ImportError:
    from md5 import _md5
    
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

import logging

from .controller import main


__version__ = '0.0.6'

logger = logging.getLogger("mayarepacker")
logger.setLevel(logging.DEBUG)
logger.propagate = False

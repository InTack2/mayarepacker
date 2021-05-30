# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

import os

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

from maya.app.general import mayaMixin
from maya import cmds

from PySide2 import QtWidgets

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


class View(mayaMixin.MayaQWidgetDockableMixin, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, "ui", "MayaAutoPackageReloader.ui"))
        self.setCentralWidget(self.ui)
        self.setWindowTitle(self.ui.windowTitle())
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

import os

from PySide2 import QtCore, QtWidgets
from PySide2.QtUiTools import QUiLoader

from maya.app.general import mayaMixin

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

settings_path = None
if os.name == "nt":
    settings_path = os.environ["APPDATA"]
else:
    settings_path = "library/preferences"


SETTING_CURRENT_PATH = settings_path


class View(mayaMixin.MayaQWidgetDockableMixin, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, "ui", "MayaAutoPackageReloader.ui"))
        self.setCentralWidget(self.ui)
        self.setWindowTitle(self.ui.windowTitle())
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.settings = QtCore.QSettings(os.path.join(SETTING_CURRENT_PATH, "setting.ini"), QtCore.QSettings.IniFormat)

    def showEvent(self, event):
        super(View, self).showEvent(event)

        self.__load_settings()

    def closeEvent(self, event):
        super(View, self).closeEvent(event)

        self.__save_settings()

    def __load_settings(self):
        self.ui.ReloadTargetBox.setCurrentText(self.settings.value(self.ui.ReloadTargetBox.objectName(), ""))
        self.ui.PathLineEdit.setText(self.settings.value(self.ui.PathLineEdit.objectName(), ""))

    def __save_settings(self):
        self.settings.setValue(self.ui.ReloadTargetBox.objectName(), self.ui.ReloadTargetBox.currentText())
        self.settings.setValue(self.ui.PathLineEdit.objectName(), self.ui.PathLineEdit.text())

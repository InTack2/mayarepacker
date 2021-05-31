#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

import threading

from . import view
from . import server

from PySide2 import QtCore

from maya import cmds


class Controller(object):
    def __init__(self):
        self.gui = view.View()

        self.reload_server = server.ReloadServer()
        self._filter = None

        self.setup_event()

    def setup_event(self):
        self.gui.ui.OpenFolderButton.clicked.connect(self.select_folder_dialog)
        self.gui.ui.StartMonitorButton.clicked.connect(self.start_monitor)
        self.gui.ui.EndMonitorButton.clicked.connect(self.end_monitor)

        self._filter = Filter(self.end_monitor)
        self.gui.installEventFilter(self._filter)

    def select_folder_dialog(self):
        select_path = cmds.fileDialog2(dialogStyle=2, fileMode=3)[0]
        self.gui.ui.PathLineEdit.setText(select_path)

    def start_monitor(self):
        target_path = self.gui.ui.PathLineEdit.text()

        thread_1 = threading.Thread(name="MonitoringThread", target=self.reload_server.start, args=[target_path])
        thread_1.start()

        self.gui.ui.StartMonitorButton.setEnabled(False)
        self.gui.ui.EndMonitorButton.setEnabled(True)

    def end_monitor(self):
        self.reload_server.stop()

        self.gui.ui.StartMonitorButton.setEnabled(True)
        self.gui.ui.EndMonitorButton.setEnabled(False)


class Filter(QtCore.QObject):
    def __init__(self, close_event):
        super(Filter, self).__init__()
        self.__close_event = close_event

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.Close:
            self.__close_event()
            print("cloe call.")

        return False


def main():
    global MayaAutoReloader

    try:
        MayaAutoReloader.gui.close()
    except:
        pass

    MayaAutoReloader = Controller()
    MayaAutoReloader.gui.show()

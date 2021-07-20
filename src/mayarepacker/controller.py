# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

import threading
import sys
import logging
from functools import partial

from . import view
from . import server

from PySide2 import QtCore

try:
    from PySide2.QtCore import QStringListModel
except ImportError:
    from PySide2.QtGui import QStringListModel

from maya import cmds


class Controller(object):
    def __init__(self):
        self.gui = view.View()

        self.reload_server = server.ReloadServer()
        self._filter = None

        self.setup_event()

        self.logger = logging.getLogger("mayarepacker")

        self.logger.handlers = []
        self.logger.addHandler(GUILogHandler(self.gui.ui.ConsoleTextEdit))

    def setup_event(self):
        self.gui.ui.OpenFolderButton.clicked.connect(self.select_folder_dialog)
        self.gui.ui.StartMonitorButton.clicked.connect(self.start_monitor)
        self.gui.ui.EndMonitorButton.clicked.connect(self.end_monitor)
        self.gui.ui.ManualReloadButton.clicked.connect(self.reload_manual)

        self.gui.ui.ConsoleTextEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.gui.ui.ConsoleTextEdit.customContextMenuRequested.connect(self.clear_console)

        self.__update_completer()

        self._filter = Filter(self.end_monitor, self.__update_completer)
        self.gui.installEventFilter(self._filter)

    def select_folder_dialog(self):
        select_path = cmds.fileDialog2(dialogStyle=2, fileMode=3)[0]
        if not select_path:
            return

        self.gui.ui.PathLineEdit.setText(select_path)

    def start_monitor(self):
        target_path = self.gui.ui.PathLineEdit.text()
        target_module = self.gui.ui.ReloadTargetBox.currentText()

        if not target_path or not target_module:
            return

        thread_1 = threading.Thread(name="MonitoringThread", target=self.reload_server.start, args=[target_path, target_module])
        thread_1.start()

        self.gui.ui.PathLineEdit.setEnabled(False)
        self.gui.ui.OpenFolderButton.setEnabled(False)
        self.gui.ui.ReloadTargetBox.setEnabled(False)

        self.gui.ui.StartMonitorButton.setEnabled(False)
        self.gui.ui.EndMonitorButton.setEnabled(True)
        self.gui.ui.ManualReloadButton.setEnabled(False)

    def end_monitor(self):
        self.reload_server.stop()

        self.gui.ui.PathLineEdit.setEnabled(True)
        self.gui.ui.OpenFolderButton.setEnabled(True)
        self.gui.ui.ReloadTargetBox.setEnabled(True)

        self.gui.ui.StartMonitorButton.setEnabled(True)
        self.gui.ui.EndMonitorButton.setEnabled(False)
        self.gui.ui.ManualReloadButton.setEnabled(True)

    def __update_completer(self):
        if not self.reload_server.is_monitor:
            current_text = self.gui.ui.ReloadTargetBox.currentText()

            self.gui.ui.ReloadTargetBox.clear()

            target_completer = [_ for _ in sys.modules]
            target_completer.sort()

            self.gui.ui.ReloadTargetBox.addItems(target_completer)
            self.gui.ui.ReloadTargetBox.setCurrentText(current_text)

            self.gui.comp.setModel(QStringListModel(target_completer))
            self.gui.ui.ReloadTargetBox.setCompleter(self.gui.comp)

    def reload_manual(self):
        from . import app

        target_module = self.gui.ui.ReloadTargetBox.currentText()
        if not target_module:
            return

        app.remove_include_module(target_module)

    def clear_console(self):
        self.gui.ui.ConsoleTextEdit.clear()


class Filter(QtCore.QObject):
    def __init__(self, close_event, focus_event):
        super(Filter, self).__init__()
        self.__close_event = close_event
        self.__focus_event = focus_event

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.Close:
            self.__close_event()
        if event.type() == QtCore.QEvent.WindowActivate:
            self.__focus_event()

        return False


def main():
    global MayaAutoReloader

    try:
        MayaAutoReloader.gui.close()
    except:
        pass

    MayaAutoReloader = Controller()
    MayaAutoReloader.gui.show()


class GUILogHandler(logging.Handler):
    def __init__(self, plain_text_edit, level=logging.NOTSET):
        super(GUILogHandler, self).__init__(level=level)
        self.plain_text_edit = plain_text_edit
        self.createLock()

    def emit(self, record):
        import maya
        if len(record.msg) > 0:
            msg = self.format(record)
        else:
            msg = ""

        maya.utils.executeInMainThreadWithResult(partial(self.plain_text_edit.verticalScrollBar().setValue, self.plain_text_edit.verticalScrollBar().maximum()))
        maya.utils.executeInMainThreadWithResult(partial(self.plain_text_edit.appendPlainText, msg))

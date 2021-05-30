# -*- coding: utf-8 -*-
"""サーバー関連

"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

import sys
import os

import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ReloadServer(object):
    def __init__(self):
        self.observer = None

        self.is_monitor = False

    def start(self, target_path):
        folder_name = os.path.basename(target_path)

        print("folder_name", folder_name)

        self.observer = Observer()
        self.observer.schedule(MayaModuleReloadEventhandler(folder_name), target_path, recursive=True)

        self.observer.start()
        self.is_monitor = True

        try:
            while self.is_monitor:
                time.sleep(1)
        finally:
            self.observer.stop()
            self.observer.join()

    def stop(self):
        self.is_monitor = False


class MayaModuleReloadEventhandler(FileSystemEventHandler):
    def __init__(self, folder_name):
        self.folder_name = folder_name

    def on_any_event(self, event):

        for k in list(sys.modules):
            if k.startswith(self.folder_name):
                print(k)
                del sys.modules[k]

        print("__module__", __package__)
        print("__name__", __name__)

        print(self.folder_name)


class SingletonMultiInstanceError(Exception):
    pass

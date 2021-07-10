# -*- coding: utf-8 -*-
"""サーバー関連

"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division
import logging

import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from . import app


class ReloadServer(object):
    def __init__(self):
        self.observer = None

        self.is_monitor = False

    def start(self, target_path, target_module):
        self.observer = Observer()
        self.observer.schedule(MayaModuleReloadEventhandler(target_module), target_path, recursive=True)

        self.observer.start()
        self.is_monitor = True

        try:
            while self.is_monitor:
                time.sleep(3)
        finally:
            self.observer.stop()
            self.observer.join()

    def stop(self):
        self.is_monitor = False


class MayaModuleReloadEventhandler(PatternMatchingEventHandler):
    def __init__(self, reload_target_name):
        super(MayaModuleReloadEventhandler, self).__init__(patterns=["*.py"], ignore_patterns=["*.pyc"])
        self.reload_target_name = reload_target_name

        self.logger = logging.getLogger("mayarepacker")

    def on_any_event(self, event):
        self.logger.info("================================================")
        self.logger.info("reload name : {}".format(self.reload_target_name))
        self.logger.info("event name : {}".format(event.event_type))
        self.logger.info("event path : {}".format(event.src_path))
        self.logger.info("================================================")

        app.remove_include_module(self.reload_target_name)


class SingletonMultiInstanceError(Exception):
    pass

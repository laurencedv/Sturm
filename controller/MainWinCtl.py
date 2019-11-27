#!/usr/bin/python3
import logging
from PySide2.QtCore import QObject

class MainWinCtl(object):
    def __init__(self, model):
        super().__init__()
        self.log = logging.getLogger(__name__)
        if model is None:
            self.log.error("Model cannot be None!")
        self.MCUdb = model


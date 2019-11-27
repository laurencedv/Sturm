#!/usr/bin/python3

import sys
import logging

from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

class win_main(QMainWindow):
    def __init__(self, model, controller):
        super().__init__()
        self.log = logging.getLogger(__name__)
        if controller is None:
            self.log.error("Controller cannot be None!")
        if model is None:
            self.log.error("Model cannot be None!")
        self.controller = controller
        self.model = model
    
    def run(self):
        uiFile = QFile("./view/win_main.ui")
        uiFile.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(uiFile)

        self._setup()
        self.window.show()

    def _setup(self):
        self.log.debug("Main window setup")


import sys
import logging

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QFile

class win_MCUdbViewer(QDialog):
    def __init__(self, model, controller):
        super().__init__()
        self.log = logging.getLogger(__name__)
        if controller is None:
            self.log.error("Controller cannot be None!")
        if model is None:
            self.log.error("Model cannot be None!")
        self.MCUdb = model
        self.ctl = controller

        uiFile = QFile("./view/win_MCUdbViewer.ui")
        uiFile.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(uiFile)

    def run(self):
        self._setup()
        self.window.show()

    def _setup(self):
        self.log.debug("MCUdbViewer setup")

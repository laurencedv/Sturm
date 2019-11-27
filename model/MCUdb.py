#!/usr/bin/python3
import logging
from PySide2.QtCore import QObject
from util.MCUcrawler import MCUcrawler

class MCUdb(QObject):

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger(__name__)
        self.crawler = MCUcrawler()
        self.data = []

    def populate(self, searchPath):
        self.log.info("Populating MCU db with crawler @%s", searchPath)
        newMCU = self.crawler.search(searchPath)        # Launch crawler against defined search path
        
        # validate newMCU

        # add newMCU in self
    
    def isValid(self):
        self.log.warning("IMPLEMENT validation of MCUdb")
        return True

    def getData(self):
        return self.data

    def setData(self, data):
        if data is not None:
            self.data = data

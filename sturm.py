#!/usr/bin/python3

#Std stuff
import sys
import os
import logging
import argparse
import pickle

#Qt stuff
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt, QFile, QCoreApplication

#Project stuff
from model.MCUdb import MCUdb
from controller.MainWinCtl import MainWinCtl
from controller.MCUdbViewerCtl import MCUdbViewerCtl
from controller.MCUselectorCtl import MCUselectorCtl
from view.win_main import win_main
from view.win_MCUdbViewer import win_MCUdbViewer
from view.diag_MCUselector import diag_MCUselector
from util.MCUcrawler import MCUcrawler
from type import *

class sturm(QApplication):
    MCUdb = None
    argParser = argparse.ArgumentParser()

    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        """Arguments"""
        self.argParser.add_argument("--db", help="Specify an MCU db file (IO)", default="./data/mcu.db")
        self.argParser.add_argument("-s", "--search", help="Specify a search path for mcu detection", default="/opt/Silabs/SimplicityStudio/developer/sdks")
        self.argParser.add_argument("--nogui", help="Force the app to not initialize the gui", action="store_true")
        self.argParser.add_argument("-v", "--verbosity", help="Adjust verbosity level of console", type=str, choices=["DEBUG","INFO","WARNING","ERROR"], default="ERROR")
        args = self.argParser.parse_args()
        self.dbPath = args.db
        self.searchPath = args.search
        self.nogui = args.nogui
        if args.verbosity == "DEBUG":
            consoleVerbosity = logging.DEBUG
        elif args.verbosity == "INFO":
            consoleVerbosity = logging.INFO
        elif args.verbosity == "WARNING":
            consoleVerbosity = logging.WARNING
        else:
            consoleVerbosity = logging.ERROR

        """Logging"""
        logging.basicConfig(filename="sturm.log",
                            filemode='w',
                            format='%(asctime)s,%(msecs)d|%(levelname)s|%(name)s|%(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
        self.log = logging.getLogger(__name__)
        console = logging.StreamHandler()
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setLevel(consoleVerbosity)
        console.setFormatter(formatter)
        self.log.addHandler(console)
        self.log.info("Console verbosity set to {}".format(args.verbosity))
        self.log.debug('Sturm app launched')

        """Childrens"""
        self.MCUdb = MCUdb()

        if self.nogui is False:
            self.MainWinCtl = MainWinCtl(model=self.MCUdb)
            self.MCUdbViewerCtl = MCUdbViewerCtl(model=self.MCUdb)
            self.MCUselectorCtl = MCUselectorCtl(model=self.MCUdb)

            self.MainWin = win_main(model=self.MCUdb, controller=self.MainWinCtl)
            self.MCUdbViewer = win_MCUdbViewer(model=self.MCUdb, controller=self.MCUdbViewerCtl)
            self.MCUselector = diag_MCUselector(model=self.MCUdb, controller=self.MCUselectorCtl)
            self.log.debug("Gui object created")

    def run(self):
        self.loadMCUdb()

        if self.nogui is False:
            self.MainWin.run()
            self.MCUdbViewer.run()

    def loadMCUdb(self):
        # First try to load previous db
        try:
            filehandler = open(self.dbPath, 'rb')
            self.log.debug("MCU db file:%s", filehandler)
        except FileNotFoundError:
            # File not found, so create it
            self.log.info("MCU db not found at %s", self.dbPath)
            self.MCUdb.populate(self.searchPath)
            
            # Then, write the actual db file for next time
            try:
                filehandler = open(self.dbPath, 'wb')
                pickle.dump(self.MCUdb.getData(), filehandler)
            except Exception as e:
                # Not supposed to happen, investiguate!
                raise e
            return

        # File found, so we simply load it
        try:
            self.MCUdb.setData(pickle.load(filehandler))
        except Exception:
            os.remove(self.dbPath)
            self.loadMCUdb()    #restart the process, without a file this time

        # Validate the content
        if self.MCUdb.isValid() == False:
            #wipe the file and rebuild it
            os.remove(filehandler)
            self.loadMCUdb()    #restart the process, without a file this time

        self.log.debug("Using MCU db: %s", self.dbPath)
        

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)    #Shush the warning!
    inst = sturm(sys.argv)
    inst.run()
    sys.exit(inst.exec_())

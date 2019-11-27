#!/usr/bin/python3
import sys
import os
import logging
from type import *

class MCUcrawler(object):
    def __init__(self):
        super().__init__()
        self.log = logging.getLogger(__name__)

    def search(self, path):
        self.log.debug("Starting crawler @%s", path)

        MCUlist = ["hello", "mon", "ti", "coco"]

        return MCUlist

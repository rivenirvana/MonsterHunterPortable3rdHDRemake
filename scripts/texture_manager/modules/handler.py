#!/usr/bin/env python3
# handler.py

import os.path as osp

from constants import HASH_DIR
from watchdog.events import RegexMatchingEventHandler

NULL_BYTE = "00000000"
HASH_FILE = HASH_DIR + "hashes.txt"


class TextureHandler(RegexMatchingEventHandler):
    TEXTURE_REGEX = [r"^.*\.png$"]

    def __init__(self):
        super().__init__(self.TEXTURE_REGEX)

    def on_any_event(self, event):
        print(event)

    def on_created(self, event):
        print("File created.")
        self.process(event)

    def on_deleted(self, event):
        print("File deleted.")

    def on_modified(self, event):
        print("File modified.")

    def on_moved(self, event):
        print("File moved.")

    def process(self, new_file):
        hash, ext = osp.splitext(new_file.src_path)
        print(hash, ext)

        with open(HASH_FILE, "a") as f:
            f.write(f"{hash}\n")
            f.write(f"{NULL_BYTE}{hash[8:]}\n")


class CatalogHandler(RegexMatchingEventHandler):
    TXT_REGEX = [r"^.*\.txt$"]

    def __init__(self):
        super().__init__(self.TXT_REGEX)

    def on_any_event(self, event):
        print(event)

    def on_created(self, event):
        print("File created.")

    def on_deleted(self, event):
        print("File deleted.")
        if event.src_path == HASH_FILE:
            raise Exception

    def on_modified(self, event):
        print("File modified.")

    def on_moved(self, event):
        if event.src_path == HASH_FILE:
            raise Exception
        print("File moved.")

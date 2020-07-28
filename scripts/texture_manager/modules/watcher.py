#!/usr/bin/env python3
# watcher.py

import os
import sys
import time

from watchdog.observers import Observer
from modules.handler import TextureHandler, CatalogHandler


class TextureWatcher:
    def __init__(self, game_dir, hash_dir):
        self.__game_dir = game_dir
        self.__hash_dir = hash_dir
        self.__texture_handler = TextureHandler()
        self.__catalog_handler = CatalogHandler()
        self.__event_observer = Observer()

    def run(self):
        try:
            self.start()
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            print(e)
            try:
                self.stop()
            except:
                sys.exit(1)

    def start(self):
        if not os.path.isdir(self.__game_dir):
            os.mkdir(self.__game_dir)
        if not os.path.isdir(self.__hash_dir):
            os.mkdir(self.__hash_dir)
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__texture_handler, self.__game_dir, recursive=True
        )
        print("Watching game dir...")
        self.__event_observer.schedule(
            self.__catalog_handler, self.__hash_dir, recursive=True
        )
        print("Watching hash dir...")

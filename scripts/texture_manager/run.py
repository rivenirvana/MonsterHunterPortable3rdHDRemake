#!/usr/bin/env python3
# run.py

from modules.constants import GAME_DIR, HASH_DIR
from modules.watcher import TextureWatcher

if __name__ == "__main__":
    TextureWatcher(GAME_DIR, HASH_DIR).run()

#!/usr/bin/env python3

import sys

from scripts.texture_manager.modules.watcher import TextureWatcher

if __name__ == "__main__":
    src_path = sys.argv[1] if len(sys.argv) > 1 else "."
    TextureWatcher(src_path).run()

import shutil
import os
import sys

# send2trash.send2trash('..' + os.path.sep + "chapter_10_debugging")
# send2trash seems to be not working for macOS at all.

shutil.rmtree('..' + os.path.sep + "chapter_10_debugging")

#! python
"""
prep_folder.py - a script to create a new chapter folder for note taking purposes
"""

import os
import shutil
import sys


foldername = str(input("Please input folder name"))
default_path = ".." + os.path.sep


new_dir = default_path + os.path.sep + \
    foldername + os.path.sep + "practice folder"
os.makedirs(new_dir)
with open(f"{new_dir}{os.path.sep}practice.py", 'w'):
    pass
with open(".." + os.path.sep + foldername + os.path.sep + "chapter_notes.md", 'w'):
    pass

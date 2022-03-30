#! python
"""
prep_folder.py - a script to create a new chapter folder for note taking purposes
"""

import os
import shutil
import sys


try:
    foldername = sys.argv[1]
except IndexError:
    print("""Please enter a correct filename, correct usage:
    python3 prep_folder.py chapter_10_debugging""")
    sys.exit()

# create the new folder(s)
new_dir = ".." + os.path.sep + foldername + os.path.sep + "misc_practice"

# populate the new folder with the correct template note files
os.makedirs(new_dir)
with open(f"{new_dir}{os.path.sep}practice.py", 'w') as practice:
    practice.write('#! python3')

with open(".." + os.path.sep + foldername + os.path.sep + "chapter_notes.md", 'w') as chapter_note:
    section_breaker = "\n\n\n"
    chapter_note.write(f"# {sys.argv[1]} notes!\n\n")
    chapter_note.write("## Introduction")
    chapter_note.write(section_breaker)
    chapter_note.write("## Reference Notes")
    chapter_note.write(section_breaker)
    chapter_note.write("## Practice Projects")

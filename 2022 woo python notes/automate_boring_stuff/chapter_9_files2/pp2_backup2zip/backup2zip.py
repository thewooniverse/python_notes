#! python3
"""
backup2zip.py - a python script that receives a 
usable from anywhere :)

"""
import os
import sys
import zipfile
import logging

# basic configurations
directories = ["error_logs", "backed_up_files", "test_files"]
for directory in directories:
    try:
        os.makedirs(os.getcwd()+os.path.sep+directory)
    except FileExistsError:
        pass

basename = os.path.basename(__file__).split('.')[0]
logging.basicConfig(level=logging.DEBUG, filename=f'{os.getcwd()+os.path.sep}error_logs{os.path.sep+basename}.txt',
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug(f'\nstart of program---!')


def backup2zip(source_dir, destination_dir=f'{os.getcwd()+os.path.sep+"backed_up_files"}'):
    """
    backup2zip - backs up source directory to destination directoy

    """
    pass

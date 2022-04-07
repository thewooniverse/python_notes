#! python3
"""
backup2zip.py - a python script that receives a 
usable from anywhere :)

"""
import os
import sys
import zipfile
import re
import logging

# basic configurations
directories = ["error_logs", "backed_up_files", "test_files"]
for directory in directories:
    try:
        os.makedirs(os.getcwd()+os.path.sep+directory)
    except FileExistsError:
        pass

basename = os.path.basename(__file__).split('.')[0]
logging.basicConfig(level=logging.DEBUG,
                    filename=f"{os.getcwd()+os.path.sep}error_logs{os.path.sep+basename}.txt", format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug(f'\nstart of program---!')


def backup2zip(source_dir=os.getcwd(), destination_dir=f'{os.getcwd()+os.path.sep+"backed_up_files"}'):
    """
    backup2zip - backs up source directory to destination directoy as a zipfile. returns none.
    """
    source_basename = source_dir.split(os.path.sep)[-1]
    # check the destination directory for any files with the same syntax created by the script
    destination_files = os.listdir(destination_dir)
    versions = [0]
    version_regex = re.compile(r'_V([0-9][0-9]|[0-9])')
    for file in destination_files:
        if (version_regex.search(file)) and (re.search(source_basename, file)):
            versions += version_regex.findall(file)
            logging.debug(version_regex.findall(file))
        else:
            pass

    # get new correct version number based on existing versions and create zipfile
    logging.debug(versions)
    logging.debug(str(sorted([int(i) for i in versions])))
    current_zip_ver = str(sorted([int(i) for i in versions])[-1] + 1)
    new_zip = zipfile.ZipFile(
        f'{destination_dir+os.path.sep+source_basename}_V{current_zip_ver}.zip', 'w')
    logging.debug(current_zip_ver)
    # zip each file in source directory into the zipfile

    for file in os.listdir(source_dir):
        new_zip.write(source_dir + os.path.sep + file,
                      compress_type=zipfile.ZIP_DEFLATED)
    new_zip.close()
    return


test_dir = os.getcwd() + os.path.sep + "test_files"
backup2zip(test_dir)

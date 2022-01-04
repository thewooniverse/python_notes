#! usr/bin/python
# clr_bin.py - clears bin based on extension logic or by filesize as well.
# usage
# python clrbin.py all -- deletes all
# python clrbin.py size 1234 -- deletes all files that has a size larger than defined size in bytes


import os, sys, shutil, re, logging
from pathlib import Path
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')


# get the trash directory
trash_dir = os.path.join(str(Path.home()), '.Trash' + os.path.sep)
trash_list = os.listdir(trash_dir)
trash_dict = {}


# get more information about the trash directory;
for trash in trash_list:
    trash_path = os.path.join(trash_dir + trash)
    trash_size = os.path.getsize(trash_path)

    if os.path.isdir(trash_path):
        for dirpath, subdir, filenames in os.walk(trash_path):
            for file in filenames:
                fp = os.path.join(dirpath, file)

                if not os.path.islink(fp):
                    trash_size += os.path.getsize(fp)

    # print(trash_path +"  Size: " + str(trash_size))
    trash_dict[trash] = trash_size


def check_if_sure():
    print("This will permanently delete this file, are you totally completely sure?:\n")


def clear_bin(execution_type, file_size=0, file_type=None):
    print("Clearing bin..." + execution_type)
    print(f"Clearing all files and directories above {file_size} bytes.")


    for trash in trash_dict.keys():
        trash_size = trash_dict.get(trash)
        logging.debug(f'size of {trash} is {trash_size}')
        trash_path = os.path.join(trash_dir + trash)

        if trash_size >= file_size:

            if os.path.isdir(trash_path):
                logging.info(f'I\'m finna delete this dir {trash}')
                shutil.rmtree(trash_path)



            elif not os.path.isdir(trash_path):
                logging.info(f'I\'m finna delete this file {trash}')
                os.unlink(trash_path)

print(sys.argv[1])
print(len(sys.argv))






if sys.argv[1] == "all":
    clear_bin(sys.argv[1], 0)

elif sys.argv[1] == "size":
    clear_bin(sys.argv[1], int(sys.argv[2]))

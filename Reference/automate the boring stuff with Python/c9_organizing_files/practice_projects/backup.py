#! /usr/bin/python
# backup.py - copies an entire folder called and its conents into a zip file whose filename increments if there are previous versions.




import zipfile, os, shutil


def backup_to_zip(folder):

    folder = os.path.abspath(folder)

    # figure out what code this file should use based on what files already exist.
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number = number + 1

    # create zip file
    print(f'Creating {zip_file_name}')
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')


    # walk entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}')

        # add the current folder to the zip file
        backup_zip.write(foldername)

        # add all the files in this folder to the ZIP file
        for filename in filenames:
            new_base = os.path.basename(folder) + "_"
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue #don't back up zipfiles.
            backup_zip.write(os.path.join(foldername, filename))


    backup_zip.close()




# backup_to_zip(os.path.abspath('../../../../')) # calls the function on relative path






import os
import shutil

source = input("Enter source directory to take backup : - ")
destination = input("Enter destination directory to copy files into : - ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)

for file in list_of_files:
    shutil.copy(source+file,destination)
import os
import shutil

# name of the directory to be sorted C:\ninitha\python
path = input("Enter the name of the directory to be sorted : - ")

# Get the list of files in the directory
list_of_files = os.listdir(path)

for file in list_of_files:
    # get the name and extension of file seperately
    name, ext = os.path.splitext(file)
    # temporary variable to store extensions 1: means tuple range
    ext = ext[1:]

# if ext is empty, it means its a directory which has to be skipped to avoid error
    if ext == '':
        continue
    
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

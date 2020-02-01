import os
import sys
import shutil
import re

def size_sort(files, reverse):
    file_size = {}
    for file in files:
        size = os.path.getsize(file)
        file_size[file] = size
        if (not reverse):
            file_size = {k:v for k,v in sorted(file_size.items(), key=lambda item:item[1])}
        else: file_size = {k:v for k,v in sorted(file_size.items(), key=lambda item:item[1], reverse=True)}
    files = [file for file in file_size]

    return files

def sort(args):
    if(args.include): 
        files = [file for file in os.listdir(args.directory)]
    else: files = [file for file in os.listdir(args.directory) if os.path.isfile(args.directory+file)]
    if (args.sort):
        if (args.sort == 'd'):
            files.sort(key = os.path.getmtime)
        elif (args.sort == 'n'):
            files.sort()
        elif (args.sort == 's'):
            files = size_sort(files, False)
        elif (args.sort == 'rd'):
            files.sort(key = os.path.getmtime, reverse = True)
        elif (args.sort == 'rn'):
            files.sort(reverse = True)
        elif (args.sort == 'rs'):
            files = size_sort(files, True) 
    if (args.number):
        del files[len(files)-args.number:]

    return files
    
def rename(args, files):
    for idx,file in list(enumerate(files, start = 1)):
        ext = os.path.splitext(file)[1]
        os.rename(args.directory+file, args.directory+args.name+str(idx)+ext)
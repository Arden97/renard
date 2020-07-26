import os
import sys
import click

# Sort files by size
def size_sort(files, reverse):
    file_size = {}
    for file in files:
        size = os.path.getsize(file)
        file_size[file] = size
        if (not reverse):
            file_size = {k:v for k,v in sorted(file_size.items(), key=lambda item:item[1])}
        else: file_size = {k:v for k,v in sorted(file_size.items(), key=lambda item:item[1], reverse=True)}
    return list(file for file in file_size.keys())

# Sort files based on arguments passed
def sort_files(name, dir, num, inc, sort):
    if(inc): 
        files = [file for file in os.listdir(dir)]
    else:
        files = [file for file in os.listdir(dir) if os.path.isfile('{}{}'.format(dir, file))]
    
    if (sort):
        if (sort == 'date'):
            files.sort(key = os.path.getmtime)
        elif (sort == 'name'):
            files.sort()
        elif (sort == 'size'):
            files = size_sort(files, False)
        elif (sort == 'rdate'):
            files.sort(key = os.path.getmtime, reverse = True)
        elif (sort == 'rname'):
            files.sort(reverse = True)
        elif (sort == 'rsize'):
            files = size_sort(files, True) 
    if (num):
        del files[len(files)-num:]

    return files

def rename(files, dir, name):
    for idx,file in list(enumerate(files, start = 1)):
        ext = os.path.splitext(file)[1]
        os.rename('{}{}'.format(dir, file), '{}{}{}{}'.format(dir,name,idx,ext))
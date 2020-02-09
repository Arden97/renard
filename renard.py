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
    files = [file for file in file_size]
    
    return files

# Sort files based on arguments passed
def sort(name, dir, num, inc, sort):
    if(inc): 
        files = [file for file in os.listdir(dir)]
    else:
        files = [file for file in os.listdir(dir) if os.path.isfile(dir+file)]
    
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
        os.rename(dir+file, dir+name+str(idx)+ext)

# Arguments and options
# TODO: add feature to sort and rename files in subfolders as well
@click.command()
@click.argument('name')
@click.option('--dir', default=os.getcwd(), help = 'Directory, which contains files')
@click.option('--num', type = int, help = 'Number of files to rename  [default: all]')
@click.option('--inc', is_flag=True, help = 'Include subfolders in renaming process')
@click.option('--sort', type=click.Choice(['date', 'name', 'size', 'rdate', 'rname', 'rsize']),
                default = 'name', help = 'Sorting order', show_default=True)
def main(name, dir, num, inc, sort):
    """
    Rename files in the directory, using naming conventions.
    """
    files = sort(name, dir, num, inc, sort)
    rename(files, dir, name)



if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter
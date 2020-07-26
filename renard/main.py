from .utils import *

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
    files = sort_files(name, dir, num, inc, sort)
    rename(files, dir, name)


if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter

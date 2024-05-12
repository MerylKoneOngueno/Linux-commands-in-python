import os
import sys
import stat
import pwd
import grp
from datetime import datetime

'''
 script that imitates the ls, ls -a and ls -al commands. 
 You can run this by going to the directory where this file is located at.
 Then you type: python ls.py into the command line 
 add optionals such as -l or -a if necessary
'''
def list_files(directory='.', long_format=False, show_hidden=False):
    printed = False # temporary solution that allows me to print . and ..
    # check if the "directory" that is being passed is in fact a directory or a file within the cwd
    if os.path.isfile(directory) and not long_format: # if it is the filename is being printed and the method is left
        print(directory)
        return
    if os.path.isfile(directory) and long_format: # if the user opts for the long version
        file_stat = os.stat(directory)
        long_format22(file_stat, os.getcwd())
        return

    files_and_dirs = os.listdir(directory)
    files_and_dirs.sort()


    for item in files_and_dirs: # iterating over all the items(files and directories) within the given directory
        item_path = os.path.join(directory, item)

        if not show_hidden and item.startswith('.'): # no -a
            continue
        if show_hidden and item.startswith('.') and not printed:#-a yes
            print(".")
            print("..")
            printed = True
        file_stat = os.stat(item_path)
        if long_format:
         long_format22(file_stat, item)
        else:
            print(item)


def long_format22(file_stat, item): # function that prints the information needed for th elong format
        mode = file_stat.st_mode
        nlink = file_stat.st_nlink
        uid = file_stat.st_uid
        gid = file_stat.st_gid
        size = file_stat.st_size
        mtime = datetime.fromtimestamp(file_stat.st_mtime).strftime('%b %d %H:%M')
        permissions = _get_permissions(mode)
        owner = pwd.getpwuid(uid).pw_name
        group = grp.getgrgid(gid).gr_name
        print(f"{permissions} {nlink} {owner} {group} {size} {mtime} {item}")


def _get_permissions(mode): # function that gets me the permissions for the -l option
    permissions = [
        stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR,
        stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP,
        stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH
    ]
    mode_str = ['-'] * 10
    for i, perm in enumerate(permissions):
        if mode & perm:
            mode_str[i] = 'rwx'[i % 3]
    if mode & stat.S_ISUID:
        mode_str[2] = 's' if mode & stat.S_IXUSR else 'S'
    if mode & stat.S_ISGID:
        mode_str[5] = 's' if mode & stat.S_IXGRP else 'S'
    if mode & stat.S_ISVTX:
        mode_str[8] = 't' if mode & stat.S_IXOTH else 'T'
    return ''.join(mode_str)


if __name__ == "__main__":
    options = sys.argv[1:]

    # checks if ls.py is being applied on a specefic directory
    if not options:
        directory = '.'  # If no arguments are provided, list files in the current directory
    else:
        if options[-1].startswith('-'):
            directory = '.'  # Use current directory if the last argument is an option
        else:
            directory = options.pop()  # Otherwise, use the last argument as the directory


    if '-l' in options:
        long_format = True
    #    options.remove('-l')
    else:
        long_format = False

    if '-a' in options:
        show_hidden = True
      #  options.remove('-a')
    else:
        show_hidden = False
    if '-al' in options or '-la' in options: #user is also able to use -la or -al if they need both options
        show_hidden = True
        long_format = True

    list_files(directory, long_format, show_hidden)

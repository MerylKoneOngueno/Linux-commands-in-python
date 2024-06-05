// erstellt am 11.05.2024
import os
import sys
import argparse
import fnmatch
from datetime import datetime, timedelta

'''
 script that imitates the find command in linux.
 Optional arguments such as -mtime -int and -name -pattern are possible
 The directory that find is being applied on is adjustable 
 How to run this code: 
    go to the directory where this file is located at and 
    type: python find.py pathname optionals in the command line
    
    examples: 
                python find.py .
                python find.py . -mtime -14
                python find.py /home/meryl/Pictures -mtime -14
                python find.py /home/meryl/Pictures -name
                python find.py /home/meryl/Pictures -name '*nana*'
                
'''

def pmatch(pattern, file, name_pattern, mtime, filepath): # checks the pattern and mtime among other things
    pattern_match = (((not pattern or fnmatch.fnmatch(file, pattern))
                       and (not name_pattern or fnmatch.fnmatch(file, name_pattern))
                       and (mtime is None or check_mtime(filepath, mtime))))
    return pattern_match
def find_files(directory, pattern='', name_pattern='', mtime=None):
    found_files = []
    for root, dirs, files in os.walk(directory):#iterate through the files in the given directory
        for file in files:
            filepath = os.path.join(root, file) # path of a file is created
            if pmatch(pattern, file, name_pattern, mtime, filepath):
                found_files.append(filepath) # found_files gets fed
    return found_files

def check_mtime(filepath, mtime): # mtime optional
    current_time = datetime.now()
    mtime_threshold = current_time - timedelta(days=abs(mtime)) # subtracts the given number of days with the current date
    file_mtime = datetime.fromtimestamp(os.path.getmtime(filepath)) # gets last modification date of a file

    if mtime >= 0: # if the number is positive
        result = file_mtime <= mtime_threshold
    else:
        result = file_mtime >= mtime_threshold

    return result

def main():
    #defining the arguments
    parser = argparse.ArgumentParser(description="Imitate the find command in Linux")
    parser.add_argument("directory", nargs='?', default='.', help="Directory to search in (default: current directory)")
    parser.add_argument("-name", help="File name pattern to search for")
    parser.add_argument("-mtime", type=int, help="Find files modified less than n*24 hours ago")
    args = parser.parse_args()

    if args.directory == '.':
        args.directory = os.getcwd() #this might be redundant because the directory default is '.'

    found_files = find_files(args.directory, '', args.name, args.mtime)

    if found_files:
     print("Found files:")
     if args.mtime is not None:
        print(args.directory)
     for file in found_files:
            print(file)
    else:
        print("No files found.")

if __name__ == "__main__":
    main()

'''
possible adjustments:
    if find is applied on the cwd: instead of printing the entire path
    i could print ./filename or ./directoryname instead 
'''

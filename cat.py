// erstellt am 27.04.2024
import sys

'''
script that imitates the cat.py command in linux
cat prints out the contents of a given file
'''
def cat(filename):
    try:
        with open(filename, 'r') as file: # file is opened
            contents = file.read() # contents are being read and printed in the following line
            print(contents)
    except FileNotFoundError: # exception handling
        print(f"Error: File '{filename}' not found")


# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 2:
        print("Usage: python script_name.py filename")
    else:
       command = sys.argv[1]
       args    = sys.argv[2:]
       filename = sys.argv[len(sys.argv)-1]
       cat (filename)

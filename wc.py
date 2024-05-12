import sys
'''
script that imitates the wc, wc -l, wc -w and wc -c command in linux. 
Further variations such as -lw -wc etc. are possible as well.
You can run this by going to the directory where this file is located at and 
typing: python wc.py in the command line 
'''

def wc(filename, options):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            line_count = len(contents.splitlines())
            word_count = len(contents.split())
            char_count = len(contents)

            if 'l' in options:
                print(f"Lines: {line_count}")
            if 'w' in options:
                print(f"Words: {word_count}")
            if 'c' in options:
                print(f"Characters: {char_count}")
            if len(sys.argv) ==2:
                print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 2:
        print("Usage: python script_name.py -<options> filename")
    else:
        options = sys.argv[1][1:]  # Get the options excluding the hyphen
        filename = sys.argv[len(sys.argv)-1]
        wc(filename, options)

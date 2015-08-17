"""
Malware Remover

Usage:  In Terminal, cd to the folder with this script.
For each text file of malware paths, run the following command:

    python malremove.py <malwareList.txt

Where malwareList.txt is replaced by the name of the text file.
Do this in order of the numbered text files, and reboot your machine between
each call, unless the program returns NO MALWARE FOUND.

When done, open Safari and Chrome and remove all extensions you aren't sure
you need.
"""

import os
import sys
import shutil
import glob

FOUND_MALWARE = 0

def main():
    malpaths = get_malwares()
    for path in malpaths:
        process_path(path)

    printsummary()

# printsummary:  instructs user to remove extensions from web browser
def printsummary():
    sys.stdout.write("\nMalware removal complete.\n\nSUMMARY:\n")
    global FOUND_MALWARE
    if not FOUND_MALWARE:
        sys.stdout.write("NO MALWARE FOUND\n")
    else:
        if FOUND_MALWARE == 1:
            print "Found 1 instance of malware."
        else:
            print "Found", FOUND_MALWARE, "instances of malware."            

# process_path:  expands wildcards and regular expressions, searches and removes files
def process_path(path):
    path = os.path.expanduser(path)
    if '*' in path or '[' in path or '?' in path:
        # expand regular expression
        for p in glob.glob(path):
            search_remove(p)
    else:
        search_remove(path)

# search_remove:  searches for and removes a pre-processed path
def search_remove(path):
    print "Looking for %s..." % path
    global FOUND_MALWARE
    if os.path.exists(path):
        os.remove(path)
        FOUND_MALWARE += 1
        print "Found and removed %s" % path
    else:
        print "Did not find %s" % path

# get_malwares:  processes malware paths in chunks, reboot between
def get_malwares():
    malwares = []
    for line in sys.stdin:
        malwares.append(line.translate(None, '\n'))
    return malwares

if __name__ == '__main__':
    main()

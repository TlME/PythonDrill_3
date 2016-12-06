## Drill 3
# Traverses a given directory and finds recently (last 24 hours) modified .txt files
# then moves them to a target folder without preserving file-structure.
# by Nick Henegar

import os
import shutil
import time

def traverse(src, dst, currentTime):
    children = os.listdir(src)
    while children != []:
        for child in children:
            recently_modified = ((currentTime - os.stat(src + child).st_mtime) <= 86400) 
            if child.endswith(".txt") and recently_modified:
                shutil.move(src + child, dst)
            else:
                traverse(src + child + "\\", dst, currentTime)
            
def main():
    src = 'H:\\Python27\\Python stuff\\Python Drills\\PythonDrill_3\\Folder A\\'
    dst = 'H:\\Python27\\Python stuff\\Python Drills\\PythonDrill_3\\Folder B\\'
    currentTime = time.time()
    traverse(src, dst, currentTime)
    print("File transfer operation complete.")

if __name__ == "__main__": main()

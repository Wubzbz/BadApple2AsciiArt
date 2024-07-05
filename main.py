import os
from vidread import vidOpen, vidCvrt
from makefilm import EXPORT_PATH
from playfilm import readf
from savefilm import savef

ORIGINAL_PATH = 'BadApple.mp4'

vc = vidOpen(ORIGINAL_PATH)
assert os.path.exists(ORIGINAL_PATH)

def init(func):
    #check if file already existed.
    #if not, generate one
    if not os.path.exists(EXPORT_PATH):
        vidCvrt(vc)
    func()

if __name__ == "__main__":
    
    key = input("Read(r) or Save(s): ")
    if key == 'r' or key == 'R':
        init(readf)
    elif key == 's' or  key == 'S':
        init(savef)
    else:
        exit()
    

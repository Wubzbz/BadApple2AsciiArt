from vidread import vidOpen, vidCvrt
from playfilm import readf
from savefilm import savef

vc = vidOpen('BadApple.mp4')

def init(func):
    #check if file already existed.
    result = func()
    
    #if not, generate one
    if result == -1:
        vidCvrt(vc)
        func()

if __name__ == "__main__":
    
    key = input("Read(r) or Save(s)")
    if key == 'r' or key == 'R':
        init(readf)
    elif key == 's' or  key == 'S':
        init(savef)
    else:
        exit()
    

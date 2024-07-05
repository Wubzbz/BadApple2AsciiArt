import time
from makefilm import SCREEN_Y, EXPORT_PATH, FRAME_TIME


def readf(filepath = EXPORT_PATH):
   
    with open(filepath, 'r') as fin:
        #line number
        lnum = 1

        for line in fin:
            
            print(line.strip('\n'))            
            
            if lnum % SCREEN_Y == 0:
                time.sleep(FRAME_TIME)
                lnum = 0
            lnum += 1
        fin.close()

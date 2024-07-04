import time
import numpy as np
from math import floor

#the ascii .txt file
EXPORT_PATH = "FILM.txt"

#the frame pictures folder
FRAME_PATH = "FRAMES"

#one frame lasts in second
FRAME_TIME = 3

#screen size: 148*40(16:9)
SCREEN_X = 148
SCREEN_Y = 40

#grayscale: 6 groups, 0-black 255-white;
#0, 50, 100, 150, 200, 250;
#0, 1,  2,   3,   4,   5;
NUM_STEP = 50
NUM_SCALE = 255//NUM_STEP + 1

CHAR = [[' '], #0
        ['.', ',', '`', '\'', '_', ':', ' '], #1
        ['"', 'x', ';', '~', '-', '^', 'z'], #2
        ['6', '+', '*', 'r', 'v', '=', '5'], #3
        ['b', 'q', 'p', 'g', 'h', 'G', '9'], #4
        ['@', '#', '&', '0', '8', 'B', '$']] #5


def mesh(width, height):
    #Check frame size
    if width<SCREEN_X or height<SCREEN_Y:
        raise ValueError(f"Video size too small. Must be no less than {SCREEN_X}*{SCREEN_Y}.")
    
    #size of grid
    deltax = floor(width//SCREEN_X)
    deltay = floor(height//SCREEN_Y)
    print(f"dx:{deltax};dy:{deltay}.")

    #Bleeding
    leftmargin = floor((width % SCREEN_X)/2)
    topmargin = floor((height % SCREEN_Y)/2)
    print(f"lm:{leftmargin};tm:{topmargin}.")

    return (deltax, deltay, leftmargin, topmargin)


#calcutate the average grayscale of certain area
def mean(array):
        return int(np.average(array)//NUM_STEP)


#select the represent value of certain area
def represent(array):
    count = np.zeros(NUM_SCALE, int)
    index = -1
    maxi = 0
    for x in array:
        for y in x:
            count[y//NUM_STEP] += 1
    for i in range(NUM_SCALE):
        if count[i]>maxi:
            index, maxi = i, count[i]
    return index

#mapping grayscale with characters
def charmap(scale):
    return np.random.choice(CHAR[scale])

def prtfile(frame, dx, dy, lm, tm, sample_mode = 0):
    
    area = np.full((dy, dx), -1, int)

    with open(EXPORT_PATH, 'a') as fout:
        #go through the grid
        for iy in range(SCREEN_Y):
            
            line = ''
            for ix in range(SCREEN_X):
                
                #coordinates of each grid
                xstart = lm + ix * dx
                ystart = tm + iy * dy

                #copy sample to array area
                for pcy in range(ystart, ystart + dy):
                    for pcx in range(xstart, xstart + dx):
                        area[pcy-ystart][pcx-xstart] = frame[pcy][pcx]
                
                #calculate grayscale group
                if sample_mode == 0:
                    scale = mean(area)
                else:
                    scale = represent(area)
                line += charmap(scale)
            fout.write(line + '\n')
        fout.close()


if __name__ == "__main__":
    #test gray scale
    import cv2
    timg = cv2.imread(r"GrayGradient.jpg", cv2.IMREAD_GRAYSCALE)
    st = time.time()
    dx, dy, lm, tm = mesh(474, 395)
    prtfile(timg, dx, dy, lm, tm)
    ed = time.time()
    print(f"time:{ed-st}")
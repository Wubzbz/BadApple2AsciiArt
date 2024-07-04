import cv2, os
from makefilm import FRAME_PATH

VIDEO_PATH = f"{FRAME_PATH}\VID\VIDEO.mp4"

def vidwrite():
    fnum = 1
    fpath = f"{FRAME_PATH}\\frame{fnum}.png"
    
    if not os.path.exists(fpath):
        raise FileNotFoundError(f"Frame lost: {fpath}")

    fsize = cv2.imread(fpath).shape[1::-1]
    print(f"Frame size: {fsize}")

    #four character code
    fcc = cv2.VideoWriter.fourcc(*'mp4v')
    wrt = cv2.VideoWriter(VIDEO_PATH, fcc, 23.98, fsize)

    while True:
        if not os.path.exists(fpath):
            wrt.release()
            print(f"Write ended at frame{fnum-1}.")
            return
        
        print(f"Writing frame{fnum}...")
        wrt.write(cv2.imread(fpath))
        #update frame number and path
        fnum += 1
        fpath = f"{FRAME_PATH}\\frame{fnum}.png"

if __name__ == "__main__":
    vidwrite()
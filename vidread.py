import cv2
from makefilm import mesh, prtfile


def vidOpen(path):
    #Open video file
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open {path}")
    return cap
    

def vidCvrt(vcap):

    dx, dy, lm, tm = mesh(vcap.get(cv2.CAP_PROP_FRAME_WIDTH), vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fnum = 1

    #read frame by frame from vcap
    while True:
        ret, frame = vcap.read()
        
        if not ret:
            print(f"Retrieve ended at frame{fnum-1}.")
            break
        #convert color from BGR to grayscale    
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        prtfile(grayframe, dx, dy, lm, tm)
        print(f"Reading frame{fnum}...")
        fnum += 1
        #press q to end the process    
        if cv2.waitKey(0) == ord('q'):
            break

    vcap.release()
    cv2.destroyAllWindows()
from cv2 import cv2
import time
import random

def take_snapshot():
    #initialize cv2
    camera_port = 0
    #cv2.CAP_DSHOW adding this, removes the warning that occurs saying anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback
    #CAP_DSHOW means direct show via VideoInput - esp Windows. Can also ignore warning.
    videoCaptureObject = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
    result = True
    while (result):
        #read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        print(ret)
        #cv2.imwrite is used to save the image to any storage device
        cv2.imwrite("NewPicture.jpg", frame)
        result = False
        #release the camera
        videoCaptureObject.release()
        # close all the window that might be opened during this process
        cv2.destroyAllWindows()


take_snapshot()
print(time.time())
print(random.randint(1,9))

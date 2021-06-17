from cv2 import cv2
import dropbox
import time
import random


start_time = time.time()

def take_snapshot():
    number = random.randint(1, 100)
    camera_port = 0
    videoCaptureObject = cv2.VideoCapture(camera_port)
    result = True
    while (result):
        global start_time
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False

    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

    return img_name
    

def upload_file(img_name):
    access_token = 'RMhIr6mpqAsAAAAAAAAAAU1xEN2pYOsUaX394pObJzM-tOo3HMfSJdzUVW4mJoWA'
    file_from = img_name
    file_to = "/newfolder1/" + img_name
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while (True):
        print(time.time()-start_time)
        if ((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)


main()



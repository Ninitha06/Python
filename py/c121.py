import cv2
import time
import numpy as np


# *'mp4v'  - for mp4
fourcc = cv2.VideoWriter_fourcc(*'XVID')

output_file = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cap = cv2.VideoCapture(0)

time.sleep(2)
bg=0

for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg,axis=1)
keyPressed = False

while(cap.isOpened()):
    ret, img = cap.read()
    #to break the infinite loop
    if not ret:
        break

    #Flip an array horizontally (axis=1).

    img = np.flip(img,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # https://pysource.com/2019/02/15/detecting-colors-hsv-color-space-opencv-with-python/

    # https://data-flair.training/blogs/invisible-cloak-opencv-python/

    # lower_green = np.array([50, 80, 20])     
    # upper_green = np.array([90, 255, 255])

    # mask_1 = cv2.inRange(hsv,lower_green,upper_green)

    # low_blue = np.array([94, 80, 20])
    # high_blue = np.array([126, 255, 255])
    # mask_1 = cv2.inRange(hsv, low_blue, high_blue)

  
   
    # waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)

    lower_red = np.array([0,80,20])
    upper_red = np.array([10,255,255])
    # Mask Red regions
    mask_1 = cv2.inRange(hsv,lower_red,upper_red)

    lower_red = np.array([160,80,20])
    upper_red = np.array([179,255,255])
    mask_2 = cv2.inRange(hsv,lower_red,upper_red)

    mask_1 = mask_1 + mask_2

    #Open and expand the image where there is mask 1 (color)
    
    # Using Morphological Transformations to remove noise from the cloth and unnecessary Details.
    mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8),iterations=1)

    # In cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
    mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((10,10),np.uint8))

    mask_2 = cv2.bitwise_not(mask_1)

    #Selecting only the part that does not have mask one and saving in mask 2
   

    res_1 = cv2.bitwise_and(img,img,mask=mask_2)


    res_2 = cv2.bitwise_and(bg,bg,mask=mask_1)

# blend images by passing alpha,beta and gamma values.. alpha =1, beta=1,gama = 0 here
    final_output = cv2.addWeighted(res_1,1,res_2,1,0)
    output_file.write(final_output)

    # #Apply background to the masked region
    # cloak = cv2.bitwise_and(bg, bg, mask=mask_1)

    # inverse_mask = cv2.bitwise_not(mask_1) 
    # current_background = cv2.bitwise_and(img, img, mask=inverse_mask)

    # combined = cv2.add(cloak, current_background)

    # combined = filter_mask(combined)

    cv2.imshow("Test", final_output)
#     1.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).

# 2.waitKey(1) will display a frame for 1 ms, after which display will be automatically closed. Since the OS has a minimum time between switching threads, the function will not wait exactly 1 ms, it will wait at least 1 ms, depending on what else is running on your computer at that time.

# So, if you use waitKey(0) you see a still image until you actually press something while for waitKey(1) the function will show a frame for at least 1 ms only.
    
    k = cv2.waitKey(1)
    # 27 IS THE CODE FOR ESC key
    if k==27:
        break

   
cap.release()
output_file.release()

# closing all open windows
cv2.destroyAllWindows()

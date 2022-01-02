import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps
import os,ssl,time   

# if(not os.environ.get('PYTHONHTTPSVERIFY','') and getattr(ssl,'_create_unverified_context',None)):
#     ssl._create_default_https_context=ssl._create_unverified_context

# X,y = fetch_openml('mnist_784',version=1,return_X_y=True)

df = pd.read_csv("./csv/mnist_784_mine.csv")
y = df["class"].tolist()
df.drop("class",axis=1)
# X = df.to_numpy()


# print(pd.Series(y).value_counts())
print("Done Reading")

X = df.iloc[:, 0:784]
X = X.to_numpy()

# print(X[0])
# print(len(X))
# print(len(y))
# total pixels in each image
# print(len(X[0]))
# print(y)
classes = ['0','1','2','3','4','5','6','7','8','9']
nclasses = len(classes)

#Splitting the data and scaling it
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=9, train_size=7500,test_size=2500)
#scaling the features
X_train_scaled = X_train/255.0
X_test_scaled = X_test/255.0


#Fitting the training data into the model
clf = LogisticRegression(solver='saga', multi_class='multinomial').fit(X_train_scaled, y_train)
#Calculating the accuracy of the model
y_pred = clf.predict(X_test_scaled)
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

# Using external cam - 0 works for me
cap = cv2.VideoCapture(0)
print(cap.isOpened())

while(cap.isOpened()):
  # Capture frame-by-framecls
  try:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    height, width = gray.shape
    # Decide the co-ordinates for detection
    upper_left = (int(width/2-56),int(height/2-56))
    bottom_right = (int(width/2+56),int(height/2+56))

    # (image,start point, end point,color, thickness)
    cv2.rectangle(gray,upper_left,bottom_right,(0,255,0),2)

    roi=gray[upper_left[1]:bottom_right[1],upper_left[0]:bottom_right[0]]

    # PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.

    img_pil = Image.fromarray(roi)

  # convert to grayscale image - 'L' format means each pixel is represented by a single value from 0 to 255
#   L : This image mode has one channel that can take any value between 0 and 255 representing white, black and all the shades of gray in between. 
# It’s an 8-bit grayscale image mode. 
# L stands for Luminance channel.
    img_bw = img_pil.convert('L')

# In digital signal processing, spatial anti-aliasing is a technique for minimizing the distortion artifacts known as aliasing when representing a high-resolution image at a lower resolution. 
# Anti-aliasing is used in digital photography, computer graphics, digital audio, and many other applications.
    img_bw_resized = img_bw.resize((28,28),Image.ANTIALIAS)

    img_bw_resized_inverted = PIL.ImageOps.invert(img_bw_resized)

    pixel_filter = 20

    min_pixel = np.percentile(img_bw_resized_inverted,pixel_filter)

    # change to 0- 255 range
    img_bw_resized_inverted_scaled = np.clip(img_bw_resized_inverted-min_pixel,0,255)

    max_pixel=np.max(img_bw_resized_inverted)

    # Similar to scaling - dividing by 255 to represent as 0 and 1

    img_bw_resized_inverted_scaled = np.asarray(img_bw_resized_inverted_scaled/max_pixel)

    test_sample = np.array(img_bw_resized_inverted_scaled).reshape(1,784)

    test_pred = clf.predict(test_sample)

    print("Predicted class is: ", test_pred)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #   break

    k = cv2.waitKey(1)
    # 27 IS THE CODE FOR ESC key
    if k==27:
        break


  except Exception as e:
    pass

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()













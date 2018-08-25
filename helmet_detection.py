import cv2
import numpy as np
cap=cv2.VideoCapture('ketki2.mp4')
i=0
minArea=1
kernel = np.ones((3,3),np.uint8)
frame2=cv2.imread('frame2.jpg')
while True:
    #ret, frame = cap.read()
    #fgmask = fgbg.apply(frame)
    ret,frame1=cap.read()
    for i in range(97,182):
        filename = './test_images/image' +  str(int(i)) + ".jpg";
        frame2=cv2.imread(filename)
        d=cv2.absdiff(frame1,frame2)
    median=cv2.GaussianBlur(d, (111,121), 0)
    #median = cv2.medianBlur(d,11)
    im1 = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
    ret3,th = cv2.threshold(im1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.line(frame1,(0,283),(640,283),5)
    cv2.line(frame1,(0,290),(640,290),5)
    #opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
    opening = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    im2, contours,hierarchy = cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame1, contours, -1, (0, 0, 255), 2)
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        if (w*h)>=26000:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            moments=cv2.moments(c)
            if (w*h)>=5000:
                x=int(moments['m10']/moments['m00'])
                y=int(moments['m01']/moments['m00'])
                
                if(h/w>1.5 and x>=165 and x<=170 and y>=283 and y<=290):
                    print("motorcycle")
                    cv2.circle(frame1,(x,y) ,1, (255,0,0),-1)
                    crop_img = frame1[y:y+(4*h),x:x-(4*w)]
                    cv2.imshow("helmetarea",crop_img)
                    
    cv2.imshow("Track", frame1)
    cv2.imshow("diff",d)
    key = cv2.waitKey(100)
    if key == ord('q'):
            break

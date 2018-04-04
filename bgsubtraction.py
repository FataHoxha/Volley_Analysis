#!/usr/bin/python3
import datetime

import numpy as np
import cv2
import ball



kernelOp = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
kernelCl = np.ones((3,3),np.uint8)
fgbg = cv2.createBackgroundSubtractorMOG2(500, 16, 0)

balls = []
max_p_age = 2
pid = 1
areaTH = 500
curr_frame=0


cap = cv2.VideoCapture('test720.mp4')
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
print( frame_rate, "frame rate" )

while(1):
    ret, frame = cap.read()

    #ROI for fixed1.mp4
    #frame2 = frame[220:670, 980:1100]

    frame2 = frame[15:570, 300:900]

    #Background Operation - opening and closing
    fgmask = fgbg.apply(frame2)
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernelOp)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernelCl)

    # Find blob contour
    ret, thresh_img = cv2.threshold(closing, 100, 255, cv2.THRESH_BINARY)
    contours = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]

    for c in contours:
        cv2.drawContours(frame2, [c], -1, (0, 255, 0), 3)

        area = cv2.contourArea(c)
        if area>areaTH:
        #add control on the area to disinguish from the noise if area > areaTH, areaTH=300
            M = cv2.moments(c)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            x, y, w, h = cv2.boundingRect(c)
            cv2.circle(frame2, (cx, cy), 2, (0, 0, 255), -1)
            img = cv2.rectangle(frame2, (x, y), (x + w, y + h), (0,255 , 0), 2)

            for i in balls:
                if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                    space_x = abs(x - i.getX())
                    space_y = abs(y - i.getY())
                    curr_frame = cap.get(cv2.CAP_PROP_POS_FRAMES);

                    delta_frame=abs(curr_frame-i.getFrame())
                    v_x=space_x/delta_frame
                    v_y = space_x /delta_frame
                    print("space x:",space_x,",", "velocity x:",v_x)
                    print("space y",space_y,",", "velocity y:",v_y)

                    curr_msec=cap.get(cv2.CAP_PROP_POS_MSEC)
                    print("curr frame", delta_frame)
                    print("curr prev Frame", curr_msec)

                    i.updateCoords(cx, cy,curr_frame)

            p = ball.VolleyBall(pid, cx, cy, max_p_age,curr_frame)
            balls.append(p)

            for i in balls:
                if len(i.getTracks()) >= 2:
                    pts = np.array(i.getTracks(), np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    frame = cv2.polylines(frame2, [pts], False, (255,0 , 0))
                #if i.getId() == 9:

                #cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)

    cv2.imshow('frame', frame2)
    cv2.imshow('frameBG',closing)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
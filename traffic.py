import cv2

import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    size = hsv_frame.size

  ##################################################################################
    # Red color

    RED_MIN = np.array([0, 0, 128], np.uint8)

    RED_MAX = np.array([250, 250, 255], np.uint8)

    dstr1 = cv2.inRange(frame, RED_MIN, RED_MAX)

    no_red = cv2.countNonZero(dstr1)

    frac_red = np.divide((float(no_red)), (float(size)))

    percent_red = np.multiply((float(frac_red)), 100)

    #print('red: ' + str(percent_red) + '%')


    ##########################################################################

    #green color

    green_MIN = np.array([32, 161, 70], np.uint8)

    green_MAX = np.array([250, 250, 255], np.uint8)

    dstr2 = cv2.inRange(frame, green_MIN, green_MAX)

    no_green = cv2.countNonZero(dstr2)

    frac_green = np.divide((float(no_green)), (float(size)))

    percent_green = np.multiply((float(frac_green)), 100)

    #print('green: ' + str(percent_green) + '%')



#######################################################################################

    #yellow color

    yellow_MIN = np.array([72, 204, 236], np.uint8)

    yellow_MAX = np.array([250, 250, 255], np.uint8)

    dstr3 = cv2.inRange(frame, yellow_MIN, yellow_MAX)

    no_yellow = cv2.countNonZero(dstr3)

    frac_yellow = np.divide((float(no_yellow)), (float(size)))

    percent_yellow = np.multiply((float(frac_yellow)), 100)

   # print('yellow: ' + str(percent_yellow) + '%')

    #####################################################################################

    if percent_green >= 3 and percent_green <= 20:
            print('color is green')


    if percent_red > 20 and percent_red < 30:
        print('color is red')

    if percent_yellow >= 0 and percent_yellow <= 2:
        print('color is yellow')

    #####################################################################################

    cv2.imshow("Frame", frame)


    key = cv2.waitKey(1)
    if key == 27:
        break
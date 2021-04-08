import os
import time
import sys
import cv2
import numpy as np
from PIL import Image
from pymouse import PyMouse

import mark_rc
import mediapipe as mp
from activity import motion
from mark_rc import Calulate as cal
from test_tool import test_tool



mp_hands = mp.solutions.hands

#转换数据格式
def get_float(s):
    return (float(s.split(':')[-1]))
def regularization(mark_list):
    xyz_ = []
    for i, m in enumerate(mark_list):
        x = round(get_float(m[0]) , 4)
        y = round(get_float(m[1]) , 4)
        z = round(get_float(m[2]) , 4)
        xyz_.append([x,y,z])
    return (xyz_)

def take_mask_msg(results):
    s = str(results.multi_handedness[0])
    s = s.replace(' ','').split('\n')[1:4]

    marks = str(results.multi_hand_landmarks[0])
    marks = marks.replace(' ','').replace('\n',' ').split('landmark')
    marks.pop(0)
    mark_list=[]
    for i in marks:
        mark_list.append(i.split(' ')[1:6])
    xyz_ = regularization(mark_list)
    return(s, xyz_)
    
# For webcam input:
Hand = cal()
hands = mp_hands.Hands(
    min_detection_confidence=0.6, 
    min_tracking_confidence=0.6,
    max_num_hands=1,)

ip = '192.168.123.41:8081'
#cap = cv2.VideoCapture(f"http://admin:admin@{ip}/video")
cap = cv2.VideoCapture(0)
print('ok~')

t = test_tool()
try:

    fps = 66
    while cap.isOpened():
        
        success, image = cap.read()

    # 约为0.01
        time.sleep(1/fps)

        if not success:
            break

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        if results.multi_hand_landmarks:
            
            _, mark_list = take_mask_msg(results)

            x,y,z = (mark_list[8])
            p_y =  mark_list[0][1]
            t.getdata([x, y, z, p_y])

            Hand.get_info(mark_list)
            Hand.next_()


                #m.move(l/4+round(l*x)/2,h/4+round(h*y)/2)



        else :
            pass
except :

    print(sys.exc_info())
    hands.close()
    cap.release()
    t.show()


hands.close()
cap.release()



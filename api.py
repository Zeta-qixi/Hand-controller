import os
import time
import sys
import cv2
import numpy as np
from PIL import Image

import mark_rc
import mediapipe as mp
from activity import motion
from mark_rc import Cal_feature as cal_f



#转换数据格式
def get_float(s):
    return (float(s.split(':')[-1]))
def regularization(mark_list):
    xyz_ = []
    for i, m in enumerate(mark_list):
        x = round(get_float(m[0]) , 5)
        y = round(get_float(m[1]) , 5)
        z = round(get_float(m[2]) , 5)
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
    
class CAP:
    def __init__(self):

        self.cap = None
        mp_hands = mp.solutions.hands
        self.hands = mp_hands.Hands(
            min_detection_confidence=0.6, 
            min_tracking_confidence=0.6,
            max_num_hands=1,)


    def ipcap(self, ip):
        self.cap = cv2.VideoCapture(f"http://admin:admin@{ip}/video")

    def over(self):
        self.hands.close()
        self.cap.release()

    def start(self, fps = 60):
        if not self.cap:
           self.cap = cv2.VideoCapture(0)
           
        while self.cap.isOpened():
            success, image = self.cap.read()
            time.sleep(1/fps)

            if not success:
                break

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = self.hands.process(image)

            if results.multi_hand_landmarks:
                
                _, mark_list = take_mask_msg(results)
                yield mark_list

            else :
                yield None
 

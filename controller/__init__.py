from .c1 import win_controller


import os
import random
from time import sleep
import numpy as np


def is_static(xy:list):
    '''
    计算标准差
    '''
    D = np.array(xy).T
    x = np.std(D[0],ddof=1)
    y = np.std(D[1],ddof=1)
    if x < 0.01 and y < 0.03:
        return True
    return False

def static_l2(a, b):
    '''
    l2长度
    '''
    if ((a[0] - b[0])**2 + (a[1] - b[1])**2) > 0.00003:
        return True
    return False

class controller:

    def __init__(self):
        self.is_press = 0
        self.click_times = 0
        self.xy = [0,0]
        self.C = win_controller()

    def get(self, marks:list, pose_list :list):
        '''
        marks : 最近5个时间序列的 食指关节xyz坐标list
        pose : 动作
        '''
        
        pose = set(pose_list) 
        print(pose)

        if pose == {'none'}:
            pass        

        elif pose == {'p'}:
            self.C.press(marks[-1])

        elif pose == {2}:
            self.C.scroll(marks)
            
        elif pose == {5}:
            if self.is_press == 1:
                self.is_press = 0
                self.C.release(marks[-1])

        elif pose == {0}:
            pass

        elif pose == {1}:
            if static_l2(self.xy, marks[-1]):
                self.C.move(marks[-1])
                self.C.click_times = 0

            self.click_times += 1
            
            if self.click_times >= 30:
                self.click_times = 0
                self.C.click(marks[-1])

        self.xy = marks[-1]
        
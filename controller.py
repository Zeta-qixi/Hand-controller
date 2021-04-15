'''
光标控制器
'''

import os
import random
from time import sleep
import numpy as np
from pymouse import PyMouse
import asyncio
m = PyMouse()
w,h = m.screen_size()

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

        self.click_times = 0
        self.xy = [0,0]

    def get(self, marks:list, pose :list):
        '''
        marks : 最近5个时间序列的 食指关节xyz坐标list
        pose : 动作
        '''
        if pose == 2:
            self.scroll(marks[0])
        elif pose == 0:
            pass

        else:

            if static_l2(self.xy, marks[0]):
                self.move(marks[0])
                self.click_times = 0

            self.click_times += 1
            

            if self.click_times >= 30:
                self.click_times = 0
                self.click(self.xy)
        self.xy = marks[0]


    def move(self,xy:list):
        
            m.move(xy[0]*w,xy[1]*h)
        


    def click(self, xy:list):
        m.click(xy[0]*w,xy[1]*h)
        

    def scroll(self, xy:list):
        x,y = m.position()
        sleep(0.1)
        if(self.xy[1]-xy[1] > 0):
            m.scroll(1)
        else:
            m.scroll(-1)
        sleep (1)
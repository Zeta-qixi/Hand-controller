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

def static_1(a, b):
    '''
    l2长度
    '''
    
    if ((a[0] - b[0])**2 + (a[1] - b[1])**2) > 0.00003:
        
        return True
    return False

class controller:

    def __init__(self):

        self.onclick = 0
        self.xy = [0,0]
    def get(self, marks:list):
        
        if static_1(self.xy,marks[0]):
            self.move(marks[0])
            self.onclick = 0

        self.onclick += 1
        self.xy = marks[0]

        if self.onclick >= 30:
            self.onclick = 0
            self.click(self.xy)
        #self.click(marks)

    def move(self,xy:list):
        
            m.move(xy[0]*w,xy[1]*h)
        


    def click(self, xy:list):
        m.click(xy[0]*w,xy[1]*h)
        

    def scroll(self):
        x,y = m.position()
        m.click(x,y)
        sleep(0.1) 
        m.scroll(1)
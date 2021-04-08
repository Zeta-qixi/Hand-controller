'''
计算动作 
'''
from math import fabs
class Pose:
    def __init__(self):
        self.pose = None   #改变时向web传递数据

        self.stop_times = 0 #静止times 可以用于渲染html
        self.stop_plot = [0, 0, 0]
        


    def hand_pose(self, figs:list):
  
        if figs == [0, 1, 0, 0 ,0]:
            return 1
        elif figs == [0, 1, 1, 0, 0]:
            return 2
        elif figs == [1, 1, 1, 1, 1]:
            return 5
        elif figs == [0, 0, 0, 0, 0]:
            return 0
        else:
            return figs


    def is_move(self, now):
        pre = self.stop_plot
        self.stop_plot = now
        if fabs(pre[0]-now[0]) < 0.015 and fabs(pre[1]-now[1]< 0.02):
            self.stop_times +=1
            if self.stop_times >= 60: #60帧下 1秒
                self.stop_times = 0
                return 'click'
            return 'stop'
        else :
            self.stop_times = 0
            return 'move'

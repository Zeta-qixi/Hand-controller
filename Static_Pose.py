'''
计算动作 
'''
from math import fabs
class Pose:
    def __init__(self):
        self.pose_list = []

        self.stop_times = 0 #静止times 可以用于渲染html
        self._plot = [0, 0, 0] #x,y,z
        


    def hand_pose(self, figs:list):
  
        if figs == [0, 1, 0, 0 ,0]:
            self.pose_list.append(1)
        elif figs == [0, 1, 1, 0, 0]:
            self.pose_list.append(2)
        elif figs == [1, 1, 1, 1, 1]:
            self.pose_list.append(5)
        elif figs == [0, 0, 0, 0, 0]:
            self.pose_list.append(0)
        else:
            self.pose_list.append('none')


    def is_move(self, now):
        pre = self._plot
        self._plot = now
        if fabs(pre[0]-now[0]) < 0.015 and fabs(pre[1]-now[1]< 0.02):
            self.stop_times +=1
            if self.stop_times >= 60: #60帧下 1秒
                self.stop_times = 0
                return 'click'
            return 'stop'
        else :
            self.stop_times = 0
            return 'move'

'''
[21][3]
只用 x y
'''
import math
import time
from time import sleep
from Pose import Pose
from pymouse import PyMouse
m = PyMouse()
l,h =m.screen_size()
class Calulate:

    def __init__(self):
        
        self.Pose = Pose()
        self.angles_ = []
        self.press = 0

    def get_info(self, hm:list):
        '''
        提取手势信息
        '''
        self.plam = hm[0]
        self.figs = []
        for i in range(5):
            n = i*4
            self.figs.append(hm[n+1:n+5])

        self.status = self.get_hand_pose()
        #print(self.angles_)
        print(self.status)

    def next_(self):
        '''
        动作  点 取食指x 手掌y+一个值 #食指y与手掌y距离 触发点击事件
        '''
        nx,ny = m.position()
        xyz = self.figs[1][-1]
        pose = self.Pose.hand_pose(self.status)
        action = self.Pose.is_move(xyz)
        #print(pose)


            #---------长按 换 中指-------------#
        # if self.press == 1:
        #     xyz = self.figs[2][-1] 
        x = round(l*xyz[0])
        y = round(l*xyz[1])
        #y = round(h*(self.plam[1]-0.3))
    
        #移动
        if pose == 1:
            
            
            m.move(x ,y)
            # if action =='move':
            #     times = 500
            #     dx = (x - nx)/times
            #     dy = (y - ny)/times           
            #     for i in range(times):
            #         time.sleep(0.1/times)
            #         m.move(i*dx + nx, ny + i*dy)
            #点击
            if action == 'click':
                print('click')
                m.click(nx, ny)
        if pose == 2:
            if self.press == 0:
                #print('press')
                m.press(nx,ny)
                self.press = 1
                sleep(0.3)
        if pose == 5:
            if self.press ==1:
                m.release(nx,ny)
                self.press = 0
                #print('release')


                
        # elif pose == 2:
        #     if self.press == 0 :
        #         self.press = 1
        #         print('press')
        #     m.press(x,y)
        # elif pose == 0:
        #     m.release(nx,ny)
        #     if self.press == 1:
        #         self.press = 0
        #         print('res')
        


    def get_hand_pose(self):
        '''
        返回五指状态信息
        '''
        figs = self.figs
        self.angles_ = []
        for f in figs:
            fig = (self.cal_figs(f))
            self.angles_.append(self.cal_angle(fig))
        pose_ = (self.isopen(self.angles_))
        
        return pose_
        
    def isopen(self, angles:list)->list:
        open = []
        '''
        计算手指状态判定
            判定一个角度 :弯曲 / 竖直
        '''
        #拇指
        if angles[0][0] < 25:
            open.append(1)
        else:
            open.append(0)

        #食指
        for a in angles[1:]:
            if a[0] < 80:
                open.append(1)
            else:
                open.append(0)

        return(open)

    def cal_figs(self, mark:list)->list:
        '''
        计算手指关节向量

            input:一根根手指的4个节点数据 单个数据代表相对手掌的xyz位置信息
            output:每一节的向量信息 ->list

            -- 目前用这两个 所构成的角度 辨识度最高 <30 ; >120  拇指 <50 >80
        '''
        V =[]
        V.append(self.vec_(mark[1], self.plam[:2]))
        V.append(self.vec_(mark[3], mark[1]))
        return V



    def cal_angle(self, vecs:list)->list:
        '''
        计算向量角度
            input: 两个向量值 -->cal_fig()的返回值
            output:每个关节的角度 
        '''
        angle_ = []
        for i in range(len(vecs)-1):
            angle_.append(self.one_angle( vecs[i], vecs[i+1]))

        return (angle_)


    def vec_(self, a:float, b:float) -> list :
        '''
        向量计算模块
            input:传入两个点 
            output:返回向量 [x,y]
        '''
        x = round((a[0] - b[0])*100, 2)
        y = round((a[1] -b[1])*100, 2) 
        return([x, y])

    def one_angle(self, x1:float, x2:float) -> float : 
        '''
        角度计算模块
            input:两个向量  
            output: cos(a)
        '''
        xx = x1[0] * x2[0] + x1[1] * x2[1]
        l1 = (math.sqrt(x1[0] ** 2 + x1[1] ** 2)) 
        l2 = (math.sqrt(x2[0] ** 2 + x2[1] ** 2)) 

        return round(math.acos(xx/(l1*l2))/math.pi * 180, 2)

            

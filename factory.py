'''
加工数据的
'''
import math
import time
from time import sleep

'''
[21][3]
只用 x y
'''

def hand_pose(figs:list):

    if figs == [0, 1, 0, 0 ,0]:
        return 1
    elif figs == [0, 1, 1, 0, 0]:
        return 2
    elif figs == [1, 1, 1, 1, 1]:
        return 5
    elif figs == [0, 0, 0, 0, 0]:
        return 0
    else:
        return 'none'
class factory:

    def __init__(self): 
        pass

    def make_(self, hm:list):
        '''
        获取手势数据
        '''
        self.plam = hm[0]
        self.figs = []
        for i in range(5):
            n = i*4
            self.figs.append(hm[n+1:n+5])

        return hand_pose(self.cal_pose())
        #print(self.angles_)


    def cal_pose(self)->list:
        '''
        retuern: 五指状态信息 (二元数组) 
        '''
        figs = self.figs
        self.angles_ = []
        for f in figs:
            fig = (self.cal_figs(f))
            self.angles_.append(self.cal_angle(fig))
        pose_ = (self.isopen(self.angles_))
        
        return pose_ 
        
    def isopen(self, angles:list)->list:
        '''
        计算手指状态判定
        retuern: 0/1 (弯曲 / 竖直)
        '''
        open = []
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

            input: 一根根手指的4个节点数据 单个数据代表相对手掌的xyz位置信息
            return: 每一节的向量信息 ->list

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

            

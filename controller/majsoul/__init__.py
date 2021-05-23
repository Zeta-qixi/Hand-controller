from pymouse import PyMouse
m = PyMouse()
w,h = m.screen_size()
print(m.position())

'''
全屏下
--13张牌 
    长度 313 - 1926  单张牌宽度 124
    高度 1233

--11张牌 
    长度 312 - 1677

--听牌示意 
 (2498, 1217)

--立直 & 跳过
(1361, 1115) (1740, 1115)

-- 理\和\鸣\切
 50 [680 770 860 950]
'''

def move(x):
    for i in range(14):
        '''
        将 [0.2,0.8] 映射为牌的位置
        牌的位置 251 + i * 124
        '''
        if x < 0.2 + (i*0.6/14):
            break
    m.move(251 + 124*i ,1250)
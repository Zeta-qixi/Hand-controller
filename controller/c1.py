from pymouse import PyMouse
m = PyMouse()
w,h = m.screen_size()

class base_controller:
    def __init__(self):
        pass

    def move(self,xy:list):
        '''
        移动
        '''
        m.move(xy[0]*w,xy[1]*h)
        
    def click(self, xy:list):
        '''
       点击
        '''
        m.click(xy[0]*w,xy[1]*h)
        
    def scroll(self, marks:list):
        '''
        滚动
        '''
        d = marks[0][1] - marks[-1][1]
        R = 0.2
        print(d)
        if d > R:
            m.scroll(-1)
        elif d < -R:
            m.scroll(1)

    def press(self, xy:list, ones = True):
        '''
        长按
        '''
        if ones:
            m.press(xy[0]*w,xy[1]*h)
        else:
            m.drag(xy[0]*w,xy[1]*h)

    def release(self, xy:list):
        '''
        松开
        '''
        m.release(xy[0]*w,xy[1]*h)


class mac_controller(base_controller):
    def __init__(self):
        super(mac_controller, self).__init__()

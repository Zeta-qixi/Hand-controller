from pymouse import PyMouse
m = PyMouse()
w,h = m.screen_size()

class controller:
    def __init__(self):
        pass

    def move(self,xy:list):
            m.move(xy[0]*w,xy[1]*h)
        
    def click(self, xy:list):
        m.click(xy[0]*w,xy[1]*h)
        

    def scroll(self, marks:list):
        d = marks[0][1] - marks[-1][1]
        R = 0.2
        print(d)
        if d > R:
            m.scroll(-1)
        elif d < -R:
            m.scroll(1)
     

    def press(self, xy:list):
        if self.is_press ==0:
            m.press(xy[0]*w,xy[1]*h)
            self.is_press = 1
        else:
            m.drag(xy[0]*w,xy[1]*h)

    def release(self, xy:list):
        m.release(xy[0]*w,xy[1]*h)
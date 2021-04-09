import matplotlib.pyplot as plt
import numpy as np


class test_tool:
    def __init__(self):
        self.data = []



    def getdata(self, d):
        self.data.append(d)

    
    def draw_tabel(self):
        D = np.array(self.data).T

        plt.figure(21)
        x = range(0, len(D[0])- 10) 
        y1 = D[1][10:]

        y2 = D[0][10:]
        plt.plot(x, y1, 'r.-',label = 'Y')

        plt.plot(x, y2, 'b.-',label = 'X')
        #plt.plot(y2, y1, 'b.-',label = 'traic')
        plt.legend(loc='best', fontsize=10)
        plt.title("vertical")
        #plt.title(f'X: {min(self.data_x)} - {max(self.data_x)}\nY: {min(self.data_y)} - {max(self.data_y)}')
        #print(np.max(D[3] - D[1]) - np.min(D[3] - D[1]))
        print('-------------')
        
        print('x:'+ str(np.max(D[0]) - np.min(D[0])))
        print(np.max(D[1]) - np.min(D[1]))
        plt.show()

    def show(self):
        self.draw_tabel()

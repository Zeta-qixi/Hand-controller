import os
import random
import time
class controller:

    def __init__(self):
        self.z = 0
        self.onclick = 0

    def frist(self, mark):
        self.z = mark

    def click(self, z):
        #print(z)
        if (self.z == 0 or self.onclick == 1):
            self.z = z
            self.onclick = 0
            
        if self.z - z > 0.1 and self.onclick == 0:
            self.onclick = 1
            print ('click')
            time.sleep(1)

        return ('')
from cap_api import cap_api
from factory import factory
from controller import controller
from filter import *
from draw_tool import draw_tool
import asyncio
dt = draw_tool()
con = controller()
ft = factory()
cap = cap_api()
import time
#cap.ipcap('192.168.123.243:8081')

try:
    list = []
    x=y=z=0
    for i in cap.start():
        if i:
            list.append (i[8])
        
            if len(list)>=10:
            
                con.get(list[-5:])
                list.pop(0)
            dt.add_data(i[8])
        
        else:
            list.append([x,y,z])
            list.pop()
            dt.add_data([0,0,0])
    cap.over()
except:
    cap.over()
    dt.show()

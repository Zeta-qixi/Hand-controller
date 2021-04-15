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

# try:
fig_list = []
pose_list = []
x=y=z=0
for i in cap.start():
    if i:
        fig_list.append (i[8])
        pose_list.append(ft.make_(i))
    
    else:
        pose_list.append([0])
        fig_list.append([0,0,0])

    if len(fig_list)>=10:
        con.get(fig_list[-5:], pose_list[-5:])
        
        fig_list.pop(0)
        pose_list.pop(0)
        dt.add_data(fig_list[-1])

        

cap.over()
# except:
#     cap.over()
#     dt.show()


from api import CAP

cap = CAP()
for i in cap.start():
    if i:
        x,y,z = i[8]
        print(x,y)
cap.over()
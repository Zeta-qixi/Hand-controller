import cap_api

cap = cap_api()
for i in cap.start():
    if i:
        x,y,z = i[8]
        print(x,y)
cap.over()
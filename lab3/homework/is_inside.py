def is_inside(x,y):
    check=0
    if(y[0]+y[2])>=x[0]>=y[0] and (y[1]+y[3])>=x[1]>=y[1]:
        check=1
    else:
        check=0
    return check

    
check=is_inside([200, 120], [140, 60, 100, 200])
if check==1:
    print("Your function is correct")
else:
    print("Oops, there's a bug")

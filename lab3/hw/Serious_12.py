def is_inside(rectangle_1,rectangle_2):
    x1 = rectangle_1[0]
    y1 = rectangle_1[1]

    x2 = rectangle_2[0]
    y2 = rectangle_2[1]
    width = rectangle_2[2]
    height = rectangle_2[3]

    rec = True
    if x1 >= x2 and x1 <= x2+width and y1 >= y2 and y1 <= y2+height:
        rec = True
    else:
        rec = False
    return rec


rectangle_1 = [200, 120]
rectangle_2 = [140, 60, 100, 200]
check = is_inside(rectangle_1,rectangle_2)
if check == True:
    print("Your function is correct")
else:
    print("Oops, there's a bug")
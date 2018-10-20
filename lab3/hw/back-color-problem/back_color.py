from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def is_inside(rectangle_1=[],rectangle_2=[]):
    x1 = rectangle_1[0]
    y1 = rectangle_1[1]
    x2 = rectangle_2[0]
    y2 = rectangle_2[1]
    width = rectangle_2[2]
    length = rectangle_2[3]
    rec = True
    if x1 >= x2 and x1 <= x2 + width and y1 >= y2 and y1 <=y2+length:
        rec = True
    else:
        rec = False
    return(rec)

def get_shapes():
    return shapes


def generate_quiz():
    
    text = choice(shapes)["text"]
    color = choice(shapes)["color"]

    return [
                text,
                color,
                randint(0,1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    check = True
    for i in shapes:
        if quiz_type == 0: #meaning
            if text == "blue":
                if is_inside([x,y],i["rect"]) == True:  #[x,y] là vị trí click vào , 
                                                        # i["rect"] : là vị trí của button và chiều dài chiều rộng của câu hỏi
                    check = True
                else:
                    check = False
            if text == "red":
                if is_inside([x,y],i["rect"]) == True:
                    check = True
                else:
                    check = False
            if text == "yellow":
                if is_inside([x,y],i["rect"]) == True:
                    check = True
                else:
                    check = False
            if text == "green":
                if is_inside([x,y],i["rect"]) == True:
                    check = True
                else:
                    check = False
        
        if quiz_type == 1: #color
            if color == "#3F51B5":
                if is_inside([x,y],i["rect"]) == True:
                    check = True
                else:
                    check = False
            if color == "#C62828":
                if is_inside([x,y],i["rect"]) == True:
                    check = True
                else:
                    check = False
            if color == "#FFD600":
                if is_inside([x,y],i["rect"]) == True:
                    check = True
                else:
                    check = False
            if color == "#4CAF50":
                if is_inside([x,y],i["rect"]) == True:
                    check = True
                else:
                    check = False
    return check
    
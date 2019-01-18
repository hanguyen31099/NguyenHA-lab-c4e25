from random import choice,randint
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

def is_inside(x,y):
    if(y[0]+y[2])>=x[0]>=y[0] and (y[1]+y[3])>=x[1]>=y[1]:
        return True
    else:
        return False

def get_shapes():
    return shapes


def generate_quiz():
    color =choice(shapes)
    list_color=[]
    for j in color:
        list_color.append(color[j])
    result=[]
    result.append(list_color[0].upper())
    result.append(list_color[1])
    result.append(randint(0,1))
    return result

def mouse_press(x, y, text, color, quiz_type):
    for  check in shapes:
        if quiz_type == 1:
            if check['text'].upper() == text:
                user_click = is_inside([x, y], check['rect'])
        else:
            if check['color'] == color:
                user_click = is_inside([x, y], check['rect'])
    return user_click
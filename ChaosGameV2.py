import turtle as t
import time as ti
import random
import Make_Linear_From_2_Points as lin

def circle(x,y,rad,color='white'):
    t.pencolor(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(rad)

def print_hex(dec):
    if dec >= 16:
        if dec > 255:
            return 'ff'
        else:
            return hex(dec)[2:]
    else:
        if dec < 0:
            return '00'
        else:
            return '0{}'.format(hex(dec)[2:])

#preset
t.bgcolor('black')
t.pencolor('white')
t.penup()
t.pensize(1)
t.speed('fastest')
t.hideturtle()
t.setup(700,700)

while True:
    # #Perfect triangle
    # start_points={1:[-t.window_width()/2 + 50,-t.window_height()/2 + 50],
    #             2:[t.window_width()/2 - 50,-t.window_height()/2 + 50],
    #             3:[0,260]}

    # Generating corners
    start_points={1:[random.randrange(round(-t.window_width()/2 + 50.5),round(t.window_width()/2 - 50.5)),
                     random.randrange(round(-t.window_height()/2 + 50),round(t.window_height()/2 - 50))],
                2:[random.randrange(round(-t.window_width()/2 + 50.5),round(t.window_width()/2 - 50.5)),
                   random.randrange(round(-t.window_height()/2 + 50),round(t.window_height()/2 - 50))],
                3:[random.randrange(round(-t.window_width()/2 + 50.5),round(t.window_width()/2 - 50.5)),
                   random.randrange(round(-t.window_height()/2 + 50),round(t.window_height()/2 - 50))]}

    cord = []
    cord.append([])
    cord.append([])

    cord[0].append(start_points[1][0])
    cord[1].append(start_points[1][1])

    cord[0].append(start_points[2][0])
    cord[1].append(start_points[2][1])

    cord[0].append(start_points[3][0])
    cord[1].append(start_points[3][1])

    # # Print corners
    # circle(cord[0][0], cord[1][0], 1)
    # circle(cord[0][1], cord[1][1], 1)
    # circle(cord[0][2], cord[1][2], 1)

    # Generate colors
    # # Default colors
    # colors = {0:'red', 1:'blue', 2:'green'}

    colors = {0:'#{}{}{}'.format(print_hex(random.randint(60, 255)), print_hex(random.randint(60, 220)), print_hex(random.randint(60, 220))),
              1:'#{}{}{}'.format(print_hex(random.randint(60, 220)), print_hex(random.randint(60, 255)), print_hex(random.randint(60, 220))),
              2:'#{}{}{}'.format(print_hex(random.randint(60, 220)), print_hex(random.randint(60, 220)), print_hex(random.randint(60, 255)))}


    # First point
    start_point = [((cord[0][0]+cord[0][1])/2+cord[0][2])/2, (((cord[1][0]+cord[1][1])/2+cord[1][2])/2)]

    x = start_point[0]
    y = start_point[1]

    for i in range(600):
        rand = random.randint(0, 2)
        x = (cord[0][rand] + x)/2
        y = (cord[1][rand] + y) / 2
        circle(x, y, 0.5, colors[rand])
    ti.sleep(1)

    del start_points
    del start_point
    del cord
    t.clear()
# t.hideturtle()
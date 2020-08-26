import turtle as t
import time as ti
import random

def circle(x,y,rad):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(rad)


#preset
t.bgcolor('black')
t.pencolor('white')
t.penup()
t.pensize(1)
t.speed(20)

#Create basic cords
cord = []
cord.append([])
cord.append([])

cord[0].append((-t.window_width()/2) + 50)
cord[1].append((-t.window_height()/2) + 50)

cord[0].append((t.window_width()/2) - 50)
cord[1].append((-t.window_height()/2) + 50)

cord[0].append(0)
cord[1].append(260)

print(cord)
# Print main cords
circle(cord[0][0], cord[1][0], 1)
circle(cord[0][1], cord[1][1], 1)
circle(cord[0][2], cord[1][2], 1)


while True:
    # Start x y
    start_x = random.randint(-t.window_width() / 2 + 0.5, t.window_width() / 2 - 0.5)
    start_y = random.randint(-t.window_height() / 2, t.window_height() / 2)

    if start_y < -238 or start_y > 498/291.5*start_x + 260 or start_y > -498/291.5*start_x + 260:
        continue
    #     V1
    # circle(start_x, start_y, 1)

    #     V2
    t.penup()
    t.goto(start_x,start_y)

    rand = random.randint(0, 2)
    circle((cord[0][rand]+start_x)/2,(cord[1][rand]+start_y)/2,1)

ti.sleep(20)
# t.hideturtle()
import math
from vpython import *

side = 20.0
s2 = 2*side
wallB = box(pos=vector(0, -side, 0), size=vector(500, 0.3, 150),  color=color.blue)


def where_ball_at(start_x, start_y, time, velocity, angle, friction):
    angle = math.radians(angle)
    y_vel = velocity * math.sin(angle)
    if angle == math.radians(90):
        cos_angle = 0
    else:
        cos_angle = math.cos(angle)
    acc_x = -friction
    x_vel = velocity * cos_angle
    ball_y_pos = start_y + y_vel + (-5) * time * time
    ball_x_pos = start_x + x_vel * time + 0.5 * acc_x * time * time
    if ball_y_pos < 0:
        ball_y_pos = 0
    return ball_x_pos, ball_y_pos, x_vel, y_vel, acc_x


ball = sphere(color=color.green, radius=0.4, make_trail=True, retain=200)
ball.mass = 1.0
ball.pos = vector(0, 0, 0)


def simulate(start_x, start_y, end_time, velocity, angle, friction):
    t = 0
    dt = 0.01
    angle = math.radians(angle)
    yv = velocity * math.sin(angle)
    if angle == math.radians(90):
        cos_angle = 0
    else:
        cos_angle = math.cos(angle)
    acc_x = -friction
    xv = velocity * cos_angle
    vel = vector(xv, yv, 0)
    pos = vector(start_x, start_y, 0)
    ball.pos = pos
    while t < end_time or t == end_time:
        rate(200)
        vel.x = vel.x + acc_x * dt
        vel.y = vel.y + (-10 * dt)
        pos = ball.pos + vel * dt
        ball.pos = pos
        t = t + 0.01
        if ball.pos.y < -side:
            print("you hit the ground at: ", t, " seconds.")
            break
    print(where_ball_at(start_x, start_y, end_time, velocity, angle, friction))


simulate(start_x=-side, start_y=-side, end_time=10, velocity=40, angle=45, friction=0)


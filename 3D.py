import turtle
from turtle import *
import keyboard
from time import sleep
import tkinter as tk

#"übermittlungs" variablen
x = 0
y = 0
z = 0
#Mesh
Mesh = [8, 8, 4, 0, 8, 4, 0, 0, 4, 8, 0, 4, 8, 8, 4
, 8, 8, 6, 0, 8, 6, 0, 0, 6, 8, 0, 6, 8, 8, 6 ]
#Count
cx = -3
cy = -2
cz = -1
#Camera Coordinates
vx = 22
vy = 0
vz = 0
cs = 0.5
c = 0

fps = 0.0166666667
turtle.speed(1000000000)

#render
turtle.ht()
turtle.tracer(0, 0)
bgcolor("lightblue")
while True:
    x = (Mesh[cx + 3] - vx)
    y = (Mesh[cy + 3] - vy)
    z = (Mesh[cz + 3] - vz)
    py = (y / (z / 5)) * 25
    px = (x / (z / 5)) * 25
    goto(px, py)
    cx = cx + 3
    cy = cy + 3
    cz = cz + 3
    c = c + 1
    turtle.update()
    if c == 10:
        cx = -3
        cy = -2
        cz = -1
        c = 0
        turtle.update()
        #camera movement
        if keyboard.is_pressed('w'):
            vy = vy + cs
            turtle.clear()
        if keyboard.is_pressed('s'):
            vy = vy - cs
            turtle.clear()
        if keyboard.is_pressed('a'):
            vx = vx - cs
            turtle.clear()
        if keyboard.is_pressed('d'):
            vx = vx + cs
            turtle.clear()
        if keyboard.is_pressed('f'):
            vz = vz - cs
            turtle.clear()
        if keyboard.is_pressed('r'):
            if vz == 1:
                print(vz)
            else:
                
                vz = vz + cs
                turtle.clear()
        sleep(fps)
        
main.loop()

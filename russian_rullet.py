import turtle
import random
import math



def goto(x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	
def draw_cir(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def draw_pistol(x, y):
    PHI = 360 / 7
    R = 50
    goto(x, y)
    turtle.circle(80)
    goto(x, y+160)
    draw_cir(5, 'red')
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        goto(math.sin(phi_rad) * R+x, math.cos(phi_rad) * R+60+y)
        draw_cir(22, 'white')

	
def the_game(start, x, y):
    phi = 360 / 7
    r = 50
    for i in range(start, 7+random.randrange(0,7)):
        phi_rad = phi * i * math.pi / 180.0
        goto(math.sin(phi_rad) * r+x, math.cos(phi_rad) * r+60+y)
        draw_cir(22, 'brown')
        draw_cir(22, 'white')

    goto(math.sin(phi_rad) * r+x, math.cos(phi_rad) * r+60+y)
    draw_cir(22, 'brown')

    start = i % 7
    if start % 7 == 0:
        draw_cir(22, 'yellow')
        draw_cir(22, 'white')
        goto(-150, 200)
        turtle.write("Вы проиграли", font=("Arial", 20, "normal"))
    return start
	
def main():
    X=100
    Y=100	
    start = 0
    turtle.speed(0)
    draw_pistol(X, Y)	
    answer = ''
    while answer != 'n':
        answer = turtle.textinput("Поиграем?", "y/n")
        if answer == 'y':
            start=the_game(start, X, Y)
        else:
            pass
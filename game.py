import turtle as t
import os #linux-aplay, mac-afplay
#import winsound, winsound.PlaySound("file.wav", winsound.SND_ASYNC)
from tkinter import messagebox

win = t.Screen()
paddlea = t.Turtle()
paddleb = t.Turtle()
ball = t.Turtle()
pen = t.Turtle()
ball.dx = .05
ball.dy = -.05
scorea = 0
scoreb = 0

def draw():
    win.title("Pong V1.0")
    win.bgcolor("black")
    win.setup(width=900, height=700)
    win.tracer(0)
    messagebox.showinfo("Welcome to Pong", "Use 'w' and 's' to control the left paddle. Use up and down arrows to control right paddle.")

    paddlea.speed(0)
    paddlea.shape("square")
    paddlea.color("red")
    paddlea.shapesize(stretch_wid=5, stretch_len=1)
    paddlea.penup()
    paddlea.goto(-350, 0)

    paddleb.speed(0)
    paddleb.shape("square")
    paddleb.color("blue")
    paddleb.shapesize(stretch_wid=5, stretch_len=1)
    paddleb.penup()
    paddleb.goto(350, 0)

    ball.speed(0)
    ball.shape("square")
    ball.color("green")
    ball.penup()
    ball.goto(0, 0)

    pen.speed(0)
    pen.color("orange")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))

def paddlea_up():
    y = paddlea.ycor()
    y += 20
    paddlea.sety(y)

def paddlea_down():
    y = paddlea.ycor()
    y -= 20
    paddlea.sety(y)

def paddleb_up():
    y = paddleb.ycor()
    y += 20
    paddleb.sety(y)

def paddleb_down():
    y = paddleb.ycor()
    y -= 20
    paddleb.sety(y)

def update_score():
    pen.clear()
    pen.write(f"PlayerA: {scorea}  PlayerB: {scoreb}", align="center", font=("Courier", 24, "normal"))

draw()
t.listen()
t.onkey(paddlea_up, "w")
t.onkey(paddlea_down, "s")
t.onkey(paddleb_up, "Up")
t.onkey(paddleb_down, "Down")

while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay sndbounce.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay sndbounce.wav&")
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scorea += 1
        update_score()
        os.system("aplay sndscore.wav&")
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreb += 1
        update_score()
        os.system("aplay sndscore.wav&")

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleb.ycor() + 40 and ball.ycor() > paddleb.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay sndbounce.wav&")
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddlea.ycor() + 40 and ball.ycor() > paddlea.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay sndbounce.wav&")

import turtle

# This is the whole background setup of the game
from turtle import Turtle

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=700, height=600)
wn.tracer(0)

score_1 = 0
score_2 = 0

# The first paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('square')
paddle_1.color('red')
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-250, 0)

# The second paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('square')
paddle_2.color('red')
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(250, 0)

# The ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape('square')
ball.color('blue')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.09
ball.dy = -0.09

pen: Turtle = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))


# How the paddles move(y and x coordinates)
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard movement
wn.listen()
wn.onkeypress(paddle_1_up, 'w')
wn.onkeypress(paddle_1_down, 's')
wn.onkeypress(paddle_2_up, 'Up')
wn.onkeypress(paddle_2_down, 'Down')

# the actual game
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 340:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -340:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))

    # the bouncing part
    if (235 < ball.xcor() < 250) and (paddle_2.ycor() + 40 > ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(235)
        ball.dx *= -1

    if (-235 > ball.xcor() > -250) and (paddle_1.ycor() + 40 > ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-235)
        ball.dx *= -1
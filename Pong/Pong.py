# Simple Pong

from functools import partial
import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

# Score
score_Player_a = 0
score_Player_b = 0

def create_Paddle(startX, startY):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(startX, startY)
    return paddle

# Paddle A 
paddle_a = create_Paddle(-350,0)
# Paddle B
paddle_b = create_Paddle(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_up(paddle):
    y = paddle.ycor()
    y+= 20
    if y < 290:
        paddle.sety(y)
    if y > 290:
        paddle.sety(290)

    


def paddle_down(paddle):
    y = paddle.ycor()
    y -= 20

    if y > -290:
        paddle.sety(y)
    if y < -290:
        paddle.sety(-290)


#Keyboard binding
win.listen()
win.onkeypress(partial(paddle_up,paddle_a), "w")
win.onkeypress(partial(paddle_down,paddle_a), "s")
win.onkeypress(partial(paddle_up, paddle_b), "Up")
win.onkeypress(partial(paddle_down,paddle_b), "Down")


def UpdateScore():
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_Player_a, score_Player_b), align="center",font=("Courier", 24, "normal"))


#Main game loop
while True:
    win.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx * 0.05)
    ball.sety(ball.ycor() + ball.dy * 0.05)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_Player_a += 1
        UpdateScore()

    if ball.xcor() < -390:
        ball.setx(390)
        ball.dy *= -1
        score_Player_b += 1
        UpdateScore()

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
        
    if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        
        

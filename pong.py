import turtle, os

paddleSpeed = 30
ballSpeed = 0.05

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("red")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("blue")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ballSpeed
ball.dy = ballSpeed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write(f"Player: {scoreA}  PlayerB: {scoreB}", align="center", font=("Courier", 24, "normal"))

# Functions
def paddleAUp():
    y = paddleA.ycor()
    y += paddleSpeed
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= paddleSpeed
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y += paddleSpeed
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= paddleSpeed
    paddleB.sety(y)

# Keyboard biding
wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBUp, "o")
wn.onkeypress(paddleBDown, "l")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle border checking
    if (paddleA.ycor() + 50) > 300:
        paddleA.sety(250)

    if (paddleA.ycor() - 50) < -300:
        paddleA.sety(-250)

    if (paddleB.ycor() + 50) > 300:
        paddleB.sety(250)

    if (paddleB.ycor() - 50) < -300:
        paddleB.sety(-250)

    # Ball border checking
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy = -ball.dy
        os.system("aplay bounce.wav")

    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy = -ball.dy
        os.system("aplay bounce.wav")


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = -ball.dx
        ball.dy = -ball.dy
        scoreA +=1
        pen.clear()
        pen.write(f"Player: {scoreA}  PlayerB: {scoreB}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = -ball.dx
        ball.dy = -ball.dy
        scoreB +=1
        pen.clear()
        pen.write(f"Player: {scoreA}  PlayerB: {scoreB}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ball.xcor() < -330 and ((paddleA.ycor() - 50) <= ball.ycor() <= (paddleA.ycor() + 50)):
        ball.setx(-330)
        ball.dx = -ball.dx
        os.system("aplay bounce.wav&")

    if ball.xcor() > 330 and ((paddleB.ycor() - 50) <= ball.ycor() <= (paddleB.ycor() + 50)):
        ball.setx(330)
        ball.dx = -ball.dx
        os.system("aplay bounce.wav&")

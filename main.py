from tkinter import *
import turtle
import winsound

# background
w = turtle.Screen()
w.title("ping pong")
w.bgcolor("black")
w.setup(width=800, height=600)

# paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("red")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(360, 0)
# paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("blue")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(-360, 0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2
# score
score = turtle.Turtle()
score.speed(0)
score.color("yellow")
score.up()
score.hideturtle()
score.goto(-20, 150)
score.write("Player B: 0    Player A: 0", align="center", font=("Courier", 24, "normal"))
score_A = 0
score_B = 0


# functions
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)


def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)


def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


def alert_popup(message):
    root = Tk()
    root.title("End game")
    wn = 250     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    z = (sw - wn)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (wn, h, z, y))
    m = message
    m += '\n'
    wn = Label(root, text=m, width=100, height=10)
    wn.pack()
    winsound.PlaySound("mixkit-medieval-show-fanfare-announcement-226.wav", winsound.SND_ASYNC)
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    root.mainloop()


# keyboard actions
w.listen()
w.onkeypress(paddle_A_up, "Up")
w.onkeypress(paddle_A_down, "Down")
w.onkeypress(paddle_B_up, "w")
w.onkeypress(paddle_B_down, "s")

check = True  # to limit the time of the game

# main game loop
while True:

    if check:
        for x in range(2000):
            w.update()
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
            # check board
            if ball.xcor() > 390:
                # ball.setx(390)
                ball.dx *= -1
                ball.goto(0, 0)
                score_B += 1
                score.clear()
                winsound.PlaySound("mixkit-small-crowd-ovation-437.wav", winsound.SND_ASYNC)
                score.write("Player B: {}    Player A: {}".format(score_B, score_A),
                            align="center", font=("Courier", 24, "normal"))

            if ball.xcor() < -390:
                # ball.setx(-390)
                ball.dx *= -1
                ball.goto(0, 0)
                score_A += 1
                score.clear()
                winsound.PlaySound("mixkit-small-crowd-ovation-437.wav", winsound.SND_ASYNC)
                score.write("Player B: {}    Player A: {}".format(score_B, score_A),
                            align="center", font=("Courier", 24, "normal"))

            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            if (340 < ball.xcor() < 350) and (paddle_A.ycor() + 50 > ball.ycor() > paddle_A.ycor() - 50):
                ball.setx(340)
                ball.dx *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            if (-340 > ball.xcor() > -350) and (paddle_B.ycor() + 50 > ball.ycor() > paddle_B.ycor() - 50):
                ball.setx(-340)
                ball.dx *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    ball.goto(0, 0)
    check = False
    if score_A > score_B:
        alert_popup(" Player A is the Winner!")
    elif score_A < score_B:
        alert_popup(" Player B is the Winner!")
    else:
        alert_popup(" Players draw!")

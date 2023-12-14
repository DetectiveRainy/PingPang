



import turtle
import winsound



wn=turtle.Screen()
wn.title("PingPong by Su")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


# Score

score_a=0
score_b=0


#pen

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("Player A 0  Player B 0", align="center", font=("Courier", 24, "normal"))



#Paddle A

paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.shape("square")

#this is the speed of the anim speed
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.speed(0)  #this is the speed of the anim speed
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#ball
ball = turtle.Turtle()
ball.speed(0) #this is the speed of the anim speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#ball.shapesize(stretch_wid=1, stretch_len=1)
ball.dx=0.15
ball.dy=0.15


#Function

def paddle_a_up():
    y = paddle_a.ycor() #get paddle location
    y+=10   #modify y value
    paddle_a.sety(y) #set y value to paddle_a

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor() #get paddle location
    y+=10   #modify y value
    paddle_b.sety(y) #set y value to paddle_a

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)




# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")





# Main Game loop

while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #boarder Checking
    if ball.ycor()>290 :
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor()<-290 :
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)




    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b) ,align="center", font=("Courier", 24, "normal"))

    if ball.xcor()<-390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}". format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    #paddle and ball collisions

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50 ):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50 ):
        ball.setx(-340)
        ball.dx *= -1



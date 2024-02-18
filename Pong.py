#pong Game
import turtle
import winsound
wn = turtle.Screen()
wn.title("Pong game")
wn.bgpic('Jingliu.gif')

wn.setup(width = 800,height = 600)
wn.tracer(0)

#Score
score1 = 0
score2 = 0

#Paddle 1

paddle1 = turtle.Turtle()
paddle1.speed(0)
turtle.register_shape('wooden-baseball-bat-resize.gif')
paddle1.shape('wooden-baseball-bat-resize.gif')
#paddle1.color("black")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

#Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
turtle.register_shape('wooden-baseball-bat-resize.gif')
paddle2.shape('wooden-baseball-bat-resize.gif')
#paddle2.color("blue")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

#Ball


  
# registering the image
# as a new shape

 
# setting the image as cursor
ball = turtle.Turtle()
ball.speed(0)
# registering the image
turtle.register_shape('doge meme resize.gif')
# as a new shape
ball.shape('doge meme resize.gif')
#ball.shape("doge meme.gif")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

#Function
#Paddle 1 control
def paddle1_up():
    y = paddle1.ycor()
    y +=20
    paddle1.sety(y)
def paddle1_down():
    y = paddle1.ycor()
    y -=20
    paddle1.sety(y)
#Paddle 2 control
def paddle2_up():
    y = paddle2.ycor()
    y +=20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -=20
    paddle2.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle1_up,"w")
wn.onkeypress(paddle1_down,"s")
wn.onkeypress(paddle2_up,"Up")
wn.onkeypress(paddle2_down,"Down")

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align = "center",font=("Courier",24,"normal"))



#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
        

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
        

    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *=-1
        score1=score1+1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score2,score1),align = "center",font=("Courier",24,"normal"))
        winsound.PlaySound("bonk-sound-effect1.wav",winsound.SND_ASYNC)
        

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score2=score2+1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score2,score1),align = "center",font=("Courier",24,"normal"))
        winsound.PlaySound("bonk-sound-effect1.wav",winsound.SND_ASYNC)
    #Paddle and ball collision
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor() < paddle2.ycor()+40 and ball.ycor()>paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx*=-1 
        winsound.PlaySound("bonk-sound-effect1.wav",winsound.SND_ASYNC)
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor() < paddle1.ycor()+40 and ball.ycor()>paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bonk-sound-effect1.wav",winsound.SND_ASYNC)
         

    




import turtle
import time
import math
wn=turtle.Screen()
wn.setup(1800,850)
wn.bgpic('riv1.gif')
turtle.tracer(2)

# Images for boat
image1='boat_1.gif'
image2='boat_2.gif'
image3='boat_3.gif'

#Turtle for boat image1
t1=turtle.Turtle('turtle')
t1.penup()
t1.hideturtle()
wn.addshape(image1)
t1.shape(image1)
t1.setposition(-580,-310)
t1.showturtle()

# Upper shore line position
t2X=-450
t2Y=250
t2=turtle.Turtle('turtle')
t2.hideturtle()
t2.pensize(5)
t2.penup()
t2.goto(-t2X,t2Y)
t2.goto(t2X,t2Y)

# Turtle of letter B and position of letter B
t4=turtle.Turtle('turtle')
image4='B.gif'
wn.addshape(image4)
t4.shape(image4)
t4.hideturtle()
t4.penup()

#Turtle of sentence AB, positition (0,0)
t5=turtle.Turtle('turtle')
image5='AB.gif'
wn.addshape(image5)
t5.shape(image5)
t5.hideturtle()
t5.penup()
TEXT_FONT=('Arial', 20,'bold')

#Velocity (boat and stream) and position of the text
velocity=turtle.Turtle()
velocity.color('white')
velocity.hideturtle()
velocity.up()

#Text answer and position of the text
answer=turtle.Turtle()
answer.color('white')
answer.hideturtle()
answer.up()
image=[image1,image2,image3]
q=-1

# Function for main boat motion
def motion():
    X=-580
    Y=-310
    q=-1
    running=True
    while running:
        q=q+1
        q1=q%3
        X=X+deltaX
        Y=Y+deltaY
        wn.addshape(image[q1])
        t1.shape(image[q1])
        time.sleep(0.1)
        t1.setposition(X,Y)
        Xcor=t1.xcor()
        Ycor=t1.ycor()
        dist=abs(Ycor-t2Y)
        if dist<40:
            t1.hideturtle()
            t1.goto(-580,-310)
            t1.showturtle()
            t4.setposition(Xcor,Ycor+130)
            t4.showturtle()
            t5.showturtle()
            time1=100/deltaY
            AB_distance=time1*deltaX
            answer.setposition(400,-110)
            answer.write('my answer=',font=TEXT_FONT)
            answer.setposition(580,-110)
            #my_answer=input('answer=')
            my_answer=wn.textinput("Welcome to River Boat Problem!", \
                              "my answer?")
            answer.write(my_answer,font=TEXT_FONT)
            answer.setposition(400,-160)
            answer.write('real answer=',font=TEXT_FONT)
            answer.setposition(580,-160)
            answer.write(round(AB_distance),font=TEXT_FONT)
            time.sleep(3)
            print(AB_distance)
            running=False
            
while True:
    activation = wn.textinput("Welcome to River Boat Problem!", \
                              "Are you ready?")
    if activation=='no':
        print("Goodbye!")
        #wn.clear()
        wn.bye()
    else:
        deltaY= wn.textinput('Welcome to River Boat Problem!', \
                             'Boat velocity')
        deltaY=int(deltaY)
        velocity.setposition(400,0)
        velocity.write('boat velocity=',font=TEXT_FONT)
        velocity.setposition(600,0)
        velocity.write(deltaY,font=TEXT_FONT)

        deltaX= wn.textinput('Welcome to River Boat Problem!', \
                             'Stream velocity')
        deltaX=int(deltaX)
        velocity.setposition(400,-50)
        velocity.write('stream velocity=',font=TEXT_FONT)
        velocity.setposition(630,-50)
        velocity.write(deltaX,font=TEXT_FONT)
        motion()
        running=True
    velocity.clear()
    answer.clear()    


import turtle,time
wn=turtle.Screen()
wn.bgcolor('violet')
#turtle.tracer(3)
turtle.tracer(2)

t1=turtle.Turtle('circle')
t1.color('blue')
t1.hideturtle()
t1.up()

t2=turtle.Turtle('circle')
t2.color('gold')
t2.hideturtle()
t2.up()


t3=turtle.Turtle('arrow')
t3.hideturtle()
t3.up()
t3.color('blue')
t3.shapesize(0.5,4)

t4=turtle.Turtle('arrow')
t4.hideturtle()
t4.up()
t4.color('gold')
t4.shapesize(0.5,4)

t5=turtle.Turtle()
t5.hideturtle()
t5.up()
t5.goto(0,-200)
image='Equation.gif'
wn.addshape(image)
t5.shape(image)
t5.showturtle()

#--------------------------------------------------

#TEXT

TEXT_FONT=('Arial',15,'bold')
text_main=turtle.Turtle()
text_main.color('black')
text_main.hideturtle()
text_main.up()
text_main.setposition(-250,250)
text_main.write('ELASTIC COLLISION of TWO BALLS', font=('Arial',25,'bold'))
text_main.up()
text_main.setposition(-150,200)
text_main.write('m1-->blue, m2-->gold', font=('Arial',25,'bold'))

text_main.up()
text_main.setposition(-230,150)
text_main.write('before collision velocity for blue ball ->U1, \
for gold ball ->U2=0', font=('Arial',15,'bold'))

text_main.up()
text_main.setposition(-230,-120)
text_main.write('after collision velocity for blue ball ->V1,\
for gold ball ->V2', font=('Arial',15,'bold'))

#----------------------------------------------
def collision(size1,size2,angle1,angle2,speed1,speed2,speed3):
    text1=turtle.Turtle()
    text1.hideturtle()
    text1.color('ghostwhite')
    text1.up()
    text1.clear()
    text1.setposition(-150,80)
    if speed1==0:
        text1.write('Two balls with equal masses m1=m2',\
                    font=('Arial',15,'bold'))
    if speed1==-3:
        text1.write('Two balls of different mass, m1<m2',\
                    font=('Arial',15,'bold'))

    if speed2==2:
        text1.write('Two balls of different mass, m1>m2',\
                    font=('Arial',15,'bold'))
        
    t1.goto(-300,0)
    t1.shapesize(size1)
    t1.showturtle()
    
    t2.goto(0,0)
    t2.shapesize(size2)
    t2.showturtle()
    
    t3.setheading(angle1)
    t3.goto(-300,-50)
    t3.showturtle()
    time.sleep(0.5)

    for i in range(62):
        t1.fd(4)
        t3.fd(4)
        time.sleep(0.01)
    t3.hideturtle()
    t3.setheading(angle2)
    t3.goto(-40,-50)
    t3.showturtle()

    t4.goto(0,-50)
    t4.showturtle()

    for i in range(280):
        t1.fd(speed1)
        t3.fd(speed2)
        if speed1==0:
            t3.hideturtle()
        t2.fd(speed3)
        t4.fd(speed3)
        time.sleep(0.01)
        
    time.sleep(0.5)
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t4.hideturtle()
    text1.clear()

#-----------------------------------------------------------
    
while True:
    collision(2.5,2.5,0,0,0,0,4)
    collision(1.5,3.5,0,180,-3,3,2)
    collision(3.5,1.5,0,0,2,2,4)
    
    
    


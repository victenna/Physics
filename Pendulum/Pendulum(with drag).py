import turtle
import time
t1=turtle.Turtle()
wn=turtle.Screen()
wn.setup(800,900)
wn.bgcolor('gold')
t1.hideturtle()
turtle.tracer(2)

t2=turtle.Turtle('turtle')
t2.hideturtle()
t2.color('blue')

t4=turtle.Turtle('square')
t4.shapesize(2,5)
t4.color('red')

t5=turtle.Turtle()
t5.up()
t5.hideturtle()
t5.goto(-390,200)
#t5.showturtle()
t5.color('red')
t5.write('Drag a pendulum to any angle and then press space bar',\
         font=('Times New Roman',25,'bold'))

t2.penup()
t2.hideturtle()
t2.goto(0,0)
t2.begin_poly()
t2.fd(400)
t2.left(90)
t2.circle(30.358)

t2.fd(4)
t2.left(90)
t2.fd(400)
t2.end_poly()

wn.register_shape('pend',t2.get_poly())

t3=turtle.Turtle(shape='pend')
t3.up()
t3.color('blue')
t3.showturtle()

def motion():
    global teta
    i=-1
    q=-1
    t3.setheading(teta)
    #time.sleep(3)
    while True:
        if teta>0 and teta<90:
        #print(teta)
            i=i+1
            i1=i%(2*teta+1)
            if i1==2*teta:
                q=-1*q
            #print(t3.heading())    
            t3.left(q)
            time.sleep(0.02)

        if teta>300:
            teta1=360-teta
            print(teta1)
            i=i+1
            i1=i%(2*teta1+1)
            if i1==2*teta1:
                q=-1*q
            t3.right(q)
            time.sleep(0.02)

  
teta=0
def drag(x,y):
    #t3.ondrag(None)
    t3.setheading(0.2*x)
    global teta
    teta=t3.heading()
    teta=round(teta)
    
    #t3.ondrag(drag)
t3.ondrag(drag)

wn.onkey(motion,'space')
#print(q.heading())
wn.listen()  
print(teta)






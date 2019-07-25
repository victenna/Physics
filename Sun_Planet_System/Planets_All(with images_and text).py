import turtle
import random


wn=turtle.Screen()
wn.setup(1300,1300)
wn.bgpic('sky.gif')
wn.bgcolor('black')


wn.tracer(30)

TEXT_FONT=('Arial',15,'bold')
text_mercury=turtle.Turtle()
text_mercury.color('yellow')
text_mercury.hideturtle()
text_mercury.up()
text_mercury.setposition(-600,600)
text_mercury.write('Mercury: gray colour on screen, distance from Sun= 57.9 million km,\
 speed=170505 km/h', font=TEXT_FONT)


text_venus=turtle.Turtle()
text_venus.color('yellow')
text_venus.hideturtle()
text_venus.up()
text_venus.setposition(-600,550)
text_venus.write('Venus: rosybrown colour on screen, distance from Sun= 108.2 million km,\
 speed=126077 km/h', font=TEXT_FONT)


text_earth=turtle.Turtle()
text_earth.color('yellow')
text_earth.hideturtle()
text_earth.up()
text_earth.setposition(-600,500)
text_earth.write('Earth: blue colour on screen, distance from Sun= 149.6 million km,\
 speed=107000 km/h', font=TEXT_FONT)


text_mars=turtle.Turtle()
text_mars.color('yellow')
text_mars.hideturtle()
text_mars.up() 
text_mars.setposition(-600,450)
text_mars.write('Mars: red colour on screen, distance from Sun= 227.9 million km,\
 speed=86871 km/h' , font=TEXT_FONT)

text_jupiter=turtle.Turtle()
text_jupiter.color('yellow')
text_jupiter.hideturtle()
text_jupiter.up()
text_jupiter.setposition(-600,400)
text_jupiter.write('Jupiter: brown colour on screen, distance from Sun= 778.5 million km,\
 speed=69911 km/h' ,font=TEXT_FONT)

text_saturn=turtle.Turtle()
text_saturn.color('yellow')
text_saturn.hideturtle()
text_saturn.up()
text_saturn.setposition(-600,350)
text_saturn.write('Saturn: orange colour on screen, distance from Sun= 1434 million km,\
 speed=34821 km/h' , font=TEXT_FONT)

text_uranus=turtle.Turtle()
text_uranus.color('yellow')
text_uranus.hideturtle()
text_uranus.up()
text_uranus.setposition(-600,300)
text_uranus.write('Uranus: green colour on screen, distance from Sun= 2871 million km,\
 speed=2406 km/h' , font=TEXT_FONT)

text_neptune=turtle.Turtle()
text_neptune.color('yellow')
text_neptune.hideturtle()
text_neptune.up()
text_neptune.setposition(-600,250)
text_neptune.write('Neptune: orange colour on screen, distance from Sun= 4495 million km,\
 speed=19720 km/h' , font=TEXT_FONT)

sun=turtle.Turtle('circle')
sun.penup()
sun.color('yellow')
sun.penup()
Sun_image='Sun5.gif'
wn.addshape(Sun_image)
sun.shape(Sun_image)
sun.setposition(0,0)


mercury=turtle.Turtle()
mercury.up()
Mercury_image='mercury.gif'
wn.addshape(Mercury_image)
mercury.shape(Mercury_image)
mercury.setposition(0,-110)
mercury.up()

venus=turtle.Turtle()
venus.up()
Venus_image='venus1.gif'
wn.addshape(Venus_image)
venus.shape(Venus_image)
venus.setposition(0,-135)
venus.up()

earth=turtle.Turtle()
earth.up()
Earth_image='earth3.gif'
wn.addshape(Earth_image)
earth.shape(Earth_image)
earth.setposition(0,-190)

moon=turtle.Pen()
moon.up()
moon.setposition(0,60)
moon.shape('circle')
moon.shapesize(0.5)
moon.color('yellow')
moon.speed(0)

mars=turtle.Turtle()
mars.up()
Mars_image='Mars1.gif'
wn.addshape(Mars_image)
mars.shape(Mars_image)
mars.setposition(0,-280)


jupiter=turtle.Turtle()
jupiter.up()
Jupiter_image='Jupiter2.gif'
wn.addshape(Jupiter_image)
jupiter.shape(Jupiter_image)
jupiter.setposition(0,-350)

saturn=turtle.Turtle()
saturn.up()
Suturn_image='Saturn4.gif'
wn.addshape(Suturn_image)
saturn.shape(Suturn_image)
saturn.setposition(0,-450)

urans=turtle.Turtle()
urans.up()
Urans_image='Uranus.gif'
wn.addshape(Urans_image)
urans.shape(Urans_image)
urans.setposition(0,-540)

neptune=turtle.Turtle()
neptune.up()
Neptune_image='Neptune.gif'
wn.addshape(Neptune_image)
neptune.shape(Neptune_image)
neptune.setposition(0,-590)
#neptune.up()





earth.goto(0,-190)
running=True
while running:
    
    mercury.circle(110,0.478)
    venus.circle(135,0.35)

    earth.penup()
    earth.showturtle()
    earth.circle(190,0.3)

   
    moon.hideturtle()
    moon.goto(earth.xcor(),earth.ycor())
    #print(earth.xcor(),earth.ycor())
    moon.fd(45)
    moon.showturtle()
    moon.left(1)
    mars.up()
    mars.circle(280,0.24)
    jupiter.penup()
    jupiter.circle(350,0.15)
    saturn.penup()
    saturn.circle(450,0.1)
    urans.circle(540,0.08)
    neptune.circle(590,0.05)



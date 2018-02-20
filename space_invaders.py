import turtle
import os
import math
import random
#Screen
myScreen = turtle.getscreen()
myScreen.bgpic("galaxy.gif")
myTitle = turtle.title("SPACE INVADERS")

#Register Shape
turtle.register_shape("space_re.gif")
turtle.register_shape("shooter_re.gif")
#Create Border
borderPen = turtle.Turtle()
borderPen.speed(0)                  #0 = fastest
borderPen.color("RED")
borderPen.penup()
borderPen.setposition(-300, -300)   #co-ordinates
borderPen.pendown()
borderPen.pensize(3)
for side in range(0, 4):
    borderPen.forward(600)
    borderPen.left(90)
borderPen.hideturtle()

#Create Player

myPlayer = turtle.Turtle()
myPlayer.speed(0)
myPlayer.color("GREEN")
myPlayer.penup()
myPlayer.setposition(0, -280)
myPlayer.shape("shooter_re.gif")
myPlayer.shapesize(1, 1)
myPlayer.setheading(90)             #direction pointer

#create Enemy
#check the loop for multiple enemies

#Create Bullet----->BHAM->BHAM
myBullet = turtle.Turtle()
myBullet.hideturtle()
myBullet.speed(0)
myBullet.color("orange")
myBullet.penup()
myBullet.setposition(0, -270)
myBullet.shape("triangle")
myBullet.shapesize(0.5, 0.5)
myBullet.setheading(90)

#***********
#Functions

#Function for player-->Left and Right
playerSpeed = 15                    #15px for 1-click

def moveLeft():
    x = myPlayer.xcor()             #reads the coordinate
    x -= playerSpeed                #copies in x and increament when moving left
    if(x<-280):
        x = -280
    myPlayer.setx(x)

def moveRight():
    x = myPlayer.xcor()             #reads the coordinate
    x += playerSpeed                #copies in x and increament when moving left
    if (x>280):
        x=280
    myPlayer.setx(x)

#Function "BULLET"
bulletState = 'READY'
bulletSpeed = 20
def bulletFire():
    global bulletState
    if (bulletState == 'READY'):
        bulletState = 'FIRE'
        x = myPlayer.xcor()         #copy the current player xcor
        y = myPlayer.ycor() + 10    #copy yco-or add 10 for bullet
        myBullet.setposition(x, y)
        myBullet.hideturtle()

#Collisions
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if (distance<25):
        return True
    else:
        return False
    
#Function for Enemy movement
enemySpeed = 2

#Adding Multiple Enemies\
noEnemies = 5
enemiesList = []
for i in range(0, noEnemies):
    enemiesList.append(turtle.Turtle())
for myEnemy in enemiesList:
    #myEnemy = turtle.Turtle()
    myEnemy.penup()
    myEnemy.speed(0)
    myEnemy.color("YELLOW")
    #myEnemy.setposition(-150, 240)
    x = random.randint(-200, 200)
    y = random.randint(100, 240)
    myEnemy.setposition(x, y)
    myEnemy.shape("space_re.gif")
    myEnemy.shapesize(1, 1)
        
while True:
    for myEnemy in enemiesList:
        #Enemy movement infinite
        x = myEnemy.xcor()
        x += enemySpeed
        myEnemy.setx(x)

        if(myEnemy.xcor()>280):
            for i in enemiesList: 
                y = i.ycor()
                y -= 40
                i.sety(y)
            enemySpeed *= -1

        if(myEnemy.xcor()<-280):
            for i in enemiesList: 
                y = i.ycor()
                y -= 40
                i.sety(y)
            enemySpeed *= -1

        #Check the collision b/w Bullet and Enemy
        if isCollision(myBullet, myEnemy):
            myBullet.hideturtle()                   #Reset the Bullet
            #myEnemy.hideturtle()                    #Reset the enemy
            bulletState = 'READY'
            x = random.randint(-200, 200)
            y = random.randint(100, 240)
            myEnemy.setposition(x, y)
            
        #Check the collision b/w Enemy and Player
        if isCollision(myPlayer, myEnemy):
            myBullet.hideturtle()                   #Reset the Bullet
            myEnemy.hideturtle()                    #Reset the Enemy
            myPlayer.hideturtle()                   #Reset the Player
            print("---> GAME OVER <---")
            #turtle.title("GAME OVER")
            break
             
            #Bullet loop
        if (bulletState == 'FIRE'):
            y = myBullet.ycor()
            y += bulletSpeed
            myBullet.showturtle()
            myBullet.sety(y)
        if (myBullet.ycor()>270):
            myBullet.hideturtle()
            bulletState = 'READY'

        
        #onkey functions inside while
        #they have to work in the middle of the enemy movement
        #onkey functions
        turtle.listen()
        turtle.onkey(moveLeft, "Left")
        turtle.onkey(moveRight, "Right")
        turtle.onkey(bulletFire, "space")



#delay = raw_input("Enter to FINISH")

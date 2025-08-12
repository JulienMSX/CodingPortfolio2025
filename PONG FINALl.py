import turtle as t
import time
import tkinter 

#make game have varying speed selectable by player
#save highest score
#

# Score varibales
#root = Tk()
#mylabel = Label(root, "Hello")



player_a_score = 0
player_b_score = 0

p1_vic = 0
p2_vic = 0
Boom_score = 0

bullet_countL = 0
bullet_countR = 0

com = int(input('How many players?: 1 or 2?: '))

while (com != 1) and (com != 2):
    print('invalid player count')
    com = int(input('How many players?: 1 or 2?: '))
else:
    print('success')
if com == 1:
    p1n = input('Player 1 Name? ')
    p2n = 'Bob the Bot'
elif com == 2:
    p1n = input('Player 1 Name? ')
    p2n = input('Player 2 Name? ')
    
    
    





dif = int(input('choose difficulty: 0(easy),1 ,2 ,3(very hard): '))


#while True:
 #   if dif != {0, 1, 2, 3}:
  #      print('invalid difficulty')
   #     dif = int(input('choose difficulty: 0(easy),1 ,2 ,3(very hard): '))
    #else:
        
if dif == 0:
    sp = 3
elif dif == 1:
    sp = 4
elif dif == 2:
    sp = 5
elif dif == 3:
    sp = 6
else:
    print('unrecognized difficulty, defaulting to 1')
    sp = 4


gt = int(input('Game length in points:(RECCOMENDED) 5, 10, 15: '))
    


win = t.Screen()# creating a window
win.title("Ping-Pong Game") # Giving name to the game.
win.bgcolor('black')    # providing color to the HomeScreen
win.setup(width=900,height=600) # Size of the game panel 
win.tracer(0)   # which speed up's the game.

st = t.Turtle()
st.pu()
st.ht()
st.turtlesize(2)
st.speed(0)
st.color('Green')
st.goto(-100,-100)


h = t.Turtle()
h.pu()
h.ht()
h.speed(0)
h.goto(0,0)
#decal = t.Turtle
#decal.color('red')
#for i in range(0,10):
#    decal.circle(100, 11)



# Creating left paddle for the game

paddle_left = t.Turtle()
paddle_left.st()
paddle_left.speed(5)
paddle_left.shape('square')
paddle_left.color('green')
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

# Creating a right paddle for the game

paddle_right = t.Turtle()
paddle_right.speed(5)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color('blue')
paddle_right.penup()
paddle_right.goto(350,0)

# Creating a pong ball for the game

ball = t.Turtle()
ball.speed(10)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = sp   # Setting up the pixels for the ball movement.
ball_dy = sp

#Left Gun

gunL = t.Turtle()
gunL.speed(0)
gunL.turtlesize(3)
gunL.shape('turtle')
gunL.color('white')
gunL.penup()
gunL.goto(-1000, 1000)
gunL_dx = 6.0

#Right Gun

gunR = t.Turtle()
gunR.speed(0)
gunR.left(180)
gunR.turtlesize(3)
gunR.shape('turtle')
gunR.color('white')
gunR.penup()
gunR.goto(1000, 1000)
gunR_dx = 6.0  

#Boom


Boom = t.Turtle()

Boom.ht()
Boom.pu()
Boom.color('red', 'yellow')
Boom.speed(0)
Boom.goto(0, 1000)



    
# Creating a pen for updating the Score

pen = t.Turtle()
pen.speed(0)
pen.ht()
pen.color('skyblue')
pen.penup()
pen.goto(0,260)
pen.write("{}: 0                    {}: 0 ".format(p1n,p2n),align="center",font=('Courier',24,"normal"))


# Moving the left Paddle using the keyboard

def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 30
    paddle_left.sety(y)

# Moving the left paddle down

def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 30
    paddle_left.sety(y)

# Moving the right paddle up

def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 30
    paddle_right.sety(y)

# Moving right paddle down

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 30
    paddle_right.sety(y)

def SaveON():
    paddle_right.goto(350,0)
    paddle_left.goto(-350, 0)


def GunR_Fire():
    gunR.sety(paddle_right.ycor())
    gunR.setx(350 - 10)
    
    
    


    
def GunL_Fire():
    gunL.sety(paddle_left.ycor())
    gunL.setx(-350 + 10)
    
    #while True:
        
        
       # gunL.setx(gunL.xcor() + gunL_dx)
        
        #if(gunL.xcor() > 340) and (gunL.xcor() < 350) and (gunL.ycor() < paddle_right.ycor() + 40 and gunL.ycor() > paddle_right.ycor() - 40):
       #     gunL.ht()
         #   paddle_right.sety(1000)   
         #   gunL.goto(-1000,1000)
         #   break
       # elif gunL.xcor() > 1000:
          #  gunL.goto(-1000, 1000)
           # break
def Start():
    ball.goto(0,-50)
    
    st.goto(0,100)
    
    
    st.write("JULIEN's PONG", align='center',font=('Helvetica', 64, 'bold'))
    st.goto(0,0)
    st.color('White')
    st.write("Press 'Space'", align='center',font=('Courier', 36, 'italic'))
    #st.write(input("Player 1 Name?"))

    st.goto(0,-50)
    st.color('Green')
    
    st.pd()
    for i in range(0,111), 17:
        st.circle(100, 111) 
    st.penup()
       
        
    
    
    
def esc():
    if p1_vic > p2_vic:
        st.clear()
        st.goto(0, 100)
        st.write('{} has the current highscore of ({}) wins Congratulations'.format(p1n,p1_vic),align="center",font=('Courier',12,"normal"))
        time.sleep(1000)
        win.bye()
    elif p2_vic > p1_vic:
        st.clear()
        st.goto(0, 100)
        st.write('{} has the current highscore of ({}) wins Congratulations'.format(p2n,p2_vic),align="center",font=('Courier',12,"normal"))
        time.sleep(1000)
        win.bye()
    else:
        win.bye()
    
def spc():
    start.goto(0,0)
    
def menu():
    h.goto(0, -10)
def cmenu():
    h.goto(0, 0)
    #st.clear()
    #pen.clear()
    #pen.goto(0,260)
    #pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Courier',24,"normal"))
    
    

    
    
    
    
    
#st.listen()
#st.onkeypress(spc,"Space")
    
#Start()
#spc()        
              
# Keyboard binding
win.listen()

win.onkeypress(paddle_left_up,"w")
win.onkeypress(paddle_left_down,"s")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")
win.onkey(GunL_Fire,"e")
win.onkey(GunR_Fire,"/")
win.onkeypress(spc,"space")
win.onkeypress(esc,"Escape")
win.onkeypress(menu,"0")
win.onkeypress(cmenu,"9")
#win.onkeypress(Save,"g")


#make a function and boolean




# Main Game Loop
#while Start() == True:
    #spc()

start = t.Turtle()
start.ht()
start.pu()
start.goto(-100,-100)

go = 2   
comhit = False

while True:
    time.sleep(0.001)
    
        
    #make Start() go away
    if go == 2:
        start.goto(-101,100)
        Start()

    if start.pos() == (-101,100):
        
       
        

        
        st.goto(0, -150)
        st.write('',align='center',font=('courier',48,'bold'))
        if start.pos() == (0,0):
            ball.goto(0,0)
            Boom.clear()
            gunL.goto(1000,-1000)
            gunR.goto(-1000,1000)
            ball.clear()
            pen.clear()
            st.clear()
            Boom_score = 0
            player_a_score = 0
            player_b_score = 0
            pen.goto(0,260)
            pen.write("{}: {}                    {}: {} ".format(p1n,player_a_score,p2n,player_b_score),align="center",font=('Courier',24,"normal"))
            go = 1
    
   
         

    if start.pos() == (-100,100):
        ball.goto(0,0)
        
        st.goto(0,-50)
        st.color('Green')
    
        st.pd()
        for i in range(0,111, 17):
            st.circle(100, 111) 
        st.penup()
        Boom.ht()

        Boom.goto(0,-100)
        Boom.write('Want to play Again?',align='center',font=('courier',48,'bold'))
        Boom.goto(0, -150)
        Boom.write('Press SPACE to Start',align='center',font=('courier',48,'bold'))
        if start.pos() == (0,0):
            SaveON()
            
            Boom.clear()
            ball.clear()
            pen.clear()
            st.clear()
            Boom_score = 0
            player_a_score = 0
            player_b_score = 0
            pen.goto(0,260)
            pen.write("{}: {}                    {}: {} ".format(p1n,player_a_score,p2n,player_b_score),align="center",font=('Courier',24,"normal"))
            go = 1
    
    
    if go == 1:
        
    
        win.update()
        

    # This methods is mandatory to run any game

    # Moving the ball
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)


#computer vs player
        if com == 1:
            paddle_right.goto(350,ball.ycor())
            if comhit == True:
                paddle_right.sety(10000)
            if paddle_right.ycor() == (paddle_left.ycor() + 10) and (paddle_left.ycor() - 10):
                GunR_Fire()
                


        



    # setting up the border
    
    
        

        
            

        if ball.ycor() > 290:   # Right top paddle Border
        
            ball.sety(290)
            ball_dy = ball_dy * -1
        
    
        if ball.ycor() < -290:  # Left top paddle Border
        

            ball.sety(-290)
            ball_dy = ball_dy * -1
        

        if ball.xcor() > 390:   # right width paddle Border
            ball.goto(0,0)
            ball_dx = ball_dx * -1
            player_a_score = player_a_score + 1
            gunL.clear()
            gunR.clear()
            Boom.clear()
            SaveON() == True
            comhit = False
            pen.clear()
            pen.write("{}: {}                    {}: {} ".format(p1n,player_a_score,p2n,player_b_score),align="center",font=('Courier',24,"normal"))
        #os.system("afplay wallhit.wav&")



        if(ball.xcor()) < -390: # Left width paddle Border
            ball.goto(0,0)
            ball_dx = ball_dx * -1
            player_b_score = player_b_score + 1
            gunL.clear()
            gunR.clear()
            Boom.clear()
            SaveON() == True
            comhit = False
            pen.clear()
            pen.write("{}: {}                    {}: {} ".format(p1n,player_a_score,p2n,player_b_score),align="center",font=('Courier',24,"normal"))
        #os.system("afplay wallhit.wav&")


    # Handling the collisions with paddles.

        if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
            ball.setx(340)
            ball_dx = ball_dx * -1
        #os.system("afplay paddle.wav&")

        if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
            ball.setx(-340)
            ball_dx = ball_dx * -1
        #os.system("afplay paddle.wav&")

    #Gun Control 
    
        gunR.setx(gunR.xcor() - gunR_dx)
        if(gunR.xcor() < -340) and (gunR.xcor() > -350) and (gunR.ycor() < paddle_left.ycor() + 80 and gunR.ycor() > paddle_left.ycor() - 80):
            paddle_left.sety(10000)
            gunR.goto(-200, 0)
            gunR.write('You Died'.format(gunR), align='center', font=('Verdana', 36,"bold"))
        

            gunR.goto(-1000,1000)
        
# Bullets
        elif gunR.xcor() < -1000:
            gunR.goto(-1000, 1000)
            bullet_countR = 0
        if gunR.xcor() < 350:
            bullet_countR = 1
            #print(bullet_countR)
        #if bullet_countR == 1:
            
            #win.onkey(GunR_Fire,'/') = win.onkey(GunR_Fire,None)
    
                
          

        gunL.setx(gunL.xcor() + gunL_dx)
        if(gunL.xcor() > 340) and (gunL.xcor() < 350) and (gunL.ycor() < paddle_right.ycor() + 80 and gunL.ycor() > paddle_right.ycor() - 80):
            paddle_right.sety(10000)
            comhit = True
            gunL.goto(200, 0)
            gunL.write('You Died'.format(gunR), align='center', font=('Verdana', 36,"bold"))

            gunL.goto(-1000,1000)
        
        
        elif gunL.xcor() > 1000:
            gunL.goto(-1000, 1000)
            bullet_countL = 0
        if gunL.xcor() > -350:
            bullet_countL = 1
        #if bullet_countL == 1:
            #win.onkey(GunL_Fire,"e") = None
        


    #Boom 
        if  (gunL.xcor() > gunR.xcor() - 2) and (gunL.ycor() < gunR.ycor() + 35 and gunL.ycor() > gunR.ycor() - 35):
            Boom.goto(gunL.xcor(),gunL.ycor())
            gunL.goto(-1000, 1000)
            gunR.goto(1000,-1000)
            Boom.pendown()
            Boom.begin_fill()
            for i in range(0, 50):
                Boom.forward(200)
                Boom.left(170)
    
        
            Boom.end_fill()
            Boom.penup()
            if (Boom.xcor() < -200) and (Boom.xcor() > -500) and (Boom.ycor() < paddle_left.ycor() + 200 and Boom.ycor() > paddle_left.ycor() - 200):
                paddle_left.sety(10000)
                gunL.goto(-200, 0)
                gunL.write('You Died'.format(gunR), align='center', font=('Verdana', 36,"bold"))
                gunL.goto(1000,-1000)
            elif (Boom.xcor() > 200) and (Boom.xcor() < 500) and (Boom.ycor() < paddle_right.ycor() + 200 and Boom.ycor() > paddle_right.ycor() - 200):
                paddle_right.sety(10000)
                comhit = True
                gunR.goto(200, 0)
                gunR.write('You Died'.format(gunR), align='center', font=('Verdana', 36,"bold"))
                gunR.goto(1000,-1000)
            else:
                Boom.goto(0, 1000)
                Boom_score = Boom_score + 1
   
    

        if Boom_score > 4:
            Boom.clear()
            Boom_score = 0
    

        


   
        if player_a_score >= gt:
            p1_vic += 1
            #SaveON() == True
            ball.goto(0,0)
            pen.goto(0,180)
            pen.write('{} Wins'.format(p1n), align='center',font=('Courier', 64, 'bold'))
            go = 0
            start.goto(-100,100)
         #Start() 
        #pen.goto(0,0)
           #pen.write("Press 'Space'", align='center',font=('Courier', 36, 'italic'))
        
        
       
        if player_b_score >= gt:
            p2_vic += 1
            ball.goto(0,0)
            pen.goto(0,180)
            pen.write('{} Wins'.format(p2n), align='center',font=('Courier', 64, 'bold'))

            go = 0
            start.goto(-100,100)
        #pen.goto(0,0)
        #pen.write("Press 'Space'", align='center',font=('Courier', 36, 'italic'))
        if h.pos() == (0,-10):
            ball.goto(0,0)
            Boom.clear()
            gunL.goto(1000,-1000)
            gunR.goto(-1000,1000)
            ball.clear()
            pen.clear()
            st.clear()
            Boom_score = 0
            pen.goto(0,260)
            pen.write("{}: {}                    {}: {} ".format(p1n,player_a_score,p2n,player_b_score),align="center",font=('Courier',24,"normal"))
            st.goto(0, 150)
            st.write("Pause Menu",align='center',font=('Courier',32,'italic'))
            st.goto(0, 100)
            if p1_vic > p2_vic:
                st.write("The current highscore is ({}) wins by {}".format(p1_vic,p1n),align='center',font=('Courier',18,'italic'))
            elif p2_vic > p1_vic:
                st.write("The current highscore is ({}) wins by {}".format(p2_vic,p2n),align='center',font=('Courier',18,'italic'))
            else:
                None

            st.goto(0,0)
            st.write("Resume?",align='center',font=('Courier',32,'italic'))
        if h.pos() == (0,0):
            st.clear()
        
        
    
    
        #Reset if both players die
    

        #if paddle_right.ycor() > 1000 and paddle_left.ycor() > 1000:
        #SaveON() == True
        #gunL.clear()
        #gunR.clear()
    
    #if pen.pos() == (670,670):
        #win.bye()
    
    
        
        
          
     



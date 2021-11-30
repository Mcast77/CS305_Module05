#For the person in charge of commenting, please add more/better comments
#I, Marco, improved the collision function inorder to work more efficient
#I also redid the "p" hotkey so it works 100% of the time, it was not working
#all the time because it was in a while loop, so the pen was randomly choosing
#to stay up or down
#import the modules needed
import sys
from turtle import *
import keyboard
def main():
    #checks to see if there are arguements
    if len(sys.argv) >1:
        width = int(sys.argv[1])
        height= int(sys.argv[2])
    else:
        width=200
        height=200
    #sets up the window for turtle
    win_setup(width,height)
    #sets speed for turtle
    speed('fastest')
    #direction, If turtle should be running, if pen is up(0) or down(1)
    commands=["",True,1]
    #hotkeys for controls
    keyboard.add_hotkey("w",t_up,[commands])
    keyboard.add_hotkey("s",t_down,[commands])
    keyboard.add_hotkey("a",t_left,[commands])
    keyboard.add_hotkey("d",t_right,[commands])
    keyboard.add_hotkey("p",pen_status,[commands])
    keyboard.add_hotkey("q",t_quit, [commands])
    #runs if commands[1] is ture
    while commands[1]:
        #if commands[0],diretion is not ""
        if commands[0]!="":
            #sets turtle heading to commands[0]
            setheading(commands[0])
            #checks to see if there is collision
            collision(width,height)
            # moves turtle forward
            forward(1)
        #pen status, needed inorder for pen to work correctly all the time
        if commands[2]==0:
            #if commands[2] is set to up(0),put pen up
            up()
        else:
            #else commands[2] should be down(1), so put pen down
            down()
    #when commands[1] is false exists while loop then closes turtle
    bye()
#sets direction to north(90)
def t_up(lists):
    lists[0]=90
#sets direction to south(270)
def t_down(lists):
    lists[0]=270
#sets direction to west(180)
def t_left(lists):
    lists[0]=180
#sets direction to east(0)
def t_right(lists):
    lists[0]=0
#a function needed for the pen to stay up or stay down
def pen_status(lists):
    #if pen is down
    if isdown():
        #set lists[2] (pen status) to up so the program will later know to put the pen up
        lists[2]=0
    else:
        #set lists[2] (pen status) to down so the program will later know to put the pen down
        lists[2]=1
# a function that will end turtle by exiting the main functions while loop
def t_quit(lists):
    #ends turtle by setting lists[1] (if game should be running) to false which exsits while loop which cuases
    #the main function to run the "bye" command
    lists[1]=False
#a function to detect collision
def collision(width,height):
    #if x coordinate is at half of width, the side wall
    if abs(xcor()) ==(width/2):
        #if pen is down it is picked up, teleported to the other side, then put back down
        if isdown():
            up()
            setx(-1*xcor())
            down()
        #if pen is up, it stays up and teleports to the other side
        else:
            setx(-1*xcor())
    #if x coordinate is at half of height, the top wall/ roof
    if abs(ycor()) ==(height/2):
        #if pen is down it is picked up, teleported to the other side, then put back down
        if isdown():
            up()
            sety(-1*ycor())
            down()
        #if pen is up, it stays up and teleports to the other side
        else:
            sety(-1*ycor())
#a function to set up the window for the turtle using the inputted width and height
def win_setup(width,height):
    setup(width,height)
    bgcolor('grey')
#runs main function
main()

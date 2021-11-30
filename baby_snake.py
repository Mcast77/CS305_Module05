from turtle import*
from Lab2_functions import *
import sys

def main():
    if len(sys.argv)<2:
        width=10
        height=10
    else:
        width=int(sys.argv[1])
        height=int(sys.argv[2])
    pair=int(width/2)
    TILE=20
    window_setup(width,height,TILE)
    draw_grid(0,0,TILE,pair,TILE,height)
    snake(TILE,width,height)
    
def draw_row(x_coord,y_coord,TILE,pair,color1,color2):
    for rect_pair in range(1,pair+1):
        start_x_coord=x_coord+(2*TILE*(rect_pair-1))
        draw_rect(start_x_coord, y_coord, TILE, TILE, color1)
        draw_rect((x_coord + TILE) + (2 * TILE * (rect_pair - 1)), y_coord,
                  TILE, TILE,color2)
def draw_grid(x_coord, y_coord, size, pair,offset, rows):

    for number_of_line in range(1, int((rows/2)+1)):

        start_point_y = 2 * size * (number_of_line - 1)

        draw_row(x_coord, y_coord + start_point_y , size, pair
                    ,'black','white')
        draw_row(x_coord, y_coord + size + start_point_y ,
                 size, pair,'white','black')

def snake(TILE,width,height):
    loops=0
    ht()
    half=TILE/2
    y_limit=(TILE*height-half)
    x_limit=(TILE*width-half)
    start=[half,half]
    snake=[[half,half],[half+TILE,half],[half+TILE*2,half]
           ,[half+TILE*3,half],[half+TILE*4,half]]
    #corners=[[10,10],[190,10],[10,190],[190,190]]
    while loops!=11:
        for index in range(len(snake)):
            if index==0:
                up()
                goto(snake[index])
                forward(half)
                down()
                triangle(3*TILE/4)
            else: 
                up()
                begin_fill()
                color('blue')
                goto(snake[index])
                down()
                dot(2*TILE/3)
                end_fill()
        update()
        new_snake=[]
        for segment in range(len(snake)):
            if snake[segment][0]==half and snake[segment][1]<y_limit:
                new_snake.append([snake[segment][0],snake[segment][1]+TILE])
            elif snake[segment][1]==y_limit and snake[segment][0]<x_limit:
                new_snake.append([snake[segment][0]+TILE,snake[segment][1]])
            elif snake[segment][0]==x_limit and snake[segment][1]>half:
                new_snake.append([snake[segment][0],snake[segment][1]-TILE])
            elif snake[segment][1]==half and snake[segment][0]>half:
                new_snake.append([snake[segment][0]-TILE,snake[segment][1]])
        snake=new_snake
        for parts in range(len(snake)):
            if parts==0:
                for actions in range(14):
                    undo()
            else:
                for actions in range(7):
                    undo()
        if snake[1]==start:
            loops+=1
    bye()
def window_setup(width,height,TILE):
    bgcolor('grey')
    title("SNAKE!")
    pencolor('blue')
    tracer(False)
    setup((width*20),(height*20),0,0)
    setworldcoordinates(-width-TILE,(width*20)+40,(height*20)+40,-height*2)

def triangle(lenght):
    setheading(0)
    begin_fill()
    color('red')
    left(30)
    forward(lenght)
    right(120)
    forward(lenght)
    right(120)
    forward(lenght)
    end_fill()
main()

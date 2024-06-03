import threading
import turtle
import random

screen = turtle.Screen()
screen.bgcolor('light blue')

def random_color():
    return(random.random(), random.random(), random.random())

def draw_square(t,size):
    for _ in range(4):
        t.forward(size)
        t.right(90)
        t.color('red','yellow','green','blue','pink','brown','black','purple')
    t.end_fill()

# 거북이 생성 사각형 그리기 코드
turtles = []
for _ in range(9):
    t = turtle.Turtle()
    t.speed(5)
    t.color(random_color())
    turtles.append(t)

square_size = 100
start_x = -57
start_y = 85

# 3*3 배열로 사각형을 그리는 루프 코드
for o in range(3):
    for p in range(3):
        t = turtles[o * 3 + p]
        t.penup()
        t.goto(start_x + p * (square_size + 20), start_y - o * (square_size + 20))
        t.pendown()
        draw_square(t,square_size)

th1 = threading.Thread(target = turtle)  

th1.start()

th1.join()


# 루프 시작 코드
turtle.mainloop()
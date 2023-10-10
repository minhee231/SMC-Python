import turtle as t
import time
#turtle.shape() 커서 모양을 바꿀 때
#turtle.shape() 거북이 모양


t.shape('turtle')
t.speed(140)
# t.forward(100)

# t.forward(50)
# t.backward(100)
# t.right(90)
# t.left(45)
# t.setheading(60)
t.color('blue')
t.bgcolor('black')
# t.circle(50)

# #정삼각형 그리기
# for i in range(3):
#     t.forward(80) 
#     t.left(120)


# #정사각형 그리기
# for i in range(4):
#     t.forward(80) 
#     t.left(90)

# #정오각형 그리기
# for i in range(5):
#     t.forward(80) 
#     t.left(72)

# #정육각형 그리기
# for i in range(6):
#     t.forward(80) 
#     t.left(60)

# #별그리기
# for i in range(5):
#     t.backward(80) 
#     t.left(145)

gak = 1

for i in range(120):
    for x in range(6):
        t.color('blue')
        t.forward(100)
        t.left(60)
    t.left(gak)

    for j in range(6):
        t.color('yellow')
        t.forward(100)
        t.left(60)
    t.left(gak)

    for k in range(6):
        t.color('red')
        t.forward(100)
        t.left(60)
    t.left(gak)












time.sleep(1000)
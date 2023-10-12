import turtle as t

#penup 그림을 그리지 않음
#pendown 그림을 그림
#clear 캔버스 지우기
#goto(x,y) 좌표이동
#getx,gety 좌표 얻기
#window_width, window_height 창의 넓이, 높이값 가져오기
#window_size(width, height) 윈도우 크기 저자
#960*810

t.bgcolor('black')
t.color('white')

t.right(90)
t.penup()
t.forward(100)

#얼굴 그리기
t.right(90)
t.forward(100)
t.right(180)
t.pendown()
t.circle(130)


t.penup()
t.left(90)
t.forward(20)
t.right(90)
t.forward(100)

t.pendown()
t.right(180)
t.circle(60)

t.penup()
t.right(90)
t.forward(130)
t.right(90)

t.pendown()
t.circle(60)
from turtle import * # turtle 모듈로부터 모두 import

color('black','gray') # 선, 터틀 색깔
pensize(3)
begin_fill() # 색 채우기


penup()
goto(0, -100) # x, y 좌표

pendown()
circle(100) # 원의 크기

left(45) # 원 안의 대각선
fd(140) # forward의 약어, 전진
rt(-90) # -90도 오른쪽 회전
fd(140)
rt(-90)
fd(140) # ...
rt(-90)
fd(140)

end_fill() # 종료 부분 코드
mainloop() # 유저의 입력을 계속 기다리게 하는 목적
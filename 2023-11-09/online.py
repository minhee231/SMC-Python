#상황 예시 온라인 강좌를 다음으로 넘기는 매크로
# 온라인 강의는 다음수업 버튼을 누르면 다음 강의로 넘어감
# 새 강의 시작 후 최소 "1분"이 지나야 다음수업 버튼을 누를 수 있음
# 강의 화면을 띄운 상태에서 1분이 지난 후 다음수업을 누를 수 있도록 구현
# "다음수업" 버튼을 계속 눌러서 50회 반복하도록 구현.

import pyautogui as pg
import time


for i in range(50):
    pg.click(1358,1010,duration=1) #봤어요
    time.sleep(0.1)
    pg.click(1496,1010,duration=1) #다음으로
    time.sleep(61)
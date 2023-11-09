import pyautogui as pg
import time
# print(pg.size())
# print(pg.position())

# pg.moveTo(832,345)
# pg.click()
# pg.click(400,400,duration=1)
# pg.click(clicks=2,interval=0.2, button='right')

path = "C:/Users/goomi/OneDrive/바탕 화면/작업/Desk/창남쌤파이썬방과후/2023-11-09/ddd.PNG"
path = "C:/Users/goomi/Downloads/ddd.PNG"
i = pg.locateCenterOnScreen(path)
print(i)

pg.click(i)

# q = pg.center(i)
#pg.mouseInfo()

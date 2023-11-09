import pyautogui as pg

print(pg.position())

pg.screenshot('num2.png',region=(286,476,40,40))

cl2 = pg.locateCenterOnScreen('num2.png')
pg.click(cl2)

print(cl2)



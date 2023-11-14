import pyperclip
import pyautogui as pg
import time

pyperclip.copy('문자열')
pg.hotkey('win','r')
# time.sleep(0.3)
# pg.hotkey('tab')
# time.sleep(0.2)
# pg.write('not')

# time.sleep(0.2)
# pg.hotkey('[enter]')
# time.sleep(0.2)
# #pg.hotkey('enter')
# pg.hotkey('ctrl','v')

pg.alert('경고창')

btn = pg.confirm("테스트")
print(btn)

btn2 = pg.confirm("선택하세요")

if btn2 == 'OK':
    print("OK입니다")
else:
    print("아니요")
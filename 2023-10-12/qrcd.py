#create(contents, errpr, mode)
#       contents(data)만 지정해줘도 됨.

#eps(file) : QR코드를 file을 eps형식으로 작성
#svg(file) : QR코드 file을 svg 형식으로 작성
#png(file,scale,module_color,background): png 형식으로 작성
#   scale - QR코드 크기
#   module_color - QR코드 rgb 색상(일반적으로 검은색), 마지막은 투명도
#   background - 배경 rgb 색상(일반적으로 흰색), 마지막은 투명도

import pyqrcode
# qrcode = pyqrcode.create("https://naver.com")
# qrcode.svg("qr_naver.svg")
# qrcode.eps("qr_naver.eps")

# url = 'https://www.youtube.com/'

# qrcode = pyqrcode.create(url, error='H', mode='binary')
# qrcode.png('qr_youtube.png', scale=8, module_color=[0, 0, 0, 255], background=[100, 100, 100, 255])


# data = "WIFI:S:senWiFi_Free;T:WPA;P:sen2021!wi;"
# qrcode = pyqrcode.create(data, mode='binary')
# qrcode.png('qrwifi.png', scale=8, module_color=[10,10,50,255], background=[255,255,255,255])

#응용
# print('###Wifi접속 스크립트 ###')
# ssid = str(input('와이파이 SSID를 입력하세요 :'))
# secu = input('암호화 방식을 입력하세요(WPA,WPA2,WPA2-PSK,TKIP 등) :')
# pwd = str(input('와이파이 패스워드를 입력하세요 :'))

# qrcode = pyqrcode.create(f'WIFI:S:{ssid};T:{secu};P:{pwd};')
# qrcode.png('qr_wifi2.png', scale=8, module_color=[0,0,0,255], background=[255,255,255,255])

data = "BEGIN:VCARD\n"
data += "VERSION:3.0\n"
data += "FN:김선생\n"
data += "TELL:TYPE=WORK  ;CELL:010 1234 1234\n"
data += "END:VCARD\n"

qrcode = pyqrcode.create(data, mode='binary', encoding='utf-8')
qrcode.png('qr_namecard.png', scale=6, module_color=[10,10,100,255] , background=[255,255,255,255])

data = "BEGIN:VCARD\n"
data += "VERSION:3.0\n"
data += "FN:김선생\n"
data += "ORG:세명컴퓨터고등학교\n"
data += "TITLE:교사\n"
data += "TELL;TYPE=WORK  ;CELL:010 1234 1234\n"
data += "TELL;TYPE=HOME  ;CELL:010 4444 5555\n"
data += "EMAIL;TYPE=WORK::abc@naver.com\n"
data += "URL;TYPE=WORK:https://smc.sen.hs.kr\n"
data += "END:VCARD\n"



qrcode = pyqrcode.create(data, mode='binary', encoding='utf-8')
qrcode.png('qr_namecard2.png', scale=6, module_color=[10,10,100,255] , background=[255,255,255,255])

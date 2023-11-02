import qrcode
import cv2

def read(open_img):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(open_img)
    if data:
        print(data)
        print(bbox)
        print(_)
# filepath = "C:/Users/goomi/OneDrive/바탕 화면/작업/Desk/창남쌤파이썬방과후/2023-11-02/qr_wifi2.png"
# filepath = "./qr_wifi2.png"
# filepath = 'https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F0156e6cd-5919-408d-a3da-5c9efa4be01e%2F0266bf58-74da-4dce-9d32-8c6328da03ad%2Fqr_wifi2.png?table=block&id=c1801a43-2033-4807-acc5-e3df7b0ebfb1&spaceId=0156e6cd-5919-408d-a3da-5c9efa4be01e&width=2000&userId=ad050ec8-fa93-4db8-9dbc-7c288cfa1aba&cache=v2'
filepath = 'https://imgur.com/hQYBlH9.png'
cv_img1=cv2.imread(filepath)
read(cv_img1)

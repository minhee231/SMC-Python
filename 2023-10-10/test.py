#리스트 압축

#짝수 만으로 리스트 만들기
myList = [1,2,3,4,5,6,7,8,9,10]
even = []
for i in myList:
    if i&2 ==0:
        even.append(i)
print(even)

#한줄로 요약
even = [i for i in myList if i&2==0]
print(even)

#5보다 작은 정수
small = [i for i in myList if i<5]
print(small)

#변수값 가공도 가능
small = [i+10 for i in myList if i<5]
print(small, "변수 가공")

#문자열 가공
#문자열 길이
a = 'apple'
b = 'apple watch!'
print(len(a)) #5
print(len(b)) #15

#한글 길이도 인식
a = '사과'
b = '애플 와치~'
print(len(a)) #2
print(len(b)) #6

#문자열 쪼개기
a = 'This is an apple'
words = a.split(' ') #띄어쓰기를 기준으로 문자열을 분리해 list 형태로 반환
print(words)

a = 'This-is-an-apple'
ab = a.split('-') # - 을 기준으로 문자열을 분리
print(ab[0])
print(ab[1])
print(ab[0] + ab[1])

#대소문자 전환 (한글은 안됨)
a = 'Semyeong Computer Highschool'
a.lower() #문자열을 소문자로 반환
print(a)

a.upper() #문자열을 대문자로 반환
print(a)

#특정 문자열 시작/끝 부분 일치 여부 검색
a = '01-smcimg.jpg'
b = '02-smcimg.png'
c = '03-smcimg.gif'
a.startswith('01') #True 반환

a.endswith('png') #false 반환

myList = [a,b,c]
for file in myList:
    if file.endswith('jpg'):
        print(file) #a 출력

#특정 문자열 교체(replace)
a = '01-smcimg.jpg'
ab = a.replace('.jpg', '.bmp') 

print(ab) # 01-smcimg.bmp

#불필요한 공백 제거(strip)
a = '  kim semyeong'
b = 'kim semyeong'
c = 'kim semyeong  '

print(a.strip())

print(a.strip() == b) #true

#문자열 인덱싱
str = 'abcdef'

print(str[0]) #a
print(str[3]) #d
print(str[-1]) #f
print(str[-2]) #e

#문자열 슬라이싱
str = "Semyeong Computer Highschool"
print(str[:8]) # 0~7 인덱스 리턴
print(str[9:17]) #9~16 인덱스 리턴
print(str[18:]) #18~문자열의 끝까지 리턴
S = "철수가 '안녕' 하고 말했다"
# 작은 따옴표를 사용하기 위해 문자열을 큰 따옴표로 묶는다.

B = '철수가 "안녕" 하고 말했다'
# 큰 따옴표를 사용하기 위해 문자열을 작은 따옴표로 묶는다.

#자료형 (집합)
#list, Tuple, Set, Dict

#List 자료형
MyList = []
print(type(MyList))

MyList = [1,2,3,4,5]

#값 추가
MyList.append(1)
#[1,2,3,4,5,1]

MyList.append(2)
print(MyList)
#[1,2,3,4,5,1,2]

#값 제거
MyList.remove(1)
print(MyList)
#[2,3,4,5,1,2]

#값 제거 
MyList.remove(2)
print(MyList)

#인덱스 접근
print(MyList[0])
print(MyList[-1])
print(MyList[-4])

#List의 길이
print(len(MyList))

#==================================================================

#Tuple 자료형
MyTuple = (1,2,3,4,5,5)
#MyTuple.append(1)  읽기 전용이라 값 추가 불가능 
#MyTuple.remove(1)  읽기 전용이라 값 삭제 불가능

print(MyTuple.count(5))
#5의 갯수 출력 (2)

print(MyTuple.index(3))
#3의 인덱스 위치 출력 (2)

#==================================================================

#Set 자료형
MySet = set()
print(type(MySet))

#값 추가
MySet.add(1)
MySet.add(2)
MySet.add(3)

#중복된 값은 추가 불가능
MySet.add(1)
MySet.add(2)
MySet.add(4)

#==================================================================

#Dict 자료형 Key값과 Value값을 가지고 있음
MyDict = dict()
print(type(MyDict))

MyDict['apple'] = 123
print(MyDict['apple'])
#Key에 접근하면 Value 출력

#0이라는 Key에 2라는 Value 선언
MyDict[0] = 2
print(MyDict[0]) #Value값인 2출력
print(MyDict)

#Value값 변경
MyDict['apple'] = '안녕하세요'
print(MyDict['apple'])

print(len(MyDict))
#2

#조건문===============================================================

answer = input()
if answer == "Y":
    print("Yes")
else:
    print("No")


#elif 사용
age = 17
if age < 12:
    print("초딩")
elif age < 15:
    print("중딩")
elif age < 18:
    print("고딩")
else:
    print("으르신")


#반복문===============================================================
MyList = [1,2,3,4,5,6,7,8,9.10]

for i in MyList:
    print(i)

#range
for j in range(0,10):
    print(j)


#Continue
for i in MyList:
    if i%2 == 1:
        continue
    print(i)

#Break
for i in MyList:
    if i >=6:
        break
    print(i)


#반복문 국룰 구구단 & 별찍기
for x in range(2,10):
    for y in range(1,10):
        print("%d * %d = %d" %(x,y,x*y))


#함수는 반복적으로 사용되는 부분을 묶어서 재사용이 가능하게 해주는 것

def avg(var1, var2 , var3):
    print((var1+var2+var3)/3)

avg(30,40,60)

#예제) list에 있는 값들의 평균값을 구하는 함수
def list_avg(mylist):
    return sum(mylist) / len(mylist)

Test = [234,239,2392,393,2983,12]
list_avg(Test)

def gugu(dan):
    for i in range(1,10):
        print(f'{dan} X {i} = {dan*i}')    
gugu(3)

#인자의 기본값 지정
def calc(i,j, factor = 1 ):
    return i*j*factor


print(calc(1,2))
#2

print(calc(1,2,3))
#9

#Named 파라미터
def report(name, age, score):
    print(name, score, age)

# 인자를 순서와 상관없이 넣을 수 있음
report(age=10, name="kim", score=90)

#가변길이 파라미터
def total(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

s = total(1,2)
print(s)
#3

s = total(1,2,3,5)
print(s)
#11

#다중 리턴값
def calc(*numbers):
    count = 0
    sum = 0
    for n in numbers:
        count += 1
        sum += n
    return count,sum

#리턴값 튜플
print(calc(1,2,3))
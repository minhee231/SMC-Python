#print 함수

a = 1
b = 'str'

print(a,b)
print("------")
print(a, b, end='\n')
print(a, b, end='\n')
print(a, b, end='\n')
print("------")
print(a, b, end=' ')
print(a, b, end=' ')
print(a, b, end=' ')
print("------")

print([1,2,3,4,5])
print(a,b)
print(a,b, sep='|')

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in matrix:
    print(i)

print(*matrix, sep='\n')

#변수 출력 format

print('나는 %s 고등학교 %d학년 %d 반입니다'%('세명컴퓨터',2,3))
print('나는 {}고등학교 {}학년 {}반입니다'.format('세명컴퓨터',2,3))
print('%d는 16진수로 %x입니다.'%(30,30))

a = '세명컴고'
b = '홍길동'
print(f'안녕하세요 {a}에 다니는 {b}입니다.')
print(f'안녕하세요 {{{a}}}에 다니는 {{{b}}}입니다.')

# 정수 2개 입력받아 비교하기2
'''
두 정수(a, b)를 입력받아
a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

입력: 0 0
출력: True
'''

a, b = input().split()
a = int(a)
b = int(b)
print(a == b)
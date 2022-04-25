# 정수 2개 입력받아 비교하기1
'''
두 정수(a, b)를 입력받아
a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.
'''
'''
True(참) 또는 False(거짓) 값으로만 표현하고 저장하는 값을 불(bool)/불리언(boolean) 값이라고 한다.
정수, 실수, 문자, 문자열과 마찬가지로 또 다른 형태의 데이터형(data type)이다.
'''

a, b = input().split()
a = int(a)
b = int(b)
print(a < b)
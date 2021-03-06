# 정수 3개 입력받아 가장 작은 값 출력하기

'''
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.

참고
프로그래밍언어 소스코드 작성시 모든 요소들은
"순서에 따라 한 단계씩 실행"
"미리 정해진 순서에 따라 하나씩 연산 수행"
"그 때까지 연산된 결과를 이용해 다시 순서에 따라 하나씩 연산"
'''

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

x = (a if a < b else b)
print(x if x < c else c)

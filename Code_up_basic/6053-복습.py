# 참 거짓 바꾸기
'''
정수값이 입력될 때,
그 불 값을 반대로 출력하는 프로그램을 작성해보자.

예시
a = bool(int(input()))
print(not a)

이러한 논리연산을 NOT 연산(boolean NOT)이라고도 부르고,
프라임 '(문자 오른쪽 위에 작은 따옴표), 바(기호 위에 가로 막대), 문자 오른쪽 위에 c(여집합, complement) 등으로 표시한다.
모두 같은 의미이다.

참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산 된다.
'''
a = int(input())
print(bool(not a))
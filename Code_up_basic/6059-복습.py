# 비트단위로 NOT 하여 출력하기

'''
입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력
비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)

** 비트단위(bitwise) 연산자는,
~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
<<(bitwise left shift), >>(bitwise right shift)
가 있다.

정수 1개를 입력하여 비트 단위로  바꾼 후 그 값을 10진수로 출력한다.

~n = -n - 1
-n = ~n + 1 과 같은 관계로 표현할 수 있다.
'''
a = int(input())
print(~a)
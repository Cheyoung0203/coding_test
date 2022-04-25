# 정수 3개 입력받아 함과 평균 출력하기
# 입력: 1 2 3
# 출력: 6 2.00

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a + b + c
ave = float(sum / 3)

print(sum, format(ave, ".2f"))
# 실수 1개 입력받아 소숫점이하 자리 변환하기
# format(f, .2f): 실수 f의 소수 둘째짜리까지 반올림한다.
# round(f, 2): 반올림 함수, 실수 f의 소수 둘째자리까지 반올림

a = input()
a = float(a)
print(format(a, ".2f"))
print(round(a, 2))
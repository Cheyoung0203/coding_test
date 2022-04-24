# 실수 2개 입력받아 나눈 결과 계산하기
# round는 짝수를 반환한다. 따라서 round(0, 5)는 1이 아니라 0을 반환한다. 3.5는 4를 반환

f1, f2 = input().split()
f3 = float(f1) / float(f2)

print(format(f3, ".3f"))
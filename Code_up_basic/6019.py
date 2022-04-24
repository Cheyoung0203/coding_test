# 연월일 입력받아 순서 바꿔 출력하기
# 입력: 연,월,일이 '.'으로 구분되어 입력되야함 ex. 2020.3.4
# 출력: -를 구분기호로 사용해서 일-월-연도로 출력 ex. 4-3-2020

year, month, day = input().split('.')
print(day, month, year, sep='-')
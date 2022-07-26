# 1부터 모든 숫자를 넣어서 식을 계산
# 1 -> 1 + 1 = 2
# 2 -> 2 + 2 = 4
# 3 -> 3 + 3 = 6
# 4 -> 4 + 4 = 8
# 5 -> 5 + 5 = 10
# 10 -> 10 + 1 + 0 = 11
# 11 -> 11 + 1 + 1 = 13
# 20 -> 20 + 2 + 0 = 22
# 100 -> 100 + 1 + 0 + 0 = 101



def sum_digits(n):
    n= str(n)
    sum_n = int(n)
    for i in range(len(n)):
        sum_n += int(n[i])

    return sum_n


sum_digits_list = []
ten_thousand_list = list(range(1,10000))


for n in range(1, 10000):
    sum_digits_list.append(sum_digits(n))


self_number_list = [x for x in ten_thousand_list if x not in sum_digits_list]

for i in self_number_list:
    print(i)


# 셀프넘버가 아닌 숫자들의 식을 함수로
# 입력받은 수 + 모든 자리수 합
# 함수 리턴 값으로 나온 숫자들을 리스트로 저장 = 셀프 넘버가 아닌 숫자들의 리스트
# 1부터 10000까지의 리스트
# (1부터 10000까지의)리스트를 돌면서 (셀프 넘버가 아닌 숫자들의)리스트에 없는 숫자들만 리스트로 저장
# = (1부터 10000까지의)리스트 - (셀프 넘버가 아닌 숫자들의)리스트
# = 셀프 넘버들이 담긴 리스트
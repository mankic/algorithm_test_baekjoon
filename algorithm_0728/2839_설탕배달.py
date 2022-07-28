# def delivery_sugar(n):
#     pack_5kg = n // 5
#     pack_5kg_remainder = n % 5
#     pack_3kg = n // 3
#     if pack_5kg_remainder == 0:
#         return print(pack_5kg)
#     elif (pack_5kg_remainder != 0) and (pack_5kg_remainder % 3) == 0:
#         pack_3kg = pack_5kg_remainder // 3
#         return print(pack_5kg + pack_3kg)
#     elif (pack_5kg_remainder != 0) and ((n % 3) == 0):
#         return print(pack_3kg)
#     else:
#         return print(-1)
#
#
# n = int(input())
# delivery_sugar(n)


# sugar 변수가 5의 배수가 아닐 때에는 5의 배수가 될 때까지 3을 빼고 bag의 개수는 1을 더한다.
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)
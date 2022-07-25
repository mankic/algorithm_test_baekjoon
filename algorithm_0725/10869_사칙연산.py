def four_fundamental_arithmetic_operations(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(round(a / b))
    print(a % b)


a, b = map(int, input().split())
four_fundamental_arithmetic_operations(a, b)
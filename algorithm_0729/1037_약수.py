def measure(n):
    measure_list = list(map(int, input().split()))
    num = min(measure_list) * max(measure_list)
    return print(num)


n = int(input())
measure(n)
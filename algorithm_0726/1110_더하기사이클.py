def plus_cycle(n):
    if len(n) == 1:
        n = n.zfill(2)

    units = n[1]
    tens = n[0]
    new_n = '0'
    count = 0

    while new_n != n:
        sum_n = int(tens) + int(units)
        sum_n = str(sum_n)

        if len(sum_n) == 1:
            sum_n = sum_n.zfill(2)

        new_n = units + sum_n[1]

        units = new_n[1]
        tens = new_n[0]
        count += 1

    print(count)

n = input()
plus_cycle(n)
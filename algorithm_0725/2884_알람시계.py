def alarm_time(h, m):
    m = m - 45

    if m < 0:
        m = 60 + m
        if h == 0:
            h = 23
        else:
            h = h - 1

        print(h, m)


h, m = map(int,input().split())
alarm_time(h, m)
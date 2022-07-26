def over_average(c):
    for i in range(c):
        score_list = list(map(int,input().split()))
        avg = sum(score_list[1:])/score_list[0]
        count = 0

        for score in score_list[1:]:
            if score > avg:
                count += 1
        over_average_per = (count/score_list[0])*100
        print(f'{over_average_per:.3f}%')

c = int(input())
over_average(c)

# map() 함수로 input 받으면 입력되는 만큼 매칭
# list() 리스트 형태로 저장
# [:] 리스트 슬라이스
# f string 에서 소수점 표현
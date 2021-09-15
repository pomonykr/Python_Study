# 문제 설명
# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

# 입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

# week = {'SUN': '0', 'MON': '1', 'TUE': '2',
#         'WED': '3', 'THU': '4', 'FRI': '5', 'SAT': '6'}
# day_in_month = {'a':'1','a':'2'}
# week_in_day = {'1':'FRI','2':'SAT','3'}
# week_in_day = {'1':'FRI','2':'SAT','3'}
# 지석의 원포인트 꿀팁 = '달력을켜라 1월1일이 금요일이란것이 중요 , 2월을 검색하는데 31, 32 , 33 , 34가 되면 수요일이된다 , 다 더해서 생각해봐'


def solution(a, b):
    sum = 0
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month_day in range(a):
        month_days[month_day]
        sum += month_days[month_day]
    if (sum+b) % 7 == 0:
        return 'THU'
    if (sum+b) % 7 == 1:
        return 'FRI'
    if (sum+b) % 7 == 2:
        return 'SAT'
    if (sum+b) % 7 == 3:
        return 'SUN'
    if (sum+b) % 7 == 4:
        return 'MON'
    if (sum+b) % 7 == 5:
        return 'TUE'
    if (sum+b) % 7 == 6:
        return 'WED'

    return 0


a = 12
b = 30

print(solution(a, b))

# 문제 설명
# 어떤 정수들이 있습니다.
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
# absolutes	signs	result
# [4,7,12]	[true,false,true]	9
# [1,2,3]	[false,false,true]	0


def solution(absolutes):

    result = 0
    for i in range(len(absolutes)):
        if signs[i]:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    return result


absolutes = [100, 200, 300, 400, 500]
signs = [True, False, True, False, True]

print(solution(absolutes))

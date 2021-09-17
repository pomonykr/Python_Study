# 문제 설명
# 0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 수 ≤ 9
# numbers의 모든 수는 서로 다릅니다.


def solution(numbers):
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_1 = []
    answer = 0
    for i in index:
        if i not in numbers:
            list_1.append(i)
    print(list_1)
    for j in list_1:
        answer = answer + j
    return answer


numbers = [3, 2, 1, 4, 5, 6]
print(solution(numbers))

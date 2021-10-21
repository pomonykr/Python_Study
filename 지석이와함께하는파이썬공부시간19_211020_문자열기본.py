'''
def solution(s):
    answer = 0
    for i in s:
        try:
            answer += int(i)
        except:
            return False
    if answer % 1 == 0:
        return True
        '''
/


def solution(s):
    if (len(s) == 4 or 6) and s.isdigit():
        return True
    else:
        return False

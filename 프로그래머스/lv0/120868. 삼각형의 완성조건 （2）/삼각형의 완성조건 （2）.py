def solution(sides):
    answer = 0
    sides.sort(reverse=True)
    # side 수 중에서 가장 긴 변이 있는 경우
    # sides[0] - sides[1] < x =< sides[0] 
    for k in range(sides[0] - sides[1] + 1, sides[0]+1):
        answer += 1
    # 새로운 값이 가장 긴 변이 되는 경우
    # x < sides[0] + sides[1] && x > sides[0]
    for i in range(sides[0]+1, sides[0] + sides[1]):
        answer += 1
    return answer
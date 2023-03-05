def solution(sides):
    answer = 2
    sides.sort(reverse=True)
    if sides[0] < sum(sides[1:3]):
        answer = 1
    return answer
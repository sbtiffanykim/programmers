def solution(a, d, included):
    answer = sum([a + idx*d for idx, boo in enumerate(included) if boo])
    return answer
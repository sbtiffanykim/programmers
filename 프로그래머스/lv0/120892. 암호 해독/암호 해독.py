def solution(cipher, code):
    answer = [char for idx, char in enumerate(cipher, start=1) if idx % code == 0]
    answer = ''.join(answer)
    return answer
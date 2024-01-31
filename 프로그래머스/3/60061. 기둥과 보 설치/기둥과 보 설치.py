def possible(arr):
    for x, y, t in arr:
        if t == 0:  # 기둥인 경우
            # 조건에 맞으면 넘김
            if y == 0 or [x - 1, y, 1] in arr or [x, y, 1] in arr or [x, y - 1, 0] in arr:
                continue
            return False   # 아니면 false 반환
        else:  # 보인 경우
            # 조건에 맞으면 넘김
            if [x, y - 1, 0] in arr or [x + 1, y - 1, 0] in arr or ([x - 1, y, 1] in arr and [x + 1, y, 1] in arr):
                continue
            return False  # 아니면 false 반환
    return True


def solution(n, build_frame):
    answer = []
    for x, y, t, op in build_frame:
        if op == 0:  # 삭제
            answer.remove([x, y, t])  # 일단 삭제
            if not possible(answer):  # 삭제하면 안되는 경우
                answer.append([x, y, t])  # 다시 설치
        else:  # 설치
            answer.append([x, y, t])  # 일단 설치
            if not possible(answer):  # 설치가 불가능한 경우
                answer.remove([x, y, t])  # 지우기

    return sorted(answer)

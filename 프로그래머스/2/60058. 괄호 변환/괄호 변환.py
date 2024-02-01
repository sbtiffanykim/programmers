# 균형잡힌 괄호 문자열의 마지막 인덱스를 반환하는 함수
def balanced_index(p):
    opened_cnt = 0  # 열린 괄호의 개수 저장
    for i in range(len(p)):
        if p[i] == "(":
            opened_cnt += 1
        else:
            opened_cnt -= 1
        if opened_cnt == 0:  # 균형잡힌 괄호 문자열인 경우
            return i  # 마지막 인덱스 반환


# 올바른 문자열인지 확인하는 함수
def check_proper_str(p):
    opened_cnt = 0  # 열린 괄호의 개수 저장
    for c in p:
        if c == "(":
            opened_cnt += 1
        else:
            if opened_cnt == 0:  # 올바른 문자열이 아닌 경우
                return False
            opened_cnt -= 1
        return True  # 올바른 문자열인 경우


def solution(p):
    answer = ""
    if p == "":  # 1
        return answer
    else:
        # 2
        idx = balanced_index(p)
        u = p[: idx + 1]
        v = p[idx + 1 :]
        if check_proper_str(u):  # 3
            answer += u + solution(v)
        else:  # 4
            answer += "("  # 4-1
            answer += solution(v)  # 4-2
            answer += ")"  # 4-3
            u = list(u[1:-1])
            for i in range(len(u)):
                if u[i] == "(":
                    u[i] = ")"
                elif u[i] == ")":
                    u[i] = "("
            answer += "".join(u)

    return answer
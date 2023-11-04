def solution(s):
    answer = []
    dic = dict()  # 숫자와 등장 횟수 저장할 dict
    s = s.replace('{', '').replace('}', '').split(',') # 숫자만 남기기
    # 숫자별로 dict에 등장 횟수 저장
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    # 가장 많이 등장하는 숫자 순서대로 정렬
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for k, v in dic:
        answer.append(int(k))

    return answer
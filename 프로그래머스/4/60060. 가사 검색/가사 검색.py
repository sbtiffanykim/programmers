from bisect import bisect_left, bisect_right

# aa-zz사이에 몇개의 단어가 있는 지 확인하는 함수
def count_by_range(a, left_val, right_val):
    left_idx = bisect_left(a, left_val)
    right_idx = bisect_right(a, right_val)
    return right_idx - left_idx

def solution(words, queries):
    answer = []

    arr = [[] for _ in range(10001)]  # 길이별로 word 나누기 위한 리스트
    reversed_arr = [[] for _ in range(10001)]  # 뒤집어서도 저장
    
    for word in words:
        i = len(word)
        arr[i].append(word)
        reversed_arr[i].append(word[::-1])

    for i in range(1, 10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for q in queries:  # 쿼리별로 확인
        res = 0
        if q[0] == "?":  # ?로 시작되는 키워드
            res = count_by_range(reversed_arr[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z"))
        else:
            res = count_by_range(arr[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        answer.append(res)

    return answer

def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        try:
            answer.append(min([n for n in arr[s:e+1] if n > k]))
        except:
            answer.append(-1)
    return answer
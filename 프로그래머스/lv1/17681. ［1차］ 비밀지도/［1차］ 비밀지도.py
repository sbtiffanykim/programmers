def solution(n, arr1, arr2):
    answer = []

    for v1, v2 in zip(arr1, arr2):
        map = format((v1 | v2), 'b').zfill(n)
        map = map.replace('1', '#')
        map = map.replace('0', ' ')
        answer.append(map)

    return answer
def solution(elements):
    sums = []
    n = len(elements)

    for k in range(1, n+1):
        for i in range(n):
            end = i + k
            if end >= n:
                sums.append(sum(elements[i:])+sum(elements[:end % n]))
            else:
                sums.append(sum(elements[i:end]))
    return len(set(sums))
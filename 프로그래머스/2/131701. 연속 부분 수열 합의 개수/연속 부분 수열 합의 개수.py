def solution(elements):
    n = len(elements)
    sums = set()
    
    for i in range(n):
        num = elements[i]
        sums.add(num)
        for j in range(i+1, i+n):
            num += elements[j%n]
            sums.add(num)
    
    return len(sums)
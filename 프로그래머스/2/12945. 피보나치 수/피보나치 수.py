a = {0:0, 1:1}
for n in range(2, 100001):
    a[n] = a[n-1] + a[n-2]

def solution(n):
    answer = a[n] % 1234567
    return answer
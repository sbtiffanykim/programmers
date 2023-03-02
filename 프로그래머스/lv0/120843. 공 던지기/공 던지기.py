def solution(numbers, k):
    pos = 2*(k-1) % len(numbers)
    answer = numbers[pos]
    return answer
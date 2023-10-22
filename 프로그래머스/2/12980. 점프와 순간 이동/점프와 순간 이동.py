def solution(n):
    ans = 0  # 이동하기 위해서는 일단 1까지는 가야함
    
    if n != 1:
        while n >= 1:
            if n % 2 != 0:
                ans += 1
            n //= 2
    else:
        ans += 1            

    return ans
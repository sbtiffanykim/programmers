def solution(nums):
    N = len(nums) // 2
    nums = set(nums)
    
    if N > len(nums): return len(nums)
    else: return N
def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    zeroes = 0
    
    zeroes = lottos.count(0)
    nums = len([n for n in lottos if n in win_nums])
    
    return [rank[zeroes+nums], rank[nums]]
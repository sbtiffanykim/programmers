def solution(score):
    rank = sorted([sum(s)/2 for s in score], reverse = True)
    rank_dict = dict()
    
    for i, v in enumerate(rank):
        if v not in rank_dict.keys():
            rank_dict[v] = i + 1
    
    return [rank_dict[sum(s) / 2] for s in score]
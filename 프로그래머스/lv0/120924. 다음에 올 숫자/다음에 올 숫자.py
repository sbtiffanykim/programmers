def solution(common):
    diff = common[1] - common[0]
    if common[1] + diff == common[2]: # 등차
        return common[-1] + diff
    else: # 등비
        return common[-1] * (common[1] // common[0])
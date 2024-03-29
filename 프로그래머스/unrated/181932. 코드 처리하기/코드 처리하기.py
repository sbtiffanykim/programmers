def solution(code):
    ret = ''
    mode = 0
    
    for idx, c in enumerate(code):
        if mode == 0:
            if c == '1':
                mode = 1
            elif c != '1' and idx % 2 == 0:
                ret += c
        else:
            if c == '1':
                mode = 0
            elif c != '1' and idx % 2 != 0:
                ret += c
    
    if len(ret) == 0: return "EMPTY"
    return ret
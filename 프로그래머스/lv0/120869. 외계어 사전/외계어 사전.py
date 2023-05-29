def solution(spell, dic):
    answer = 2
    
    for word in dic:
        cnt_list = list(map(lambda x: word.count(x), spell))
        if set(cnt_list) == {1}:
            return 1

    return answer
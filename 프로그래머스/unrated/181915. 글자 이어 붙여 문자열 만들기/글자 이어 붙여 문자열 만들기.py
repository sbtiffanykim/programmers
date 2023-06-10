def solution(my_string, index_list):
    return ''.join(list(map(lambda x: my_string[x], index_list)))
import re

def solution(str1, str2):
    res = re.findall(str2, str1)
    return 2 if len(res) == 0 else 1
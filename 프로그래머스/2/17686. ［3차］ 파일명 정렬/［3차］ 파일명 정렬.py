import re

def solution(files):
    dic = dict()
    for idx, file in enumerate(files):
        t = re.match('(\D+)(\d{1,5})(.*)', file)
        head = t.group(1).lower()
        number = int(t.group(2))
        dic[file] = (head, number, idx)
    
    new_dict = dict(sorted(dic.items(), key=lambda x: (x[1][0], x[1][1], x[1][2])))
    answer = [title for title, _ in new_dict.items()]
    return answer
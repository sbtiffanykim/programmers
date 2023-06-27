import re

def solution(dartResult):
    bonus_num = {'S': 1, 'D': 2, 'T': 3}
    option_num = {'*': 2, '#': -1, '': 1}
    scores = [0] * 3
    sets = re.findall('([\d]{1,2}[S|D|T][#|*]?)', dartResult)
    
    for idx, s in enumerate(sets):
        score = re.search('\d{1,2}', s).group()
        bonus = re.search('[S|D|T]', s).group()
        try:
            option = re.search('[*|#]', s).group()
        except:
            option = ''
                
        scores[idx] = int(score) ** bonus_num[bonus]
        if idx == 0:
            scores[0] = scores[0] * option_num[option]
        else:
            if option == '*':
                scores[idx-1] *= option_num[option]
            scores[idx] *= option_num[option]
    
    return sum(scores)
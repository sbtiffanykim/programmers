import operator

def solution(quiz):
    answer = []
    for q in quiz:
        a = q.split(' ') 
        if a[1] == "+":
            if int(a[4]) == operator.add(int(a[0]), int(a[2])): answer.append("O")
            else: answer.append("X")
        else:
            if int(a[4]) == operator.sub(int(a[0]), int(a[2])): answer.append("O")
            else: answer.append("X")
    return answer
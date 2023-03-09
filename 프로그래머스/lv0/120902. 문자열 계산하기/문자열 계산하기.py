import operator

def solution(my_string):
    my_string = my_string.split(' ')
    my_string = my_string[::-1]
    answer = int(my_string.pop())
    
    while len(my_string) > 0:
        print(answer)
        val = my_string.pop()
        try:
            a = int(val)
        except ValueError:
            opr = val
            num = my_string.pop()
            if opr == "+":
                answer += int(num)
            else:
                answer -= int(num)
                            
    return abs(answer)
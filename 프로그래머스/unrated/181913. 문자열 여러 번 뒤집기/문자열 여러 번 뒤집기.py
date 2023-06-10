def solution(my_string, queries):
    for q1, q2 in queries:
        my_string = my_string[:q1] + ''.join(reversed(my_string[q1:q2+1])) + my_string[q2+1:]
    return my_string
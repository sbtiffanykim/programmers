def solution(my_string, num1, num2):
    sn = min(num1, num2)
    ln = max(num1, num2)
    
    answer = my_string[:sn] + my_string[ln] + my_string[sn+1:ln] + my_string[sn] + my_string[ln+1:]
    
    return answer
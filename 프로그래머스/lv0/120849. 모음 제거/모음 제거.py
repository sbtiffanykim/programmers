def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in my_string:
        if char in vowels:
            pass
        else:
            answer += char
    return answer
def get_coordinate(n, keypads):
    idx = [(i, j) for i in range(4) for j in range(3) if keypads[i][j] == n]
    return idx[0]

def solution(numbers, hand):
    answer = ''
    left_only = [1, 4, 7]
    right_only = [3, 6, 9]
    both = [2, 5, 8, 0]
    keypads = [[1,2,3], [4,5,6], [7,8,9], [11,0,12]]   
    
    cur_right = 12
    cur_left = 11
    
    for n in numbers:
        if n in left_only:
            cur_left = n
            answer += 'L'
        elif n in right_only:
            cur_right = n
            answer += 'R'
        else:
            
            l_idx = get_coordinate(cur_left, keypads)
            r_idx = get_coordinate(cur_right, keypads)
            cur_idx = (both.index(n), 1)
            l_dist = abs(l_idx[0] - cur_idx[0]) + abs(l_idx[1] - cur_idx[1])
            r_dist = abs(r_idx[0] - cur_idx[0]) + abs(r_idx[1] - cur_idx[1])
                       
            if l_dist < r_dist: 
                cur_left = n
                answer += 'L'
            elif l_dist > r_dist:
                cur_right = n
                answer += 'R'
            else:
                if hand == 'right':
                    cur_right = n
                    answer += 'R'
                else:
                    cur_left = n
                    answer += 'L'
    
    return answer
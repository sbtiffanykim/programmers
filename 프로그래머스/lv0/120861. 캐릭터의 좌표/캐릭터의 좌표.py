def solution(keyinput, board):
#   -+ board[0] // 2 , -+ board[1] // 2 초과 시 => 이동 불가
    w_max = board[0] // 2
    h_max = board[1] // 2
    x, y = 0, 0
    
    for k in keyinput:
        if k == "left" and -w_max < x <= w_max: x -= 1
        elif k == "right" and -w_max <= x < w_max: x += 1
        elif k == "down" and -h_max < y <= h_max: y -= 1
        elif k == "up" and -h_max <= y < h_max: y += 1
    
    return [x, y]
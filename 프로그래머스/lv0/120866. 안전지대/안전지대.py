def solution(board):
    answer = 0
    hazard_range = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    hazards = []
    
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                for h in hazard_range:
                    temp = [a+b for a, b in zip([x,y], h)]
                    if (0 <= temp[0] < len(board)) and (0 <= temp[1] < len(board)) and (temp not in hazards):
                        hazards.append(temp)
                if [x,y] not in hazards:
                    hazards.append([x,y])

    answer = (len(board) ** 2) - len(hazards)
    return answer
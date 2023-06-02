def solution(lines):
    answer = 0
    table = [set([]) for _ in range(200)]

    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index)

    for line in table:
        if len(line) > 1:
            answer += 1

    return answer
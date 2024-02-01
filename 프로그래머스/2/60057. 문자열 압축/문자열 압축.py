def compress(s, l):
    tmp = [s[idx : idx + l] for idx in range(0, len(s), l)]
    div_string = ""
    prev, nxt, cnt = 0, 1, 1
    while True:
        if tmp[prev] == tmp[nxt]:
            cnt += 1
            nxt += 1
        else:
            if cnt != 1:
                div_string += str(cnt)
            div_string += tmp[prev]
            cnt = 1
            prev = nxt
            nxt += 1
        if nxt >= len(tmp):
            break

    if cnt != 1:
        div_string += str(cnt)
    div_string += tmp[prev]

    return len(div_string)

def solution(s):
    shortest = len(s)
    if shortest == 1:
        return 1
    else:
        for i in range(1, len(s)):
            shortest = min(shortest, compress(s, i))
        return shortest
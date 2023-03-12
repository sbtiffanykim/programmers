def solution(dots):
    heights = []
    widths = []
    for d in dots:
        widths.append(d[0])
        heights.append(d[1]) 
    answer = (max(heights) - min(heights)) * (max(widths) - min(widths))
    return answer
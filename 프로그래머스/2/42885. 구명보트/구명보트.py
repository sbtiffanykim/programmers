def solution(people, limit):
    answer = 0
    people.sort(reverse=True)  # 무게 내림차순으로 정리
    p1, p2 = 0, len(people) - 1  # 비교 위해 맨 앞, 맨 끝에 index 두기
    
    while True:
        # 제일 가벼운 사람과 무거운 사람의 합이 무게제한보다 크면        
        if people[p1] + people[p2] > limit:
            p1 += 1  # 무거운 사람만 탈출
        # 아니면 둘 다 탈출
        else:
            p1 += 1
            p2 -= 1
        answer += 1  # 탈출횟수 증가

        if p1 > p2:  # 인덱스 순서 바뀌면 탈출 끝남
            break
    
    return answer
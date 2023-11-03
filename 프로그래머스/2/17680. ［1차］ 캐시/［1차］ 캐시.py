from collections import deque

def calc_exec_time(cache, cacheSize, city):
    if cacheSize == 0:
        return cache, 5
    # cacheHit
    if city in cache:
        cache.remove(city)
        cache.appendleft(city)
        return cache, 1
    # cacheMiss
    else:
        if len(cache) == cacheSize:
            cache.pop()
        cache.appendleft(city)
        return cache, 5

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    for city in cities:
        cache, time = calc_exec_time(cache, cacheSize, city.lower())
        answer += time
        
    return answer
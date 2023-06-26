def solution(N, stages):
    failure_rate = {i: 0 for i in range(1, N+1)}
    
    for n in range(1, N+1):
        clear, not_clear = 0, 0
        not_clear = len([s for s in stages if s == n])
        clear = len([s for s in stages if s >= n])
        
        if clear != 0:
            failure_rate[n] = (not_clear / clear)
    
    failure_rate = dict(sorted(failure_rate.items(), key=lambda x: x[1], reverse=True))
    
    return list(failure_rate.keys())
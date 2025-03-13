def solution(bridge_length, weight, truck_weights):
    from collections import deque
    bridge = deque([0 for _ in range(bridge_length)])
    answer = 0
    dq = deque(truck_weights)
    bridge_sum = sum(bridge)
    while bridge :
        answer += 1
        bridge_sum -= bridge.popleft()
        
        if dq :
            if bridge_sum + dq[0] <= weight :
                bridge.append(dq.popleft())
                bridge_sum += bridge[-1]
            else :
                bridge.append(0)

    return answer
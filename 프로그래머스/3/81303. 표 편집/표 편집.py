def solution(n, k, cmd):
    deleted = []
    
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+2)]
    
    k+=1
    
    for cmd_i in cmd:
        if cmd_i.startswith('C'):
            # linked list
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            deleted.append(k)
            k = down[k] if down[k] <= n else up[k]
                 
        elif cmd_i.startswith('Z'):
            restore = deleted.pop()     
            up[down[restore]] = restore
            down[up[restore]] = restore
                 
        else:
            op, num = cmd_i.split()
            for _ in range(int(num)):
                k = up[k] if op == 'U' else down[k]
                    
                    
    answer = ['O'] * n
    for i in deleted :
        answer[i-1] = 'X'
    return ''.join(answer)
        
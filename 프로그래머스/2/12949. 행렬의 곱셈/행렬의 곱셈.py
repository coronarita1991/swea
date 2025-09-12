def solution(arr1, arr2):
    answer = [[0]* len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[0])):
                # print(i, j, k)
                tmp += arr1[i][k] * arr2[k][j]
                # print(arr1[i][j] , arr2[j][k])
                
            answer[i][j] = tmp
            
    return answer
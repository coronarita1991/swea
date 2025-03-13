def solution(board, moves):
    
    # board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    # moves = [1,5,3,5,1,2,1,4]
    
    answer = []   
    # 세로방향으로 0이 아닌 값[인형의 존재] 탐지     
    basket = []
       
    for j in moves : 
        for i in range(len(board)) :
            # index : j-1 
            if board[i][j-1] != 0 :
                basket.append(board[i][j-1])
                board[i][j-1] = 0
                if basket[-1:] == basket[-2:-1]:
                    answer += basket[-1:]
                    basket = basket[:-2]              
                break

    
    return len(answer) * 2

    # result = 4 (= answer)
    # 새롬 : 바구니 - 스택으로 !
    # 마지막, 이전값 비교해서 제거 ! 
    # 1. 길이 > 1,
    # 2. 맨마지막과, -1, -2값 2개 값비교
    # 같으면 pop ~ (둘다 제거)
    
    
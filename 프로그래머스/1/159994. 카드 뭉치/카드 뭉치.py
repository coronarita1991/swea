def solution(cards1, cards2, goal):
    answer = ''
    # 순서가 중요하다. 
    p1, p2 = 0, 0
    for word in goal :
        # p1, p2 둘 중에서 가능하면 포인터 갱신
        if p1 < len(cards1) and cards1[p1] == word : 
            p1 += 1
        elif p2 < len(cards2) and cards2[p2] == word :
            p2 += 1
        
        else : 
            return "No"
    return "Yes"
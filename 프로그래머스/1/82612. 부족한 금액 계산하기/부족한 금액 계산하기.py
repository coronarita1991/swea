def solution(price, money, count):
    # N번째 이용 시 N배 요금
    for i in range(1, count+1):
        money -= price * i
    
    return abs(money) if money < 0 else 0
def solution(numbers):
    answer = set()
    for idx1, num1 in enumerate(numbers):
        for idx2, num2 in enumerate(numbers):
            if idx1 == idx2 : 
                continue
            answer.add(num1+num2)
    return sorted(list(answer))
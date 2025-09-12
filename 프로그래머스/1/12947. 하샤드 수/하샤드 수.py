def solution(x):
    
    def calculate_nums(n):
        n = str(n)
        return sum(int(i) for i in n)
    
    def is_hashad_num(n, cn):
        return n % cn == 0
    
    return is_hashad_num(x, calculate_nums(x))
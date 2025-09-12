def solution(arr):
    answer = []
    m = min(arr)
    arr.remove(m)
    return arr if arr else [-1]
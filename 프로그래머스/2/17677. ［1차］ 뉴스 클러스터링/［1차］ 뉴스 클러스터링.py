import re
from collections import Counter

def parse(string):
    res = [
        string[i:i+2].lower()
        for i in range(len(string) - 1)
        if re.findall('[a-z]{2}', string[i:i+2].lower())
    ]
    return res

def solution(str1, str2):
    answer=0
    
    str1, str2 = parse(str1), parse(str2)
    print(str1, str2)
    # 집합 
    intersection = sum((Counter(str1) & Counter(str2)).values())
    union = sum((Counter(str1) | Counter(str2)).values())
    
    if union==0 : 
        return 1 * 65536
    
    return int(intersection/union *65536)
    
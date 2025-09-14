def solution(s):
    answer = 0
    def inspect_bracket(w):
        stack = []
        for br in w : 
            if br in ('[', '{', '('):
                stack.append(br)
            
            else :
                if not stack :
                    return False
                elif stack : 
                    if br == ']' and stack[-1] == '[':
                        stack.pop()
                    elif br == '}' and stack[-1] == '{':
                        stack.pop()
                    elif br == ')' and stack[-1] == '(':
                        stack.pop() 
            # print(stack)  
        return True if not stack else False
    
    for i in range(len(s)):
        s = s[1:] + s[0]
        if inspect_bracket(s):
            answer += 1
    return answer
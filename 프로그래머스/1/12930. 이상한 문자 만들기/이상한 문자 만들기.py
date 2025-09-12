def solution(s):
    result = []
    for word in s.split(' '):
        new_word = ''
        for idx,w in enumerate(word):
            if idx%2 ==0 : new_word += w.upper()
            else : new_word += w.lower()
        result.append(new_word)
    return ' '.join(result)
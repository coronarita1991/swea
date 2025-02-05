from collections import deque

def solution(begin, target, words):

    # 단어 변환 
    # '한번에 한 개의 알파벳 바꾸고' / words에 있는 단어로 가능 
    # 최소 몇 단계에 걸처 target 변환 가능한지 ?
    
    # hit - hot - dot - dog - cog 
    # 각 단어 길이는 10 이하 소문자로 구성
    
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = {begin: 0}
    
    while queue:
        current_word, steps = queue.popleft()

        if current_word == target:
            return steps  # 시작 단어 포함

        for word in words:
            # 1글자 차이 검증
            diff = sum(c1 != c2 for c1, c2 in zip(current_word, word))

            if diff == 1 and word not in visited:
                visited[word] = steps + 1
                queue.append((word, steps + 1))

    return 0
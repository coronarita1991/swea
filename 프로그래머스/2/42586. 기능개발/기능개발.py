import math

def solution(progresses, speeds):
    # 각 기능이 며칠 후에 100%가 되는지 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    stack = []  # 각 원소: [배포기준일, 기능수]
    for d in days:
        if not stack:
            # 스택이 비었다면 새 배포 그룹 시작
            stack.append([d, 1])
        else:
            # 스택 top 확인
            if d <= stack[-1][0]:
                # top의 기준일 이하이면 같은 그룹에 포함
                stack[-1][1] += 1
            else:
                # 더 오래 걸리므로 새로운 배포 그룹으로 시작
                stack.append([d, 1])
    
    # 스택에 쌓인 각 그룹의 기능수를 순서대로 꺼내서 결과 반환
    return [group[1] for group in stack]
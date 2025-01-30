'''
3 4 - N, M
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
N개의 줄, M개의 줄에 입력받고, 교집합의 크기, 원소를 사전순으로 도출
'''
N, M = map(int, input().split())

n_group = set([input() for _ in range(N)])
m_group = set([input() for _ in range(M)])

common_group = n_group & m_group

print(len(common_group))

cl = sorted(list(common_group))

for elem in cl:
    print(elem)

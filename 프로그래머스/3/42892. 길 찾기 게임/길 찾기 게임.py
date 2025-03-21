import sys
sys.setrecursionlimit(10**6)

def VLR_LRV(node, subtree, answer1, answer2):
    # VLR
    answer1.append(node[0])
    
    # leftsubtree, right subtree 구하기 (x 기반)
    leftsubtree = [_node for _node in subtree if _node[1] < node[1] and _node[2] < node[2]] 
    rightsubtree = [_node for _node in subtree if _node[1] > node[1] and _node[2] < node[2]] 
    
    if leftsubtree !=[] :
        VLR_LRV(leftsubtree[0], leftsubtree, answer1, answer2)
    if rightsubtree !=[] :
        VLR_LRV(rightsubtree[0], rightsubtree, answer1, answer2)    
    answer2.append(node[0])    

def solution(nodeinfo):
    #nodeinfo에 해당 번호를 넣고, 정렬시키기
    nodeinfo = [[i+1]+nodeinfo[i] for i in range(len(nodeinfo))]
    nodeinfo.sort(key=lambda x:(-x[2], x[1]))
    
    answer = [[], []]
    VLR_LRV(nodeinfo[0], nodeinfo, answer[0], answer[1])
    
    return answer
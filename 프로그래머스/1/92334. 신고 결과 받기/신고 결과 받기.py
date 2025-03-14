from collections import defaultdict
def solution(id_list, report, k):
    
    id_dict:dict[(str, int)] = defaultdict()
    reported_dict:dict[(str, int)] = defaultdict()
    report_list_dict:dict[(str, set)] = defaultdict(set)
    
    for id in id_list:
        id_dict[id] = 0
        reported_dict[id] = 0
        
    for s in report:
        id, reported_id = s.split()
        if reported_id not in report_list_dict[id]:
            report_list_dict[id].add(reported_id)
            reported_dict[reported_id] += 1
        
    # k회 이상
    # print(report_list_dict, reported_dict)
    rep_list = []
    for reported_id, val in reported_dict.items():
        if val >= k:
            rep_list.append(reported_id)
    
    for id, indiv_list in report_list_dict.items():
        for user in rep_list:
            if user in indiv_list:
                id_dict[id]+=1
    
    result = []
    for id in id_list:
        result.append(id_dict[id])
    
    return result
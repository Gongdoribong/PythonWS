def solution(id_list, report, k):
    
    members = len(id_list)
    result = [0]*members
    cnt_report = [[0]*members for _ in range(members)]
    temp_report = []

    for i in range(len(report)):
        temp_report.append(report[i].split(" "))
        x, y = temp_report[i]
        cnt_report[id_list.index(x)][id_list.index(y)] = 1

    for i in range(members):
        cnt = []
        for j in range(members):
            if(cnt_report[j][i] == 1):
                cnt.append(j)
        if(len(cnt) >= k):
            for t in range(len(cnt)):
                result[cnt[t]] += 1
                
    return result
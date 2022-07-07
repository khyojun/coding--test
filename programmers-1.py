def solution(id_list, report, k):
    answer = []
    report= set(report) # 중복 제거
    report= list(report)
    report_right=[0]*len(id_list)
    answer_find=[]
    sued_people=[]

    for i in range(len(report)):
        tmp=report[i].split(' ')
        sued_people.append(tmp[1])

    for i in range(len(id_list)):
        if sued_people.count(id_list[i])>=k:
            report_right[i]=id_list[i]

    for i in range(len(report)):
        tmp=report[i].split(' ')
        if report_right.count(tmp[1])==1:
            answer_find.append(tmp[0])
    for i in range(len(id_list)):
        answer.append(answer_find.count(id_list[i]))



    return answer
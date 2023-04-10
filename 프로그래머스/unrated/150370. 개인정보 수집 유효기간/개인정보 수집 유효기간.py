def solution(today, terms, privacies):
    answer = []
    now_y, now_m, now_d = today.split(".")

    now_y=int(now_y)
    now_m=int(now_m)
    now_d=int(now_d)

    dict={}

    for i in range(len(terms)):
        idx, val=terms[i].split(" ")
        dict[idx] = int(val)

    real_result=[]
    for i in range(len(privacies)):
        date, terms_alp= privacies[i].split(" ")
        pri_y, pri_m, pri_d = date.split(".")
        pri_y=int(pri_y)
        pri_m=int(pri_m)
        pri_d=int(pri_d)
        result_m=dict[terms_alp]+ int(pri_m)
        plus_year=0
        if(result_m>12):
            plus_year=result_m//12
            result_m=result_m%12
        pri_y=plus_year+int(pri_y)

        real_valid_y=pri_y
        real_valid_m=result_m
        real_valid_d=pri_d-1
        if(real_valid_d<=0):
            real_valid_d=28
            real_valid_m=real_valid_m-1
        if(real_valid_m==0):
            real_valid_m=12
            real_valid_y=real_valid_y-1


        if(now_y > real_valid_y):
            real_result.append(i+1)
            continue
        if(now_y== real_valid_y and now_m > real_valid_m):
            real_result.append(i+1)
            continue
        if((now_y== real_valid_y and now_m == real_valid_m) and now_d > real_valid_d):
            real_result.append(i+1)
            continue
            

    
    return real_result
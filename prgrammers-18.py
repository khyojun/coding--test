def solution(array, commands): # k번째수
    answer = []
    for i in commands:
        arr_=array[(i[0]-1):i[1]]
        arr_.sort()
        answer.append(arr_[i[2]-1])
    return answer
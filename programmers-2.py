def solution(s):
    answer = 0
    find_num=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(find_num)):
        s=s.replace(find_num[i], str(i))
    answer =int(s) 
    
    return answer
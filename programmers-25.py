def solution(a, b): # 2016년
    month=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
    Days=['FRI', 'SAT',  'SUN', 'MON', "TUE", "WED", 'THU']
    answer = ''
    now_day=sum(month[0:(a-1)])+b        
    answer=Days[now_day%7-1]
    return answer
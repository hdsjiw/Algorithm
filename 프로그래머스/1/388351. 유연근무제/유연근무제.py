def time_change(time):
    if time%100>=60:
        time+=100
        time-=60
    return time

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(timelogs)):
        late=False
        
        for j in range(len(timelogs[0])):
            day = (startday + j - 1) % 7 + 1
            # 토요일(6), 일요일(7) 제외
            if day == 6 or day == 7:
                continue
                
            timelog=timelogs[i][j]
            schedule=time_change(schedules[i]+10)
            
            if timelog>schedule:
                late=True
                break
                
        if late==False:
            answer+=1
    return answer
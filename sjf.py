def read(n,p):
    n = int(input("Enter the total no of processes: "))
    for i in range(0,n):
        p.append([])
        p[i].append(input('Enter p_name: '))  
        p[i].append(int(input('Enter p_arrival: '))) 
        p[i].append(int(input('Enter p_bust: ')))     
        p[i].append(0)    
        p[i].append(0)    
        print (' ')
    return n,p

def add_process_in_running(p,running,lastProcessEnding):
    n = len(p)
    if(p[0][1] <= lastProcessEnding):
        running.append(p[0])
        del(p[0])
    else:  
        lastProcessEnding += -lastProcessEnding+p[0][1]
        running.append(p[0])
        del(p[0])
    return  lastProcessEnding

def execute(p,running,complete):
    i=0;    
    n = len(p)   
    lastProcessEnding = 0 
    while i < n:
        lastProcessEnding = add_process_in_running(p,running,lastProcessEnding)
        running[0][3] = lastProcessEnding
        running[0][4] = running[0][3]+running[0][2]
        lastProcessEnding = running[0][4]  
        i+=1   
        complete.append(running[0])
        del(running[0])

def cal_time(n,complete):
    w_time = 0; t_time=0
    for i in range(n):
        w_time += complete[i][3]-complete[i][1]
        t_time += complete[i][4]-complete[i][1]
    return w_time,t_time


def display(n,p):
    print ('ProcessName\tArrivalTime\tBurstTime\tStartTime\tFinalTime')
    for i in range(n):
        print (p[i][0],' ',p[i][1],' ',p[i][2],' ',p[i][3],' ',p[i][4])
    print(' ')

if __name__ == "__main__":
    running = []
    p = []
    complete = []
    total_waitTime = 0
    total_turnAroundTime = 0
    n = 0
    n ,p = read(n, p)    
    p.sort(key = lambda p:p[2]) #first sort by burst time
    p.sort(key = lambda p:p[1]) #then sort by arrival time, as it is inplace so the shortest job with best arrival time is here
    execute(p,running,complete)
    display(n,complete)
    total_waitTime,total_turnAroundTime = cal_time(n,complete)    
    print ('Total waiting time: ',total_waitTime)
    print ('Average waiting time: ',(total_waitTime/n) )
    print ('Total turn around time: ',total_turnAroundTime)
    print ('Average turn around time: ',(total_turnAroundTime/n) )
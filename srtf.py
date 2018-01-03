def read(n,p):
    n = int(input("Enter the total no of processes: "))
    for i in range(0,n):
        p.append([])
        p[i].append(input('Enter process_name: '))  
        p[i].append(int(input('Enter process_arrivalTime: ')))  
        p[i].append(int(input('Enter process_burstTime: ')))  
        p[i].append(0)    
        p[i].append(0)    
        p[i].append(p[i][2])   
        p[i].append(0)  
        print (' ')
    return n,p

def add_process_in_running(p,running,lastProcessEnding):
    p.sort(key = lambda p:p[2]) 
    n = len(p)
    for i in range(n): 
        if p[i][1] <= lastProcessEnding:
            running.append(p[i])
            del(p[i])
            return lastProcessEnding
    lastProcessEnding += p[0][1]-lastProcessEnding
    running.append(p[0])
    del(p[0])
    return lastProcessEnding

def execute_process(p,running,complete):
    p.sort(key = lambda p:p[1])
    i=0; lastProcessEnding = 0
    n = len(p)
    while i<n:
        lastProcessEnding = add_process_in_running(p,running,lastProcessEnding)
        if not running:
            k =3
        else:
            if running[0][6] == 0:
                running[0][3] = lastProcessEnding
                running[0][6] = 1
            running[0][2] -= 1 
            lastProcessEnding += 1
            if running[0][2] <= 0:  
                running[0][4] = lastProcessEnding
                complete.append(running[0])
                del(running[0])
                i += 1 
            else:  
                p.append(running[0])
                del(running[0])
  

def cal_time(n,complete):
    w_time = 0; t_time=0
    for i in range(n):
        w_time += complete[i][4]-complete[i][1]-complete[i][5]
        t_time += complete[i][4]-complete[i][1]
    return w_time,t_time


def display(n,p):
    print ('ProcessName\tArrivalTime\tBurstTime\tStartTime\tFinalTime')
    for i in range(n):
        print (p[i][0],' ',p[i][1],' ',p[i][5],' ',p[i][3],' ',p[i][4])
    print(' ')

if __name__ == "__main__":
    running = []
    p = []
    complete = []
    total_waitTime = 0
    total_turnAroundTime = 0
    n = 0
    n ,p = read(n, p)
    execute_process(p,running,complete)
    display(n,complete)
    total_waitTime,total_turnAroundTime = cal_time(n,complete)    
    print ('Total waiting time: ',total_waitTime)
    print ('Average waiting time: ',(total_waitTime/n) )
    print ('Total turn around time: ',total_turnAroundTime)
    print ('Average turn around time: ',(total_turnAroundTime/n) )

from collections import deque
def display(time,process={},enter=[],que=deque([])):
	i=0
	arr=[]
	while(i<len(enter)):
		if(process.get(enter[i])[0]<=time):
			arr.append(enter[i])
		i=i+1
	i=0
	maximum=-1
	while(i<len(arr)):
		maximum=i
		j=i
		while(j<len(arr)):
			if(process.get(arr[j])[2]>process.get(arr[i])[2]):
				maximum=j
			j=j+1
		if not(maximum==i):
			temp=arr[maximum]
			arr[maximum]=arr[i]
			arr[i]=temp
		i=i+1
	i=0
	while(i<len(arr)):
		enter.remove(arr[i])
		que.append(arr[i])
		i=i+1
	return len(arr)


process={1:[3,3,8],2:[1,6,3],3:[0,6,1],4:[5,2,4],5:[2,7,8]}



key=[1,2,3,4,5]
enter=[1,2,3,4,5]
RQ=[]
Ready=deque([])
time=0
n=5
while(n>0):
	display(time,process,enter,Ready)
	if Ready:
		n=n-1
		element=Ready.popleft()
		time=time+process.get(element)[2]
		j=0
		while j<process.get(element)[2]:
			RQ.append(element)
			j=j+1
		print 'Process Name: ',element,'\t-------->\t Turnaround time= ',time-process.get(element)[0]
	else:
		RQ.append(-1)
		time=time+1
	

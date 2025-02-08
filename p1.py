n=int(input())
l=list(map(int,input().split()))
d={ index:value for index,value in enumerate(l) }
new=[]
minl=min(d.values())



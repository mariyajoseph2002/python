#given an input eg 28 the divisble nos sum should be eql to the same no then return true
n=int(input())
list=[]
for i in range(1,n):
    if n%i==0:
        list.append(i)
s=sum(list)
print(list)
if s==n:
    print(True)
else:
    print( False)

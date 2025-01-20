""" def differenceofSum(n. m)

The function accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n.
 """
""" def calc(m,n):
    sumdiv=0
    sumnot=0
    for i in range(1,m+1):
        if i%n==0:
            sumdiv+=i
        else:
            sumnot+=i
   
    return (sumnot-sumdiv)
n=int(input())
m=int(input())
s=calc(m,n)
print(s)
 """
# acccept a no and find the even and odd nos till that no. return second highest of odd no and second lowest of even no
def calc(arr):
    sumeve=[]
    sumodd=[]
    n=len(arr)
    for i in range(0,n):
        if i%2==0:
            sumeve.append(arr[i])
        else:
            sumodd.append(arr[i])
    sumeve.sort()
    sumodd.sort()
    return (sumeve[-2]+sumodd[1])
n=int(input())
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)

s=calc(arr)
print(s)           

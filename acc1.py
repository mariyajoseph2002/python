""" The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range """
def calc(r,unit,arr,n):
    if n==0:
        return -1
    required=r*unit
    sum=0
    for i in range(0,n):
        sum=sum+arr[i]
        if sum>required:
            break
    if required>=sum:
        return 0
    else:
        return i+1

r=int(input("enter no of rats"))
unit=int(input("amount of food each rat consumes"))
n=int(input("no of houses"))
arr=[]
for i in range(0,n):
    m=int(input("amount of food in house"))
    arr.append(m)
s=calc(r,unit,arr,n)
print(s)


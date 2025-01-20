""" You are given a function,
int findCount(int arr[], int length, int num, int diff);

The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1. """


def find(arr,length,num,diff):
    count=0
    max=num+diff
    min=num-diff
    for i in range(0,length):
        if(abs(arr[i]-num)<=diff):
        
            count+=1
        
    return count
length=int(input())
arr=[]
for i in range(0,length):
    m=int(input())
    arr.append(m)
num=int(input("enter num"))
diff=int(input("enter diff"))
s=find(arr,length,num,diff)
print(s)

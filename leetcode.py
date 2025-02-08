nums=list(map(int,input().split()))
numsn=[]
n=len(nums)
for i in range(0,n):
    sum=0
    for j in range(0,i+1):
        sum=sum+nums[j]
    numsn.append(sum)
print(numsn)
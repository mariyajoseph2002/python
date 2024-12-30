n = int(input())  
list=[] 
for i in range(0,n):
    m=int(input())
    list.append(m)
print("array inserted")
print(list)
st=''
for i in range(0,n):
    digit=list[i]%10

    st=st+str(digit)
print(st)
if int(st)%10==0:
    print("Yes")
else:
    print("No")  
#accets a string and returns a string without repeating characters
strr=input()
st=[]
for i in range(0,len(strr)):
    if strr[i] not in st:
        st.append(strr[i])
    else:
        continue
for i in range(0,len(st)):
    print(st[i],end='')
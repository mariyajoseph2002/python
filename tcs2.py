count=dict()
str=input().split()
for word in str:
    if word.isalpha():
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    else:
        print("invalid")
print(count)
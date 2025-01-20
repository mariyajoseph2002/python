#a list is there find the combinations that can be made by arranging them in different order

def combinations(l,combo_length):
    combs=[]
    for i in range(len(l)):
        curent=l[i]
        remain=l[i+1:n]
        for combo in combinations(remain,combo_length-1):
            combs.append([curent] +combo)
    print(combs) 




n=int(input("enter limit:"))
l=[]
combs=[]
for i in range(0,n):
    l.append(input())
combinations(l,n)


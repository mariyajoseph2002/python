""" Bob has a playlist of 
 songs, each song has a singer associated with it (denoted by an integer)

Favourite singer of Bob is the one whose songs are the most on the playlist

Count the number of Favourite Singers of Bob
 """
n = int(input())     
play=[]             # Reading input from STDIN
for i in range(0,n):
    a=int(input())
    play.append(a)
         # Writing output to STDOUT
singercount={}
for i in play:
    if i in singercount:
        singercount[i]+=1
    else:
        singercount[i]=1

maxcount=max(singercount.values())
favcount=0
for j in singercount.values():
    if j==maxcount:
        favcount+=1
print(favcount)
    


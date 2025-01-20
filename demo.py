print("hello")


a=10
print(type(a))

a=b=c=12
print(a,b,c)

a,b,c=12,12.4,"helllo"
print(a,b,c)
print(type(a),type(b),type(c))

l=[1,2,3,1,"adsd",4.6]
print(l)
print(type(l))
print(l[0])
l.append(10)
print(l)
l[1]=10
print(l)

h={"slno":1,"color":"red"}
print(h)
print(type(h))
print(h["slno"])


b=(1,2,3,"asd",9.0)
print(b)
print(type(b))
print(b[0])


v={1,12,12,1,3,"gj",9.0}
print(v)
print(type(v))
v.add(15)
print(v)

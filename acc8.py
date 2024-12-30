""" Daniel has a ball. He wants to find the ball's rebound height, which he dropped from height H with an initial velocity V. After the Nth rebound the final velocity of the ball is Vn. Your task is to help him find and return an integer value representing the height to which the ball rebounds after N bounces. """

def bounded_height(in1,in2,in3):
    e=in2//in3
    new_e=e**2
    return in1*new_e

h=int(input("enter initial height"))
v=int(input("enter initial velocity"))
vn=int(input("enter final velocity"))
print(bounded_height(h,v,vn))

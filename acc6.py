""" You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number """
""" 
def CheckPassword(str):
    st='False'
    if str[0].isnumeric():
        if len(str)>4:
            for i in str:
                if i.isupper():
                    st='True'
                    if str==' ' or str=='/': 
                        st='False'
    return st
strr=input("Enter password:")
print(CheckPassword(strr))

                    
 """



# input a no . and display the sum of squares till that no


# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=(i*i)
# print(sum)




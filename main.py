def stepen(m,n,t):
    if n!=0:
        return(stepen(m,n-1,t*m))
    else:
        return(t)
def sum(a,b):
    if b!=0:
        return(sum(a+1,b-1))
    else:
        return(a)

#Первое задание
m=int(input())
n=int(input())
print(stepen(m,n,1))
#Второе задание
a=int(input())
b=int(input())
print(sum(a,b))

#fibonacci series
n=int(input("enter no.of terms:"))
a=0
b=1
print(a,end=",")
print(b,end=",")
for i in range(2,n+1):
    s=a+b
    print(s,end=",")
    a=b
    b=s



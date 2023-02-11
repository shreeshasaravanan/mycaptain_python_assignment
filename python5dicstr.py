
str1=input("enter the string:")
dict1={}
for i in str1:
    ct=str1.count(i)
    dict1[i]=ct
sortdic=sorted(dict1.items(),reverse=True,key=lambda x:x[1])
print(dict(sortdic))

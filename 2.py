str1=input("enter first string")
str2=input("enter second string")
a=str2[-1]
count=0
for i in str1:
    if i==a:
        count=count+1
print(count)

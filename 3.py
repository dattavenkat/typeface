s=(0,1,2,5,6,8,9)
inp=int(input())
count=0
ps=""
for i in s:
    count=count+1
    ps=ps+str(i)
    
def validity(k):
    k=str(k)
    for i in k:
        if i not in ps:
            return False
    return True
    
if inp<count:
    k=s[inp]
else:
    k=s[-1]
    while(count<=inp):
        k=k+1
        if validity(k):
            count=count+1
print(k)   

    
    

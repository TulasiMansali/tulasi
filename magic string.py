s=input()
n=len(s)
d={}
mx=0
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    if d[i]>mx:
        mx=d[i]
print(n-mx)                
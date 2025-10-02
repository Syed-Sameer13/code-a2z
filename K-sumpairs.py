s=list(map(int,input().split(',')))
k=int(input())
se=set()
a=()
for i in range(len(s)):
    for j in s[i+1:]:
        if (s[i]+j)==k:
            a=(s[i],j)
            a=list(a)
            a.sort()
            a=tuple(a)
            se.add(a) 
se=list(sorted(se))
for i in se:
    print(i)

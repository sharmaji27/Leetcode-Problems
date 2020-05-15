A = "s z z z s"
B = "s z ejt"
d={}

for i in A.split():
    d[i] = d.get(i, 0) + 1

for i in B.split():
    d[i] = d.get(i, 0) + 1

l=[]
for k,v in d.items():
    if v==1:
        l.append(k)

print(l)
a, b=input().split()


results = []

for i in a:
    for j in b:
        c = i + j
        if c not in results: 
            results.append(c)


for r in results:
    if r[1]==0:
      d=r[0]
    elif r[1]==r[0]:
      d=r[0]
    elif r[0]=="A" and r[1]=="B":
       d=r

    
    print(d, end=" ")


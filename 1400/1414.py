c = input()
c = c.lower()
ccount = 0
cccount = 0
for x in range(len(c)):
    if c[x] == "c":
        ccount += 1
    if c[x:x+2] == "cc":
        cccount += 1
print(ccount)
print(cccount)
a=int(input())
n=input()
dna={"A":"U", "T":"A", "C":"G", "G":"C"}

a=""
for b in n:
  a+=dna[b]
print(a)

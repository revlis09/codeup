n=list(input())
count=0
count1=0
for i in n:
  if i=="(":
    count+=1
  elif i==")":
    count1+=1

print(count)
print(count1)
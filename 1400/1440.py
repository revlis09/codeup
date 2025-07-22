n=int(input())
count=1
a=list(map(int, input().split()))
for i in range(0, len(a)):
  print(f"{count}:", end=" ")
  for j in range(0, len(a)):
    if i !=j :
      if a[i] > a[j]:
        print(">", end=" ")
      elif a[i]==a[j]:
        print("=", end=" ")
      else:
        print("<", end=" ")
  print()
  count+=1
  
def f():
  a, b=map(int, input().split())
  if a>b:
    result=a-b
  else:
    result=b-a
  return result


print(f())
def f():
  a, b=map(int, input().split())
  if a>b:
    result=b
  else:
    result=a
  return result


print(f())
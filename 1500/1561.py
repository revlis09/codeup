def f():
  a, b=map(int, input().split())
  if a>b:
    result=a
  else:
    result=b
  return result


print(f())
a, b=map(float,input().split())
weight=(a-100)*0.9
weight_1=(b-weight)*100/weight

if weight_1<=10:
  print("정상")
elif 10<weight_1<=20:
  print("과체중")
else:
  print("비만")
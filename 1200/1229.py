height, weight=map(float,input().split())
if height<150:
  right=height-100
elif 150<=height<160:
  right=(height-150)/2+50
else:
  right=(height-100)*0.9

right1=(weight-right)*100/right

if right1<=10:
  print("정상")
elif 10<right1<=20:
  print("과체중")
else:
  print("비만")
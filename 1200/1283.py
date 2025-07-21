a = float(input())  
b = int(input())  
changes = list(map(int, input().split())) 

money = a
for percent in changes:
    money *= (1 + percent / 100)

profit = money - a

if -0.5 < profit < 0.5:
    profit = 0
else:
    profit = round(profit)

print(int(profit))

if profit > 0:
    print("good")
elif profit == 0:
    print("same")
else:
    print("bad")
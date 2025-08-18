a = int(input())
b = a * 10
count = 0

b_1 = b // 25
count += b_1

b_1_m = b % 25

c_1 = b_1_m // 15
count += c_1

b_1_m = b_1_m % 15

d_1 = b_1_m // 10
count += d_1

print(count)
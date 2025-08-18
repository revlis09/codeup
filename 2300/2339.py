n = 32900
n_1 = 30000
target = n - n_1  

count = 0

count += target // 300
target = target % 300

count += target // 200
target = target % 200

count += target // 100
target = target % 100

print(count)

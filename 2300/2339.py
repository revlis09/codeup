n=32900
n_1=30000
result=n-n_1
count=0
result_1=result//300
result_1_max=result%300
count+=result_1
result_2=result_1//200
result_2_max=result_1_max%200
count+=result_2
result_3=result_2//100
result_3_max=result_2_max%100
count+=result_3

print(count)
# 입력
n = int(input())                     
temp = list(map(int, input().split()))  
d = [0] + temp                      
k = int(input())                

def lower_bound(k):
    for i in range(1, n+1):
        if d[i] >= k:   
            return i
    return n + 1       

print(lower_bound(k))

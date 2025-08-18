
n = int(input())               
temp = list(map(int, input().split()))  
d = [0] + temp                  
a=int(input())

def maxi(a): 
    b=1
    for i in range(len(temp)):
        if a<temp[i]:
            b=0
            return i+1
    if b==1:
        return(n+1)
    

# 결과 출력
print(maxi(a))

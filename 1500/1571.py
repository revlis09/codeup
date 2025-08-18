# 입력
n = int(input())                     
temp = list(map(int, input().split()))  
d = [0] + temp                        # 1-based index 맞춤
k = int(input())                       # 찾을 값

# 함수 작성
def upper_bound(k):
    for i in range(1, n+1):
        if d[i] > k:   # k보다 큰 값 찾기
            return i
    return n + 1        # 모두 작거나 같으면 n+1 반환

# 결과 출력
print(upper_bound(k))

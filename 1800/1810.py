s = input()
start, n = map(int, input().split())

# 1부터 시작한다고 가정했을 때
sub = s[start - 1 : start - 1 + n]

print(sub)

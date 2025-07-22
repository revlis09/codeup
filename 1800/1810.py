s = input()
start, n = map(int, input().split()) 


sub = s[start-1:start + n-1]

print(sub)

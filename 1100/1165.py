minute, score = map(int, input().split())
 
while minute<90 :
    minute += 5
    score += 1
 
print(score)
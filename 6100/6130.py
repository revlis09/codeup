s = input().strip()  

x_index = s.find('x')   

a = int(s[:x_index])    
b = s[x_index + 1]     
c = int(s[x_index + 2:]) 

if b == '+':
    x = -c / a
elif b == '-':
    x = c / a

print(f"{x:.2f}")
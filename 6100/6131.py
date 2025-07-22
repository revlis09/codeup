s = input().strip() 

x_index = s.find('x')
eq_index = s.find('=')

a = int(s[:x_index])         
op = s[x_index + 1]      
b = int(s[x_index + 2:eq_index]) 
c = int(s[eq_index + 1:])    


if op == '+':
    x = (c - b) / a
elif op == '-':
    x = (c + b) / a


print(f"{x:.2f}")

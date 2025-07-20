form = input()
for x in range(len(form)):
    if form[x] == '+':
        a = int(form[:x])
        b = int(form[x+1:])
        print(a + b)
    elif form[x] == '-':
        a = int(form[:x])
        b = int(form[x + 1:])
        print(a - b)
    elif form[x] == '*':
        a = int(form[:x])
        b = int(form[x + 1:])
        print(a * b)
    elif form[x] == '/':
        a = int(form[:x])
        b = int(form[x + 1:])
        print("%0.2f" %(a / b))

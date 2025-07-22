text=input()
text1=""
text2=""
for i in range(len(text)):
    text1+=chr(ord(text[i])+2)
    text2+=chr(ord(text[i])*7%80+48)
print(text1)
print(text2)
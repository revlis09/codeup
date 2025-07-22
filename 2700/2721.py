S1 = input()
S2 = input()
S3 = input()

if S1[-1] == S2[0]:
    if S2[-1] == S3[0]:
        if S3[-1] == S1[0]:
            print("good")
        else:
            print("bad")
    else:
        print("bad")
else:
    print("bad")
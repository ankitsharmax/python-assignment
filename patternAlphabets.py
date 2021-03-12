asciiValue = 65
for i in range(0,5):
    for j in range(0,i+1):
        print(chr(asciiValue),end=' ')
        asciiValue += 1
    print()

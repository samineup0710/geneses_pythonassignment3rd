n = int(input("input the rows: "))
"""left-sided * traingle"""
print("The left sided pyramid is:")
for i in range(1, n+1):
    #print(i)
    for x in range(1,(n-i)+1):
        #print(x)
        print(" ", end="")
    for star in range(1,i+1):
        print("*", end="")
    print()

""" right-sided * traingle"""
print("The right sided pyramid is:")
for j in range(1, n+1):
    #print(i)
    for y in range(n-j+1, 1):
        #print(x)
        print(" ", end="")
    for star in range(1, (n-j+2)):
        print("*", end="")
    print()

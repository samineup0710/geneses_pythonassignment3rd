#userinput = "pineapple"
userinput = input("enter a input in strings:").strip()
print(userinput)
dictval = {}
for ch in userinput:
    #print(ch)
    if len(userinput)==0:
        print("invalid operations")
        """ count each character repetition"""
    x = userinput.count(ch)
    dictval[ch] = str(x)     # append into dictionary
print(dictval)


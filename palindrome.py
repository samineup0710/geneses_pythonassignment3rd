"""take input from user"""
userinput = input("enter a input in strings:")


"""printing the input from user"""
print("The user input is:", userinput)


"""rerversing the string"""
inpt = userinput[::-1]
print("The reversed string is:",inpt)

""" check if the reversed string matches the input string or not""" 
if inpt!=userinput:
    print("{}is not a palindrome string".format(str(userinput)))
else:
    print("{} is a palindrome string".format(str(userinput)))
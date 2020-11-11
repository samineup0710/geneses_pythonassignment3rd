userinput = input("enter a input in strings:")
import re 
"""set counters"""
upp=0
sc =0
num = 0
"""checking and counting"""
for ch in userinput:
    if (ch>='a'and ch<='z'):
        low = low+1
    if(ch>='A' and ch<='Z'):
        upp = upp+1
    if re.match("^[!@#$%^&*()_]*$", ch):       #regex checking special character pattern
        sc = sc+1
    if re.match("^[0-9]", ch):
        num = num+1
print("The num of lowercase char in string is {}".format(low))
print("The num of uppercase char in string is {}".format(upp))
print("The num of special char in string is {}".format(sc))
print("The num of digitnumber  in string is {}".format(num))

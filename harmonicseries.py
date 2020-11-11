inp =int(input("Enter the number of terms: "))
"""set counter to store sum"""
s = 0
for i in range(1,inp+1):
    s =s+(1/i)
    if i!=0:
        """to print harmonic series"""
        print("1/{} + ".format(i), end = " ")
        """ to print harmonic series sum"""
print("\nThe sum of series is",round(s,3))


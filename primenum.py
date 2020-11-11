""" list to store prime numbers"""
primelist = []

""" list to store non prime numbers"""
nonprimelist = []

"""outer loop for looping through our numbers"""
for j in range(1, 101):
    count =0    
    for i in range(1, j+1):
        if j%i == 0:
            count = count +1
    if (count ==2):           #prime num have only 2 factors
        primelist.append(str(j))
    else:
        nonprimelist.append(str(j))
print("The list of prime numbers are:", primelist)
print("The list of nonprime numbers are:", nonprimelist)
""" 
# WAP to check the given number is prime or not.

# num = 29

# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
        
===========================================================================================================
# Find the largest number in the list.

data = [12,54,105,20,2,8,86,45,30]

largest = data[0]

for i in data:
    if i > largest:
        largest = i
        
print(largest)

============================================================================================================
# WAP to find smallest number in the list.

data = [12,54,105,20,2,8,-10,86,45,30]

smallest = data[0]

for i in data:
    if i < smallest:
        smallest = i
        
print(smallest)

============================================================================================================

"""

# Find the second largest number in the list.

data = [12,54,105,20,2,8,-10,86,45,30]

largest = data[0]
sec_largest = float('-inf')

for i in data:
    if i > largest:
        sec_largest = largest
        largest = i
        
    elif i > sec_largest and i != largest:
        sec_largest = i
            
print("Largest Number :",largest)
print("Second Largest Number :",sec_largest)
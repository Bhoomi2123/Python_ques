# Swap 2 variables
 
# Using third variable
num1 = int(input("Enter 1st number : "))  
num2 = int(input("Enter 2nd number : ")) 

print("Numbers before swapping are", num1, "&", num2) 

t = num1
num1 = num2
num2 = t

print("Numbers after swapping are", num1, "&", num2)

# Using comma assignment operator
num1 = int(input("Enter 1st number : "))  
num2 = int(input("Enter 2nd number : ")) 

print("Numbers before swapping are", num1, "&", num2) 

num1, num2 = num2, num1

print("Numbers after swapping are", num1, "&", num2)
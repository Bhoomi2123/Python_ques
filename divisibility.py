num = int(input("Enter number to be checked : "))

print(num, "is divisible by these numbers :")
for i in range(1, num+1):
    if (num % i == 0):
        print(i)
        
        
        
num1 = int(input("Enter smaller number : "))
num2 = int(input("Enter larger number : "))

def hcf(x, y):
    for i in range(1, x+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
            
print("HCF of", num1, "&", num2, "is", hcf(num1, num2))
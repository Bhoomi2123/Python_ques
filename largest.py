num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

if(num1 > num2 and num1 > num3):
    print("1st number is largest :", num1)
elif(num2 > num1 and num2 > num3):
    print("2nd number is largest :", num2)
else:
    print("3rd number is largest :", num3)
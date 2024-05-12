num = int(input("Enter number : "))

c=0
sum = 0
org = number = num

# finding no. of digits
while(num > 0):
    rem = num%10
    num = num//10
    c+=1

# finding armstrong
while(org>0):
    r = org%10
    sum = sum + (r**c)
    org = org//10
    
if(sum == number):
    print(number, "is an armstrong number!")
else:
    print(number, "is not an armstrong number!")
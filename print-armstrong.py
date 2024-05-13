lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))

for num in range(lower, upper+1):
    temp = org = num
    ord = 0
    sum = 0
    
    # finding order
    while(temp > 0):
        rem = temp % 10
        ord += 1
        temp = temp // 10
        
    while(org > 0):
        r = org % 10
        sum = sum + (r ** ord)
        org = org // 10
        
    if(num == sum):
        print(num, "is an armstrong number")

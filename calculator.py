#calculator
while True:
    print("select operation:")
    print("1.Add")
    print("2.Subsract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exponention")
    print("6.Modulus")
    print("7.Exit")
    choice = input("Enter choice(1/2/3/4/5/6/7):")
    
    if choice == '7':
        break
    
    num1= int(input("first number:"))
    num2=int(input("second number:"))
    
    if choice== '1':
        result=num1+num2
        print("sum =",result)
        
    elif choice=='2':
        result=num1-num2
        print("difference=",result)
        
    elif choice== '3':
        result=num1*num2
        print("product=",result)

    elif choice== '4':
        result=num1/num2
        print("quotient=",result)

    elif choice== '5':
        result=num1**num2
        print("power=",result)

    elif choice== '6':
        result=num1%num2
        print("reminder=",result)

    else :
        print("invalid operation")

while True:
    print("="*62)
    print( """#calculator project""" )
    print("="*62)
    num1 = float(input("what's your first number:"))
    operator = input("""
    Choose operator:
    +  Addition
    -  Subtraction
    *  Multiplication
    ** Power
    /  Division
    // Floor division
    %  Remainder
    
    Enter your choice: 
    """)
    num2 = float(input("what's your second number:"))
    
    if operator == "+":
        print("sum =",num1+num2)
    
    elif operator == "-":
        print("difference =",num1-num2)
    
    elif operator == "*":
        print("product=",num1*num2)
    
    elif operator == "**":
        print("square=",num1**num2)
    
    elif operator == "/":
        print(" coefficient =",num1/num2)
    
    elif operator == "//":
        print("floar division value =",num1//num2)
    
    elif operator == "%":
        print("reminder =",num1%num2)
    else:
            print("="*62)
            print( """just try to enter the operator in the given menu else u cannot run the program! """ )
            print("="*62)
            
    again = input("i wonder if u want another calculation! if yes enter yes else  enter no")
    if again.lower() not in ["yes", 'y' ,'ye','ya']:
               break
           
           
           
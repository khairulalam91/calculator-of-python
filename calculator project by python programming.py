import math

print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBSTRACTION")
print("3. MULTIPLICATION")
print("4. DIVIDE")
print("5. SAMPLE MATH")

operation = input()

if operation == "1":
    try:
        def add(*numbers):
            sum=0
            for num in numbers:
                sum = sum+num
            print(sum)

        list=[]
        n=int(input("Enter the number of element: "))
        for i in range(0,n):
            num=int(input())
            list.append(num)
        add(*list)
    except ValueError:
        print("Wrong Input")
    
elif operation=="2":
    def sub(num1,num2):
        return (num1-num2)
    try:
        num1 = int(input("Enter the first value: "))
        num2 = int(input("Enter the second value: "))
        result = sub(num1,num2)
        print("Substraction is: ", result)

    except ValueError:
        print("Wrong Input")
        
elif operation=="3":
    try:
        numbers=[]
        while True:
            number = input("Enter a number: ")
            if number== "=" or number=="":
                break
            else:
                numbers.append(number)
        multiplication = 1
        for num in numbers:
            multiplication*=int(num)
        print(f"Multiplication = {multiplication}") 
    except ValueError:
        print("Wrong Input")
        
elif operation=="4":
    try:
        num1 = input("Enter the first value: ")
        num2 = input("Enter the second value: ")
        division = float(num1) / float(num2)
        print("Division is: ", division)
    except ZeroDivisionError:
        print("Undefined")
    except ValueError:
        print("Wrong Input")
    finally:
        print("Thank You")

elif operation=="5":
    try:
        x=int(input())
        y=int(input())
        a=math.sin(x)
        b=math.cos(y)
        pi=math.pi
        ans = eval(input("enter your number and math operation : "))
        print(ans)
    except ValueError:
        print("Wrong Input")
    finally:
        print("Thank You")
        
        



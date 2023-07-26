num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
if num1>num2 and num1>num3:
    print("num1 wins:")
    if num2>num3:
        print("num2 is middle:")
        print("num3 is last:")
    else:
        print("num3 is middle:")
        print("num2 is last:")
if num2>num1 and num2>num3: 
    print("num2 wins:")
    if num3>num1:
        print("num3 is middle:")
        print("num1 is last:")
    else: 
        print("num1 is middle:")
        print("num3 is last:")
if num3>num1 and num3>num2:
    print("num3 wins: ")
    if num1>num2: 
        print("num1 is middle:")
        print("num2 is last:")
    else: 
        print("num2 is middle:")
        print("num1 is last:")
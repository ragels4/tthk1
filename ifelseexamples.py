#Example1
local = int(input("Input ur age: "))
if local >= 18:
    age = "ur old"
else:
    age = "ur a kid"
print (age)


#Example2
numbr = int(input("Input number to check "))
if numbr % 2 == 0:
     numbr = "Even"
else:
     numbr = "Odd"
print (numbr)

#Example3
num1 = int(input("Input number1 - "))
num2 = int(input("Input number2 - "))
num3 = int(input("Input number3 - "))

if num1 > num2 and num1 > num3:
    print("Number1 is the biggest")
elif num2 > num1 and num2 > num3:
    print("Number2 is the biggest")
else:
    print("Number3 is the biggest")
    

inp = int(input("How much points u got: "))

if inp < 0 or inp > 100:
    grade = ("U aint got that amount of points lil bro ong fr")
    print (grade)
    exit()
elif inp < 60:
    grade = "D"
elif inp < 74:
    grade = "C"
elif inp < 89:
    grade = "B"
else:
    grade = "A"

print("Your grade is -", grade)

num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
opp = input("Input the operator (+, -, *, /): ")
print("")

if opp == '+' or opp == '-' or opp == '*' or opp == '/':
    if opp == '+':
        print(num1 + num2)
    elif opp == '-':
        print(num1 - num2)
    elif opp == '*':
        print(num1 * num2)
    elif opp == '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Cannot divide by zero")
else:
    print("Invalid operator")

#Counting from 1 to usr input
i = 1
ask = int(input("how many times max sucked? "))
while i <= ask:
          print("okay he sucked", i, "times")
          i = i + 1
          
print("")

#Counting from usr input to 1
asky = int(input("okay lets count down from what number? "))
while asky >= 1:
           print("okay im on", asky, "rn")
           asky = asky - 1
           
print("")

#Number times itself ig idk ts pmo
usinp = int(input("Input number "))
c = 1
summa = 0
while usinp >= c:
    print("Max sucked", c, "times")
    summa = summa + 1
    c = c + summa
    
print("")
    
#Check if the numbers are even or odd on the way to usr input ig idk ts pmo
intask = int(input("enter number "))
crnt = 0
even = 0
odd = 0
while crnt < intask:
    crnt = crnt + 1
    if crnt % 2:
        print("The number", crnt, "is odd")
        odd = odd + 1
    else:
        print("The number", crnt, "is even")
        even = even + 1
print("")
print("Amount of even numbers: ", even)
print("Amount of oddnumbers: ", odd)
    
#How does break work?
b = 1
inputiga = int(input("Enter numbriga: "))

while b < inputiga:
    if "3" in str(b):  
        b += 1        
        continue      
    
    print(b)
    b += 1
print("")
    
#Number guesser
import random
guess = random.randint(1, 100)
trysum = 5

while trysum > 0:
    tryniga = int(input("Try to guess a number! U have " + str(trysum) + " tries left! "))

    if tryniga == guess:
        print("U guessed right!")
        break
    elif tryniga < guess:
        trysum -= 1
        print("Too low, try again. Only " + str(trysum) + " tries left!")
        print("")
    elif tryniga > guess:
        trysum -= 1
        print("Too high, try again. Only " + str(trysum) + " tries left!")
        print("")

if trysum == 0:
    print("Sorry, you have run out of tries. The correct number was " + str(guess))

print("")
    
#ATM App

passwd = 123
errs = 3
acb = 88 

while errs > 0:
    logscreen = int(input("Enter the password: "))

    if logscreen == passwd:
        print("Login Successful!")
        
        while True:
            print("\nChoose an operation option:")
            print("1 - Withdraw")
            print("2 - Put money")
            print("3 - Check account balance")
            
            bank = input("Type here: ")

            if bank == "1":
                print("")
                witd = int(input("Okay, how much money do you want to withdraw? "))
                if witd <= acb:  
                    acb -= witd  
                    print(f"Okay, here is your {witd} euros.")
                else:
                    print("Sorry, not enough money.")
            
            elif bank == "2":
                print("")
                amount = int(input("How much money would you like to deposit? "))
                acb += amount  
                print(f"{amount} euros have been added to your account.")
            
            elif bank == "3":
                print("")
                print(f"Your account balance is {acb} euros.")
            
            else:
                print("Invalid option. Please choose one of the listed options.")
            
            smthelse = input("\nDo you want to perform another operation? (y/n): ")
            if smthelse != "y":
                print("Exiting the system.")
                break  
        
    else:
        errs -= 1
        if errs > 0:
            print(f"Invalid password. You have {errs} tries left.")
        else:
            print("Invalid password. Card is blocked and 911 is called.")
            break


        
              

    
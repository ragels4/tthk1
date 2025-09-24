#Exercise1 - Time of Day
hrs = int(input("Input the time (1-24): "))
if hrs <= 6:
    print("Night")   
elif hrs <= 12:
    print("Morning")
elif hrs <= 18:
    print("Afternoon")
else:
    print("Evening")
print("")   
print("=============================================")
print("")
    
#Exercise2 - Drink Choice
prf = input("Hot or Not ? ")
if prf == "Hot":
    tip = input("Okay, Tea or Coffee? ")
    if tip == "Tea":
        print("We'll serve you a tea")
    elif tip == "Coffee":
        print("We'll serve you a coffee")
else:
    print("We'll serve you a limonade")
print("")   
print("=============================================")
print("")

#Exercise3 - Color type
clr = input("Choose a color: ")
if clr == "Red":
    print("Bright")
elif clr == "Blue":
    print("Calm")
else:
    print("Normal color")
print("")   
print("=============================================")
print("")

    
#Exercise4 - By the scheme
trp2 = input("Choose transport ")
wth2 = input("Whats the weather? ")

if trp2 == "Bus":
    if wth2 == "Rain":
        print("Bus ride through rain")
    else: print("Comfy bus ride")
else:
    if wth2 == "Rain":
        print("We'll take an umbrella")
    else:
        print("Comfy walk")
        

    


    
print("")
print("=============================================")
print("")

#Exercise5 - Food type
ftp = input("Fruit or Vegetable? ")
sos = input("Sweet or Sour or anything else? ")
if ftp == "Fruit" and sos == "Sweet":
    print("Thats an edible fruit!")
elif ftp == "Fruit" and sos == "Sour":
    print("Thats a fruit full of vitamins!")
elif ftp == "Fruit" and sos:
    print("A regular fruit")
elif ftp == "Vegetable" and sos == "Sweet":
    print("Thats a sweet vegetable!")
elif ftp == "Vegetable" and sos == "Sour":
    print("Thats a sour vegetable!")
elif ftp == "Vegetable" and sos:
    print("A regular vegetable")

print("")
print("=============================================")
print("")
    
#Exercise5 - Alternative

fod = input("Fruit or Vegetable? ")
stp = input("Sweet or Sour? ")
print (stp + " " + fod)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

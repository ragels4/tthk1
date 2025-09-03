print (6+7)
print ("6"+"7")
# "hello world" - str
# 1 - int
# 1.5 - float

# muutujad
name = "Dominik"
surname = "Ragels"

print (name)
print (surname)
print (name+ " " + surname)
print (" ")

show="Breaking Bad,"
year="Released in 2008."
producer="The producer is Vince Galligan."
actor1="The first actor is Bryan Cranston, "
actor2="the second actor is Aaron Paul"

print (show+" "+year + " " +producer + " " + actor1 + "and" " " +actor2)


# luua muutujad film, aasta, rezisöör, näitleja1, ja näitleja 2
# tulemus - Film breaking bad ilmus aastal 2008, rezisöör on Vince Galligan,
# ning peanäitlejad on Bryan Cranston ja Aaron Paul

favanimal = input("Input ur fav animal: ")
print("My fav animal is: " + favanimal)

#str() - text to number
#int() - number to text
height = int(input("Input height "))
width = int(input("Input width "))
circumfrence = 2 * (height + width)
area = (height * width)
print (" ")
print ("Circumfrence: ", circumfrence)
print ("Width: ", width)
print (" ")

# Programm where it asks u some personal things like ur name and fav food
nameask = input("Whats ur name?: ")
ageask = input("How old are u?: ")
placeask = input("Where do u live?: ")
movieask = input("Whats ur favourite movie/show?: ")
musicask = input("What kind of music do u like?: ")
foodask = input("Name ur 3 favourite foods!: ")

print(" ")
print("Welcome: " + nameask + " and thanks for answering all the questions lil bro, here is what i know about u know")
print("Ur name is: " + nameask)
print("U are : " + ageask)
print("U live in: " + placeask)
print("Ur favourite movie is: " + movieask)
print("Ur favourite music to listen to is: " + musicask)
print("And finally, ur top 3 foods are: " + favanimal)
print(" ")
print("alright man thanks for taking the time on answering all the questions and all that, come again anytime lil bro")
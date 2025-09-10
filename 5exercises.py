#Task1
N1 = float(input("Input first number "))
N2 = float(input("Input second number "))
sum = (N1 + N2)
multi = (N1 * N2)
difer = abs(N1 - N2)

print ("It equals to: ", sum)
print ("Multiplied its:", multi)
print ("The difference between those numbers is:", difer)

print ("")

#Task2
nameask = input("Input your name ")
ageask = int(input("Input your age "))

yearcalc = int(2025 - ageask)

print ("Hello, ", nameask)
print ("Your were probably born in", yearcalc)

print ("")

#Task3
seconds = int(input("Input the amount of seconds "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secondfinal = seconds % 60

print ("Here is the time in the HH:MM:SS format: ", hours, ":", minutes, ":", secondfinal)

print ("")

#Task4
nama = float(input("Input the number (a) "))
namb = float(input("Input the number (b) "))
print("")

print("Before swapping: a =", nama, "b =", namb)
print("After swapping: a =", namb, "b =", nama)

#Task5
flightnumb = input("Input your flight number: ")
depcode = input("Input your local airport's code: ")
descode = input("Input your destination airport's code: ")
lvtime = input("Input the time of the start of your flight in HH:MM format: ")

hours, minutes = lvtime.split(":")
fhours = int(hours)
minutiga = int(minutes)

# Create a time list to fix the NameError
time = [fhours, minutiga]

minutiga 

print(time[0])
print("")
print("****************************************")
print("          National Airline              ")
print("*                                      *")
print("*  Flight number: " + flightnumb + "                  *")
print("*                                      *")
print("*  "+depcode+"->"+descode+"            *")
print("*                                      *")
print("*  Departure time:", fhours, ":", minutiga)
print("*  Arrival time:", fhours + 1, minutiga + 45)





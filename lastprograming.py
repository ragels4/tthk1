arr = ["hello", 88, "two", "donkey"]

print(arr[0])
print(arr[-1])
print(arr[len(arr) - 1])
print(arr[len(arr)//2])

print("-----------------------------------------")
for i in range(0, len(arr)):
    print(arr[i])
    
print("-----------------------------------------")
    
firstElements = arr[0:4]
middleToEnd = arr[len(arr)//2:]
print(middleToEnd)
print(arr[-3:])
print(arr[-1::-1])

print("-----------------------------------------")

myArr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
oddArr = myArr[:len(myArr):2]

print(oddArr)

print("-----------------------------------------")

ToddArr = []
TevenArr = []
for n in range(0,len(myArr)-1):
    if myArr[n] % 2 == 0:
        TevenArr.append(myArr[n])
    else:
        ToddArr.append(myArr[n])
print(ToddArr)
print(TevenArr)

print("-----------------------------------------")

basket = ["milk", "bread", "eggs"]
basket.append("Butter")
basket.insert(0, "Tea")

sugaradd = []
sugaradd.append("sugar")
basket = sugaradd + basket
print(basket)

print("-----------------------------------------")

for p in basket[:]: 
    if len(p) > 4:
        basket.remove(p)
        print(p)
    else:
        print(p)



















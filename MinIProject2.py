'''
##- Variables.

#1.String programs
str1= "Python Program"
print(len(str1))
print(str1[0])
print(str1[-1])
print(str1[0:3])
print(str1[0:])
print(str1[:3])
print(str1[:])


#- String method

str1= "Python Program"
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
print(str1.find("P"))
print(str1.find("Pro"))


#-Numbers

x = 10
y = 3

print(x+3)
print(x-3)
print(x*3)
print(x/3)
print(x//3)
print(x%3)
print(x**3)


#- Some math modules

print(round(2.3))
print(round(2.7))
print(abs(-2.5))



#- Type converstion

x = input("x: ")
y = int(x) + 1

print(f'x: {x}, y: {y}')

 #- Conditional statement

temp = 15
if temp > 30:
    print("Hot")
elif temp > 20:
    print("Normal day")
else:
    print("cold")



#- Logical operater
# - AND

income = True
Credit = True

if income and Credit:
    print("credit card ok")
else:
    print("credit card not")

# - OR

income = True
Credit = False

if income or Credit:
    print("credit card ok")
else:
    print("credit card ")


#-- loops
#- For lopps.

for number in range(4):
    print("Attempt", number)
    print("Attempt", number+1)
    print("Attempt", number+1, (number+1) * "*")



#- For else

suc = True
for num in range(3):
    print("Attempt")
    if suc:
        print("suc")
        break
else:
    print("Attemted 3 times and fail")


 #- nested loops

for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")


#- While loops

num = 100
while num >0:
    print(num)
    num //= 2


#-- lists
#- Accessing letters

letters = ["a", "b", "c"]
print(letters[1])
print(letters[-1])
print(letters[0:3])
print(letters[:3])
print(letters[1:])
print(letters[::2])
print(letters[::-1])

#- Adding & Remove list

letters = ["a", "b", "c"]
letters.append("d")
print(letters)
letters.insert(0,"*")
print(letters)
letters.remove("b")
print(letters)
letters.pop(0)
print(letters)


#- sort list

num = [3, 5, 1, 2, 6]
num.sort()
print(num)
num.sort(reverse = True)
print(num)

#  - Tuple

point = (1, 2)
print(type(point))


point = (1, 2) + (3, 4)
print(point)
point = (1 ,2) * 3
print(point)
point = tuple([1, 2])
print(point)



point = (1, 2, 3)
print(point[0])
print(point[0:2])


# -Swapping variables

x = 10
y = 5

x,y = y, x
print("x", x)
print("y", y)

#-- sets

num = [1, 1, 2, 3, 4]
fis = set(num)
sec = {1,5}
print(fis | sec)
print(fis & sec)
print(fis - sec)
print(fis ^ sec)


#- Dictionaries

point = dict(x=1, y=2)
print(point["x"])
point["z"] = 20
print(point)

'''
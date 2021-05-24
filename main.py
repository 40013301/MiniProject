''''''
# 1.-- Write a python program to get a string from a given string where all occurence of itsfirst char have
  #- char have been changed to '$', expcet the first char itself sample
  # - String : 'restart' Expected  -- result : 'resta$t'

#str1 = "restart"
#fst_letter = str1[0]
#len1 = len(str1)

#for iterator in range(1, len1):
#    if fst_letter == str1[iterator]:
#        str1 = str1[0:iterator]+'$'+str1[iterator+1:len1]

#print(str1)



# - 2. Write a python program to remove the nth index character from a nonempty string.


#str1 = "python"
#index = int(input("Enter the index value: "))
#str1 = str1[0:index]+str1[index+1:]
#print(str1)

''''''

# - 3. Write a python program to find the first repeated character in a given string.

#str1 = "character"

#s = 0

#for i in range(0, len(str1)):
#    if s == 1:
 #       break
 #   for j in range(i+1, len(str1)):
  #      if str1[i]==str1[j]:
   #         print(str1[i])
    #        s = 1
     #       break

#if s == 0:
 #   print(-1)

### 4.---Write a python program to find the second smallest number in a list..

#lst = []
#num = int(input("Enter the number of elements: "))
#for x in range(1, num+1):
#    ele = int(input("Enter the element: "))
#    lst.append(ele)

#lst.sort()
#print("The second smallest value of this list: ", lst[1])



## 5.-- Write a python program to change the position of every nth value with the n+1 th in a list.

#lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#index1 = int(input("Enter the index: "))
#for x in range(1, len(lst)):
#    if x % index1 == 0:
#       lst[x-1], lst[x] = lst[x], lst[x-1]
#print(lst)

#-- 6. Write a python program to convert a list of tuples of tuples into a  dictionary.

#tup =[('Subbu' , 10), ('mahesh' , 25), ('dilli' , 30)]
#print(dict(tup))

#or
#print(dict([('Subbu' , 10), ('mahesh' , 25), ('dilli' , 30)]))

#--7. Write a python program to find the repeated items of a tuple.

#tup = 2, 4, 5, 2, 4, 7, 8  # - create the tuple
#print(tup)
#count = tup.count(5)       # - return the number of times it apper in the tuple
#print(count)

#--8. for kid, name in cities.items():print(kid, name)

#cities = {1 :"subbu" , 2 : "navven" , 3 : "murali"}
#for kid,name in cities.items():
#    print(kid,name)

#--9. Write a python program to merge two python dictionaries.

#dict1 = {"subbu": 10 , "mahesh": 25 , "dilli" : 55}
#dict2 = {"manu" : 99 , "laddu": 98 , "pandu" : 97}
#dict3 = dict1.copy()
#dict3.update(dict2)
#print(dict3)

#--10. Write a python program to convert a list into a nested dictionary of keys.

#num_list = [1, 2, 3, 4]
#new_dict = current = {}
#for name in num_list:
#    current[name] = {}
#    current = current[name]
#print(new_dict)


#-- 11. Write a python program to get next day of given date using if-elif-else.

#date = "03/11/1991"
#day = int(date[0:2])
#month = int(date[3:5])
#year = int(date[6:])
#print(type(day), day)
#print(type(month), month)
#print(type(year), year)

#week =(day + 2*month + 3*(month+1)//5+ year + year // 4 - year//100 + year//400 +2) % 7

#print("week: ", week)

#if (week == 0):
#    print("sunday")
#elif (week == 1):
#    print("Monday")
#elif (week == 2):
#    print("Tuesday")
#elif (week == 3):
#    print("Wednesdy")
#elif (week == 4):
#    print("Thursday")
#elif (week == 5):
#    print("Friday")
#else:
#    print("Saturday")


#-- 12. Write a python program to check if the input number is - real number - float number - string - complex num - zero(0)

#num = input("Enter the value: ")
#print(type(num))
#if(type(num) == type(" ")):
#    print("data is string")

#elif(type(num)  == type(3)):
#   print("real number")
#    if(num == 0):
#        print("Data is zero")

#elif(type(num)  == type(3.3)):
#    print("Data is Float")
#    print("real number")

#elif(type(num)  == type(3+3j)):
#    print("Data is Complex")
#else:
#    print("unknown number")

#elif num == "":
#    print("its a string")

#else:
#    print("complex number")

#--13. write a python program to check the user enters "lol", print("laughing out loud". if the user enters"rof1",---
#---print"rolling on the floor laughing". if the user enters "lmk", print "shaking my head".

#str1 = input("user enter the word : ")

#if str1 == "lol":
#    print("laughing out loud")

#elif str1 == "rof1":
#    print("rolling on the floor laughing")

#elif str1  == "lmk":
#    print("shaking my head")

#else:
#    print("user enter the worng word")

#--- 14. Write a python program that asks a user how many pizza slices they want.The pizzeria charges Rs-123.00----
#----a slice if user order even number of slices, price per slice is Rs-120 print the total price depending on how---
#---many slices user orders.

#slices = int(input("Enter the pizza slices: "))
#if (slices % 2 == 0):
#    print("Total cost: ", slices*123)
#else:
#    print("Total cost: ", slices * 120)



















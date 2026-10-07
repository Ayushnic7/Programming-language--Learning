# LECTURE 1 - VERIABLE AND DATA TYPES

# FOR COMMENET OUT  USE CTRL + /
#(      )  -  PARENTHESIS
# [      ]  -  SQUARE BRACKETS
#"   "  -  DOUBLE QUOTES
# '   '  -  SINGLE QUOTES
# <    >  -  LESS THAN AND GREATER THAN
# =    -  EQUAL TO
# : THE COLON IS USED TO DEFINE A BLOCK OF CODE IN PYTHON. IT IS USED TO DEFINE THE START OF A BLOCK OF CODE. IT IS USED TO DEFINE THE START OF A FUNCTION, CLASS, LOOP, IF STATEMENT, ETC.

# import string


# name = "ayush"
# age = 18
# price = 35.99

# print("my name is: ",name)
# print ("my age is :",age)-


# a = 4
# b = 2

# print(a + b) #addition 
# print(a - b) #subtract
# print(a * b) # multiplication 
# print(a / b) # for divivson
# print(a % b) # % its used for finding remainder
# print(a ** b) # here ** is used as power mean a^b (isme jo ahai jo pehle hai usko utna baar multiple kiya jaiygega jitna digit likha hoga like 5 ko yaha 2 baar 5 se multiply )
#  a^b means a to the power b matlab jo b hai wo a ka power hai


#RATIONAL OPERATORS

# a = 5 
# b = 2
# print (a == b )#false
# print (a != b )#true != that mean not equal to ! is the sign of not
# print (a >= b )#true
# print (a > b )#true
# print (a <= b )#false
# print (a < b )#false


#ASSINGMENT OPERATORS

# num = 10
# num = num + 10 #10+10=20
# num += 10
# num -= 10 
# num /= 10
# num %= 10
# num **= 10
# print ("num :", num )

#LOGICAL OPERATERS

# a = 9
# b = 3
# print (not False) #true
# print (not (a<b))

# val1  = True
# val2  = False

# print ("AND operators:", val1 and val2) # when both operators are same then true
# print ("OR operator:", val1 or val2) #only depend on true if even one value is true then it will give true
# print ("OR operator:",(a == b) or (a > b))

# TYPE CONVERSION 

# TWO TYPES OF TYPE CONVERSION
# 1). CONVERSION - AUTOMATICALLY
# 2). CASTING - MANUALLY


#1).TYPE CONVERSION 
# a = "2"
# b = 4.25

# print(a + b) # no answer coz string cannot sum with float

# 2). TYPE CASTING
# a = 3.14
# a = str(type(a))

# print(type(a))

#INPUT IN PYTHON

# age  = input("enter your age: ") 
# print ("your age is", age)

# print ("you entered", age)


# val = float(input("enter your val:"))
# print(type(val), val) #all value will be str if you wanr another tpye you should do type casting



 # MY 1ST  QUESTION - WRITE A PROGRAM TO INPUT 2 NUMBER & PRINT THEIR SUM

# first = int(input("enter first : "))
# second = int(input("enter second : "))
 
# print("sum =", first + second)

# 2ND QUESTION - WAP TO INPUT SIDE OF A SQUARE & PRINT ITS AREA

# side = float(input("enter square side : "))

# print("area =", side * side)#it will print the area of square.

# print("area 2 :", side ** 5 )#it will print the area of square to the power 5.

# 3RD QUESTION - WAP TO INPUT 2 FLOATING POINT NUMBERS & PRINT THEIR AVERAGE.

# first = float(input("enter first :"))
# second  = float(input("enter second :"))

# print("avg =", (first+second)/ 2)

# 4TH QIUESTION - WAP TO INPUT 2 INT NUMBERS, A AND B.PRINT TRUE IF A GREATER THAN OR EQUAL TO B. IF NOT PRINT FALSE?

# a = int(input("enter first: "))
# b = int(input("enter second: "))

# print (a >= b)



# LECTURE 2 -STRINGS & CONDITIONAL STATEMENTS.

                                                  # "CONCATENATION - JOINING OF 2 STRINGS"

# str1 = "hello"
# len1 = len(str1)
# print(len1)
# str2 = "world"
# len2 = len(str2)
# print(len2)
# str3 = str1+str2 #its used to add 2 strings.
# print(str3)
# str4 = str1 + " " + str2 #its used to add space between 2 strings.
# print(str4)
# len4 = len(str4) # empty space is also counted in length of string.
# print(len4) # len means length of string and len() is a function which is used to find the length of string.



       
       
       
       # "iNDEXING - INDEXING IS USED TO FIND THE POSITION OF A CHARACTER IN A STRING. INDEXING STARTS FROM 0 AND ENDS AT N-1 WHERE N IS THE LENGTH OF STRING."


# str = "asunix"
# char1 = str[0] # indexing starts from 0.
# print(char1)

         # "SLICING - SLICING IS USED TO EXTRACT A SUBSTRING FROM A STRING. IT TAKES 2 ARGUMENTS START AND END. START IS INCLUSIVE AND END IS EXCLUSIVE."

# str[startindex:endindex:step] # ending index is exclusive.
# str = "asunix"
# print(str[1:5]) # it will print from 1 to 4 index character.

# str = "apna college"
# print(str[0:4]) # it will print from 0 to 3 index character.
# print(str[0:len(str)]) # it will print whole string coz ending index is exclusive and len(str) is 12 so it will print from 0 to 11 index character.
# print(str[0:])# it will print whole string coz ending index is exclusive and len(str) is 12 so it will print from 0 to 11 index character.

                                                
# str = "apna college"
# print(str[-1]) # it will print the last character of the string.
# print(str[-4:]) # it will print from -4 to -2 index character. so minus mein zero hota hi nhi hai isiliye humlog left to rigt kar denge yni likh denge 

                                                                          #STRING FUNCTIONS


# str = " i love orange juice with salt "
# print(str.upper()) # it will print the string in uppercase.
# print(str.lower()) # it will print the string in lowercase.
# print(str.strip()) # it will remove the leading and trailing spaces from the string.
# print(str.replace("i love", "I HATE")) # it will replace the first string with the second string.
# print(str.split()) # it will split the string into a list of strings.
# print(str.find("orange")) # it will find the index of the first occurrence of the string.
# print(str.count("i")) # it will count the number of occurrences of the string.
# print(str.startswith("i love")) # it will return True if the string starts with the specified string.
# print(str.endswith("salt")) # it will return True if the string ends with the specified string 
# print(str.capitalize()) # it will capitalize the first character of the string.

#STRING IS MORE POWERFUL THAN WE THINK COZ IT HAS MANY FUNCTIONS WHICH WE CAN USE TO MANIPULATE THE STRING.

#1st QUESTION - WAP TO INPUT USER'S NAME AND PRINT ITS LENGTH?
# input_name = input("enter your name: ")
# print("length of your name is:", len(input_name)) # it will print the length of the string.

#2nd QUESTION - WAP TO INPUT USER'S FIRST NAME & PRINT ITS LENGTH?
# str = "hi, $iam the $ system $99.99"
# print(str.count("$")) # it will count the number of occurrences of the string.


                                                                       #CONDITIONAL STATEMENTS
#if-elif-else (syntax) is used to execute a block of code based on a condition. 
#if condition:only if the condition is true then the block of code will be executed.it is used to check a single condition.and give true or false value.

# light = "green"

# if (light == "red"):
#        print("stop")
# elif(light == "green"):# it will see first one thenafter that no other condition will be checked if the first one is true.
#        print("go")
# elif(light == "yellow"): 
#        print("look")
# print("end of code") # it will print the end of code coz it is not in the if-elif-else block. 

# IF → AGAR YE CONDITION TRUE HAI, TO YE CODE CHALAO.AUR YE CODE HAR BAAR CHECK HOGA.
# ELIF → AGAR PEHLI CONDITION FALSE HAI, TO IS CONDITION KO CHECK KARO.YE TABHI CHECK HOGA JAB PEHLI CONDITION FALSE HAI. AUR YE CODE HAR BAAR CHECK HOGA.
# ELSE → AGAR UPAR KI SAARI CONDITIONS FALSE HAIN, TO YE CODE CHALEGA. AUR YE CODE HAR BAAR CHECK HOGA.

# temperature = 25

# if temperature > 35:
#     print("It's very hot.")
# elif temperature == 25:
#     print("The weather is warm.")
# else :
#     print("It's cold.")
#     print("end of code") # it will print the end of code coz it is not in the if-elif-else block.


# IF CONDITION1:
    # CODE IF CONDITION1 IS TRUE

# ELIF CONDITION2:
    # CODE IF CONDITION2 IS TRUE

# ELSE:
    # CODE IF ALL CONDITIONS ARE FALSE

#conditional statements
# grade student based on marks
# marks >= 90: A
# 80 <= marks < 90: B
# 70 <= marks < 80: C
# marks < 70: D

# marks = int(input("enter marks of student :"))
# if (marks == 100):
#     print("A+")
# elif (marks >= 90):
#     print("A")
# elif (marks >= 80):
#     print("B")
# elif (marks >= 70):
#     print("C")       
# else:
#     print("D")
# print("grade of student is:", marks) # it will print the grade of student based on marks.


#NESTING = NESTING IS USED TO CHECK MULTIPLE CONDITIONS IN A SINGLE IF-ELIF-ELSE BLOCK. IT IS USED TO CHECK A CONDITION INSIDE ANOTHER CONDITION.
#its work like if the first condition is true then it will check the second condition and if the second condition is true then it will execute the block of code inside the second condition.

#Q for myself : 
#age = 80 #already but i modidify for myself
# age = int(input("enter a number: "))

# if (age >= 18):
#     if (age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")        


#QUESTION 1ST - WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS EVEN OR ODD.

# num = int(input("enter a number: "))

# if(num % 2 == 0):
#          print("even"   )
# else:
#          print("odd")         

#QUSETION 2ND - WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER.

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))     
# c = int(input("enter third number: "))                 
# 5,982,153

# if (a > b and a > c):
#     print("first is greatest number :", a) 
# elif (b >= c):
#     print("second is greatest number :", b)
# else:
#     print("third is greatest number :", c)        

# QUESTION 3RD - WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT.

# NUM = int(input("enter a number: "))

# if (NUM % 7 == 0):
#     print("multiple of 7") 
# else:
#     print("not a multiple of 7")

#LECTURE 3- LISTS & TUPLES IN THE PYTHON.

#LISTS ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE. LISTS ARE CREATED USING SQUARE BRACKETS [] AND ITEMS ARE SEPARATED BY COMMAS. LISTS ARE MUTABLE, MEANING WE CAN CHANGE THE VALUE OF THE LIST. LISTS ARE ORDERED, MEANING THE ORDER OF THE ITEMS IN THE LIST IS PRESERVED. LISTS CAN CONTAIN ITEMS OF DIFFERENT DATA TYPES.
#TUPLES ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE. TUPLES ARE CREATED USING PARENTHESES () AND ITEMS ARE SEPARATED BY COMMAS. TUPLES ARE IMMUTABLE, MEANING WE CANNOT CHANGE THE VALUE OF THE TUPLE. TUPLES ARE ORDERED, MEANING THE ORDER OF THE ITEMS IN THE TUPLE IS PRESERVED. TUPLES CAN CONTAIN ITEMS OF DIFFERENT DATA TYPES.

                                                       #LISTS IN PYTHON             
# marks = [90, 80, 70, 60, 50] # LIST IS A COLLECTION OF ITEMS WHICH ARE ORDERED AND CHANGEABLE. IT IS DEFINED BY SQUARE BRACKETS [].

# print(marks) # IT WILL PRINT THE LIST OF MARKS.
# print(type(marks)) # IT WILL PRINT THE TYPE OF MARKS WHICH IS LIST.
# print(marks[0]) # IT WILL PRINT THE FIRST ELEMENT OF THE LIST WHICH IS 90.
#IS STARTRED WITH 0 INDEX AND END WITH N-1 INDEX WHERE N IS THE LENGTH OF THE LIST.
# #STRINGS ARE IMMUTABLE BUT LIST IS MUTABLE MEANS WE CAN CHANGE THE VALUE OF THE LIST.

#LIST SLICING IS SAME AS STRING SLICING. WE CAN USE THE SAME SYNTAX TO SLICE A LIST.AND WE CAN USE THE SAME FUNCTIONS TO MANIPULATE A LIST AS WE USE TO MANIPULATE A STRING, IT IS BECAUSE LIST IS A COLLECTION OF ITEMS WHICH ARE ORDERED AND CHANGEABLE. IT IS DEFINED BY SQUARE BRACKETS [].

# students = ["ayush", "rahul", "rohit", "sachin"] # list of students.

# print(students) # IT WILL PRINT THE LIST OF STUDENTS.
# # print(students[0]) # IT WILL PRINT THE FIRST ELEMENT OF THE LIST WHICH IS AYUSH.
# students[0] = "amit" # IT WILL CHANGE THE FIRST ELEMENT OF THE LIST WHICH IS AYUSH TO AMIT, IT WILL NOT PRINT COZ OT ONLY CHANGE THE TEXT NO PRINT IN TERMINAL.
# print(students) # IT WILL PRINT THE LIST OF STUDENTS AFTER CHANGING THE FIRST ELEMENT TO AMIT
# print(students[0:4])# IT WILL PRINT THE LIST OF STUDENTS FROM INDEX 0 TO 3.
# print(students[-1:-4])# IT WILL PRINT THE LIST OF STUDENTS FROM INDEX -1 TO -3.BUT IT WILL NOT PRINT ANYTHING HERE COZ THE DEFAULT STEP DIRECTION IS $+1$ (LEFT-TO-RIGHT)
# print(students[-4:-1])# IT WILL PRINT THE LIST OF STUDENTS FROM INDEX -4 TO -2.

# list = [2,3,4,5]
# list.append(6)
# print(list) # THIS USED IN ADDING NUMBER IN THE LAST 

#SORTING = MEANS ARRANGING THE ELEMENTS IN A PARTICULAR ORDER. IN PYTHON WE CAN SORT THE LIST IN ASCENDING OR DESCENDING ORDER USING THE SORT() METHOD. THE SORT() METHOD SORTS THE LIST IN PLACE, MEANING IT MODIFIES THE ORIGINAL LIST AND DOES NOT RETURN A NEW LIST. THE SORT() METHOD TAKES AN OPTIONAL ARGUMENT REVERSE WHICH IS A BOOLEAN VALUE. IF REVERSE IS SET TO TRUE, THE LIST IS SORTED IN DESCENDING ORDER. IF REVERSE IS SET TO FALSE OR NOT PROVIDED, THE LIST IS SORTED IN ASCENDING ORDER.

# list= [6,2,3,4,1,8,6,7,]
# print(list.append(9)) # THIS USED IN ADDING NUMBER IN THE LAST
# print(list.sort()) # THIS USED IN SORTING THE LIST IN ASCENDING ORDER.
# print(list.sort(reverse=True)) # THIS USED IN SORTING THE LIST IN DESCENDING ORDER.
# print(list) # THIS USED IN PRINTING THE LIST AFTER SORTING.

#SORTING KA EK RULE HAI WO EK HI BAAR MEIN SAARE KO PRINT NHI KAREGA PEHLA EK KAAM KAREGA PHIR AAP PRINT LISTKAROGE TAB RESULT AAIYEGAA EK KA AAB AUR KARWANA HAI TOH USKO COMMENT OUT KARO YA NAYA CODE EXECUTE KARO.

# list= ["apple", "banana", "orange", "mango", "pineapple"] 
# print(list.sort()) #ITS USED IN SORTING THE LIST IN ASCENDING ORDER IN ALPHABETICAL ORDER.
# #print(list.sort(reverse=True)) # THIS USED IN SORTING THE LIST IN DESCENDING ORDER.
# print(list) # THIS USED IN PRINTING THE LIST AFTER SORTING.

# list= ["a", "e", "i", "o", "u"]
# list.reverse() # THIS USED IN REVERSING THE LIST.
# print(list) # THIS USED IN PRINTING THE LIST AFTER REVERSING.

# list= [3, 1, 4, 2, 5]
# list.insert(3, 9) # THIS USED IN INSERTING AN ELEMENT AT A SPECIFIC INDEX IN THE LIST.
# #HERE 3 IS THE INDEX WHERE WE WANT TO INSERT THE ELEMENT AND 9 IS THE ELEMENT WE WANT TO INSERT.
# print(list) # THIS USED IN PRINTING THE LIST AFTER INSERTING THE ELEMENT

# #INDEXING = MEANS FINDING THE POSITION OF AN ELEMENT IN THE LIST. IN PYTHON WE CAN FIND THE INDEX OF AN ELEMENT IN A LIST USING THE INDEX() METHOD. THE INDEX() METHOD TAKES AN ARGUMENT WHICH IS THE ELEMENT WE WANT TO FIND THE INDEX OF. IF THE ELEMENT IS FOUND IN THE LIST, IT RETURNS THE INDEX OF THE FIRST OCCURRENCE OF THE ELEMENT. IF THE ELEMENT IS NOT FOUND IN THE LIST, IT RAISES A VALUEERROR.

# list= [3, 1, 4, 1, 2, 5]
# list.remove(4) # THIS USED IN REMOVING AN ELEMENT FROM THE LIST.ITS REMOVE FIRST 1 FROM THE LIST.AND ANY ELEMENT WHICH IS DOUBLE TIME IN THE LIST THEN IT WILL REMOVE THE FIRST ONE.

# print(list) # THIS USED IN PRINTING THE LIST AFTER REMOVING THE ELEMENT.

# list= [3, 1, 2, 4, 2, 5]
# list.pop(3) # THIS USED IN REMOVING THE LAST ELEMENT FROM THE LIST.
# print(list) # THIS USED IN PRINTING THE LIST AFTER REMOVING THE ELEMENT.

# #INDEXING = MEANS FINDING THE POSITION OF AN ELEMENT IN THE LIST. IN PYTHON WE CAN FIND THE INDEX OF AN ELEMENT IN A LIST USING THE INDEX() METHOD. THE INDEX() METHOD TAKES AN ARGUMENT WHICH IS THE ELEMENT WE WANT TO FIND THE INDEX OF. IF THE ELEMENT IS FOUND IN THE LIST, IT RETURNS THE INDEX OF THE FIRST OCCURRENCE OF THE ELEMENT. IF THE ELEMENT IS NOT FOUND IN THE LIST, IT RAISES A VALUEERROR.


                                                        #TUPLES IN PYTHON

# tup = (1, 2, 3, 4, 5) # TUPLE IS A COLLECTION OF ITEMS WHICH ARE ORDERED AND UNCHANGEABLE. IT IS DEFINED BY PARENTHESES ().
# print(tup[0]) # IT WILL PRINT THE FIRST ELEMENT OF THE TUPLE WHICH IS 1.
# print(tup) # IT WILL PRINT THE TUPLE.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS TUPLE.

# tup = ()
# print(tup) # IT WILL PRINT AN EMPTY TUPLE.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS TUPLE.



# tup = (1,)
# print(tup)# IT WILL PRINT A TUPLE WITH A SINGLE ELEMENT WHICH IS 1.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS TUP


# tup = (1)
# print(tup) # IT WILL PRINT AN INTEGER WHICH IS 1.COZ IT IS NOT A TUPLE, IT IS AN INTEGER.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS INT.


# tup = (1.0)
# print(tup) # IT WILL PRINT A FLOAT WHICH IS 1.0.COZ IT IS NOT A TUPLE, IT IS A FLOAT.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS FLOAT.


# tup = ("HELLO")
# print(tup) # IT WILL PRINT A STRING WHICH IS HELLO.COZ IT IS NOT A TUPLE, IT IS A STRING.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS STR.
#HERE IT IS A STRING COZ IT IS NOT A TUPLE, IT IS A STRING. TO MAKE IT A TUPLE WE HAVE TO ADD A COMMA AFTER THE STRING.
#COMMA IS USED TO MAKE A TUPLE WITH A SINGLE ELEMENT. IF WE DON'T ADD A COMMA AFTER THE STRING, IT WILL BE CONSIDERED AS A STRING AND NOT A TUPLE.

# tup = ("hello",)
# print(tup) # IT WILL PRINT A TUPLE WITH A SINGLE ELEMENT WHICH IS HELLO.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS TUP
# #HERE IT IS FLOAT COZ COMMA IS USED TO MAKE IT A TUPLE. IF WE REMOVE THE COMMA THEN IT WILL BE A STRING.


# tup = (1, 2, 3, 4, 5)
# print(tup) # IT WILL PRINT THE TUPLE.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS TUPLE.
#HERE COMMA IS NOT USED AT THE LAST BECAUSE IT IS A TUPLE WITH MULTIPLE ELEMENTS. COMMA IS ONLY USED TO MAKE A TUPLE WITH A SINGLE ELEMENT. IF WE DON'T ADD A COMMA AFTER THE STRING, IT WILL BE CONSIDERED AS A STRING AND NOT A TUPLE.


# tup = (1, 2, 3, 4, 5,)
# print(tup) # IT WILL PRINT THE TUPLE.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS TUPLE.
# #HERE COMMA IS USED AT THE LAST BECAUSE IT IS A TUPLE WITH MULTIPLE ELEMENTS. COMMA IS ONLY USED TO MAKE A TUPLE WITH A SINGLE ELEMENT. IF WE DON'T ADD A COMMA AFTER THE STRING, IT WILL BE CONSIDERED AS A STRING AND NOT A TUPLE.BUT IT IS NOT NECESSARY TO ADD A COMMA AT THE LAST OF A TUPLE WITH MULTIPLE ELEMENTS. IT IS OPTIONAL. BUT IT IS A GOOD PRACTICE TO ADD A COMMA AT THE LAST OF A TUPLE WITH MULTIPLE ELEMENTS. IT WILL HELP US TO ADD MORE ELEMENTS IN THE FUTURE WITHOUT HAVING TO MODIFY THE LAST ELEMENT.

# tup = (5,)     # tuple ✅
# tup = (5)      # integer ❌

# tup = (1, 2, 3, 4, 5)
# print(tup[1:4]) # IT WILL PRINT THE TUPLE.
# print(type(tup)) # IT WILL PRINT THE TYPE OF TUPLE WHICH IS TUPLE.
# #SLICING IS SAME AS STRING SLICING. WE CAN USE THE SAME SYNTAX TO SLICE A TUPLE. AND WE CAN USE THE SAME FUNCTIONS TO MANIPULATE A TUPLE AS WE USE TO MANIPULATE A STRING, IT IS BECAUSE TUPLE IS A COLLECTION OF ITEMS WHICH ARE ORDERED AND UNCHANGEABLE. IT IS DEFINED BY PARENTHESES ().



# tup = (1, 2, 3, 4, 5)
# print(tup.index(3)) # IT WILL PRINT THE INDEX OF THE ELEMENT 3 WHICH IS 2.
# #IT IS USED TO FIND THE INDEX OF AN ELEMENT IN A TUPLE. IF THE ELEMENT IS NOT FOUND IN THE TUPLE, IT WILL RAISE A VALUEERROR.

# tup = (1, 2, 3, 4, 5, 3 ,3 ,3 )
# print(tup.count(3)) # IT WILL PRINT THE COUNT OF THE ELEMENT 3 WHICH IS 4.
# #IT IS USED TO FIND THE COUNT OF AN ELEMENT IN A TUPLE. IF THE ELEMENT IS NOT FOUND IN THE TUPLE, IT WILL RETURN 0.

                                                        

#QUESTION 1 - WAP TO ASK THE USER TO ENTER OF THEIR 3 FAVOURITE MOVIES AND STORE THEM IN A LIST?
 
movies= []

#FIRST WAY TO DO THAT 

# mov1 = input("enter your first favourite movie: ")
# movies.append(mov1)
# mov2 = input("enter your second favourite movie: ") 
# movies.append(mov2)
# mov3 = input("enter your third favourite movie: ") 
# movies.append(mov3)

#HERE WE SAW THAT HOW WE ADD THE MOVIES IN LIST WITH ANOTHER METHOD USING APPEND

#ANOTHWER WAY OF DOING THIS


# movies.append(input("enter your first favourite movie: "))
# movies.append(input("enter your second favourite movie: "))
# movies.append(input("enter your third favourite movie: "))

#THIS PRINT SHOULD BE AT LAST TOE ADDED LIST,
# print(movies)

#QUESTION 2 - WAP TO CHECK IF A LIST CONTAIN A PALONDROME OF ELEMENTS.?
#A (PALINDROME) IS A WORD, PHRASE, NUMBER, OR SEQUENCE THAT READS THE SAME FORWARD AND BACKWARD.

# 👉 Palindrome = Same when read forward and backward.
# 121   → 121 ✅
# 1331  → 1331 ✅
# 123   → 321 ❌


# list1 = [1,2,3]
list2 = [1,2,1]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#    print("palindrome")
# else:
#      print("NOT palindrome")

#      #FOR SECOND ONE


# copy_list2 = list2.copy()
# copy_list2.reverse()

# if(copy_list2 == list2):
#    print("palindrome")
# else:
#      print("NOT palindrome")



#HERE IS THE BREAKDOWN OF EACH SECTION.SO, FIRST WE DO COPY OF LIST AND  THEN WE DID THAT REVERSE AND AFTER THAT WE COMPARE THE ORIGINAL LIST WITH THE REVERSED COPY LIST AND THEN WE FIND OUT THE ITS IS PALINDROME OR NOT.

# #QUESTION 3 - WAP TO COUNT THE NUMBER OF STUDENT  WITH THE "A" GRADE IN THE FOLLOWING TUPLE?
# #CONDITION - STORE THE VALUE IN A LIST & SORT THEM FROM "A" TO "D".

# grade = ["c", "d", "a", "a","a","b","b"]
# grade.sort()
# print(grade)


# LECTURE 4 - DICTIONARY & SETS IN PYTHON

                                                        #DICTIONARY IN PYTHON
#we cannot duplicate the keys

# info = {
#       "key" : "value",
#       "name" : "gajodhar",
#       "learning" : ["coding","c++","java","html"],
#       "age" : "65",
#       "topis" : ("dict","ses"),
#       "in_adults": "true",
#       "marks" : "99.9",
#       "99.9" : "34.6"
# }                                                       

# print(info)
# print(info["key"])
# print(info["name"])
#A dictionary in Python stores data as key-value pairs. We use square brackets [] to get a value using its key. For example, info["name"] means find the "name" key inside info and give me its value, which is "gajodhar". Similarly, info["age"] gives "65".
# We use [] because dictionaries are accessed using keys. () is used for calling functions, and . is generally used for accessing methods or attributes. So remember: Dictionary → dict["key"] → value.

# null_dictiponary ={}
# null_dictiponary["name"] = "ayyush kumar"
# print(null_dictiponary)

# info = {
#         "key" : "value",
#         "subjects" : {
#                       "maths": "99.9",
#                       "english" :"99.9",
#                       "hindi" : "99",
#         }

#  }
# print(info)
# print(type(info))

# print(list(info))


#ayush

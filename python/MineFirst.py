# LECTURE 1 - VERIABLE AND DATA TYPES

# FOR COMMENET OUT  USE CTRL + /
#(      )  -  PARENTHESIS
# [      ]  -  SQUARE BRACKETS
#"   "  -  DOUBLE QUOTES
# '   '  -  SINGLE QUOTES
# <    >  -  LESS THAN AND GREATER THAN
# =    -  EQUAL TO
# : THE COLON IS USED TO DEFINE A BLOCK OF CODE IN PYTHON. IT IS USED TO DEFINE THE START OF A BLOCK OF CODE. IT IS USED TO DEFINE THE START OF A FUNCTION, CLASS, LOOP, IF STATEMENT, ETC.

import string


# name = "ayush"
# age = 18
# price = 35.99

# print("my name is: ",name)
# print ("my age is :",age)


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

#print(a + b) # no answer coz string cannot sum with float

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

#str[startindex:endindex:step] # ending index is exclusive.
# str = "asunix"
# print(str[1:5]) # it will print from 0 to 3 index character.

# str = "apna college"
# print(str[0:4]) # it will print from 0 to 2 index character.
# print(str[0:len(str)]) # it will print whole string coz ending index is exclusive and len(str) is 12 so it will print from 0 to 11 index character.
# print(str[0:])# it will print whole string coz ending index is exclusive and len(str) is 12 so it will print from 0 to 11 index character.

                                                
# str = "apna college"
# print(str[-1]) # it will print the last character of the string.
# print(str[-4:0]) # it will print from -4 to -2 index character. 

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

# age = 80

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

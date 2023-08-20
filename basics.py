'''
#first program
print("hello world","hello suhani")
print(5)
print(18*16)

#comments


print("hello \"friends\"") 
print("hello 'friends'")
print("hello",5,6, sep="-",end="8888\n")

#variables 
a= 10
e=110
b= "harry"
c=True
d=None
print("type of a is ", type(a))
print(a+e)
print("type of b is ", type(b))
print("type of c is ", type(c))
print("type of d is ", type(d))

#variables are used so that we can store whatever we want in them 
#variables are used so that we can modify the value of same variable from different places 

#operators
a= 15
b= 5 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #remove value after points 
print(a**b) #a*a*a*b
print(a%b) 

#typecasting 

a= "5"
b= "2"
print(int(a)+int(b))
#types of typecasting: implicit- automatic, explicit-done by programmers
string="4"
num=5
string_number= int(string)
sum= num+string_number 
print("the sum of both values are", sum)
#implicit typecast 
a=5.5
b=2
print(a+b)

#input 

a= input("enter your name: ")
print(a)
b= input("enter b value")
c= input("enter c value")
print(b+c)
print(int(b)+int(c))
 
 '''

#strings 
# name = "harry"
# friend= "garry"
# sentence= '''hey harry
# how are you 
# i love your content 
# goodbye harry
# '''
# print(name)
# print(friend)
# print(sentence)
# print(name[0])
# # for all charaters we use loop
# for char in name:
#     print(char)

# #string slicing 
# print(name[1])
# print(name[0:3]) #include 0 but not 3
# print(name[:4])  #include 0 to 3
# print(name[:]) #include whole length
# print(len(name))
# print(name[-3:-1])

# if else  

# num= int(input("enter the value of num: "))

# if(num!=0):
#     if(num<10):
#         print("number is between 1-10")
#     elif(num<20):
#         print("number is between 10-20")
#     else:
#         print("number is greater than 20")
# else:
#     print("number is zero")

# project 

# import time

# timestamp= time.strftime('%H:%M:%S')
# print("time right now is:", timestamp)

# hours=int(time.strftime('%H'))

# if(hours>=0 and hours<=12):
#     print("GOOD MORNING CHAMP")
# elif(hours>12 and hours<=15):
#     print("GOOD AFTERNOON CHAMP")
# elif(hours>15 and hours<=19 ):
#     print("GOOD EVENING CHAMP")
# else:
#     print("GOOD NIGHT CHAMP")

# switch case 

# age=int(input("enter your age: "))

# match age:
#     case _ if(age>0 and age<=4):
#         print("you're a baby")
#     case _ if(age>4 and age<13):
#         print("you're a kid")
#     case _ if(age>=13 and age<17):
#         print("you're a teen")
#     case _:
#         print("you're an adult")

# for loop

# name="kapil is a joker"
# for alps in name:
#     print(alps)


# for i in range(1,6,2):  #(start,stop,step) 
#     print(i)

# name=["red","blue","green","yellow"]
# for color in name:
#     print(color)
#     for alp in color:
#         print(alp)

# table 
'''num= int(input("enter your number: "))

for i in range(1,11):
    print(num,"x",i,"=",num*i )'''

# while loop
# the loop will continue until we enter the desired value 

'''num= int(input("enter the value: "))
print(num)
while(num<=38):
    num=int(input("enter the value: "))
    print(num)
else:
    print("code exits successfully")'''

# do while loop in python
'''
list1=["Meta","Apple","Amazon","Netflix","Google"]
i=0
size=len(list1)
while(True):
    print(list1[i])
    i=i+1
    if(i<size and list[i]<10):
        continue
    else:
        break

'''
# Exercise 1: Print First 10 natural numbers using while loop
'''
i=1
while(i<=10):
    print(i)
    i=i+1 '''
# Write a program to print the following number pattern using a loop.
'''
for i in range(1,6):
    for j in range(1,i):
        print(j, end=" ")
    print(" ")
'''


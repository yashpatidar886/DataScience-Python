  print("Hello MindCoders")

# yash Patidar
'''i 
am 
yash patidar'''         

print("How")
print("are")
print("you")
print("yash")
age=4
print(age)
print(type(age))

age ="Four"
print(age)
print(type(age))

name = "Yash Patidar"
profession = "Software Developer"
exceperience = 4

print("Hello , I am", name, "I am a ",profession,"Professionaly . And I hae around", exceperience, "years of experience with it !")

x  =5 
print(x,type(x))
x="Hello World"
print(x,type(x))
x =20
print(x,type(x))
x =20.5
print(x,type(x))
x =1j
print(x,type(x))
x = ["Apple" ,"Banana", "Cherry"]
print(x,type(x))
x = ("Apple" ,"Banana", "Cherry")
print(x,type(x))
x= range(6)
print(x,type(x))
x = {"name" ,"Jhon" ,"age " , 36 }
print(x,type(x))
x = {"Apple" ,"Banana", "Cherry"}
print(x,type(x))
x =frozenset({"Apple" ,"Banana", "Cherry"})
print(x,type(x))
x =True
print(x,type(x))
x =b"Hello"
print(x,type(x))
x=bytearray(5)
print(x,type(x))
x = memoryview(bytes(5))
print(x,type(x))
x = None
print(x,type(x))

#Arithmetic opretors

print("10+2", 10+2)
print("10-2", 10-2)
print("10*2", 10*2)
print("10/2", 10/2)
print("10%2", 10%2)
print("10//2", 10//2)
print("2**3", 2**3)


# Assigment opreters

#compuond opreters

x=  5
print(x)
x+=3
print(x)
x-=2
print(x)
x *=3
print(x)
x /=2
print(x)
x //=3
print(x)
x**=2
print(x)
x =5
x %=3
print(x)
x |=2
print(x)
x ^=3
print(x)

#Comparison Opreters (== , != , > ,< , >= ,<=)
a = 10
b =20
print("a ==b :" , a==b)
print("a ==10 :" , a==10)

print("a !=b :" , a!=b)
print("a !=a :" , a!=a)

print("a >b :" , a>b)
print("a <b :" , a<b)
print("a<=b:", a<=b)
print("a>=b:", a>=b)
print("a>=10:", a>=10)

#Logical Opreters (AND ,OR ,NOT)
x = 4
print(x < 5 and x <10 )
print(x <5 or x <4)
print(not(x < 5 and x <10))
y =4
print(x is y)
print(x is not y)

#Identity Opreters (is ,is not) 

# x = ["Maruti","BMW"]
y = ["Maruti","BMW"]
z =x
print(x is y)
print(x is not y)
print(y is z )
print(y is not z)
print(x is z)
print(x is not z)

x = 10 
y =10 
print(x is y)
print(x is not y)

x = ("Maruti","BMW",)
y =("Maruti","BMW",)
print(x is y)
print(x is not y)

# Membership oprerters

x = ["Maruti","BMW"]
y = ["Maruti","BMW"]
print(x is y)

print("Maruti " in x)
print("Maruti " not in x)

# Bitwise opreters
x = 10   #    0000 1010
y = 20   #    0001 0100

print (x&y)  # AND opreter
print(x|y)   # OR opreter
print(x^y)   # XOR opreter
print(~x)    # NOT opreter
print(~y)    # NOT opreter
print(x <<2) # Left side 
print(y <<2) # Left side
print(x<<2)  # Right side
print(x<<2)  # Right side


#  User Input 
name = input("Please enter yoyr name : ")
print("hello" , name)
age = input("please enter your age :")
print("Hello" , name ,"Your name ", age , "Years old ")
phone = input("Enter your phone number :"
print("Contact Number " , phone)
email = input("Enter your email :")
print("email " , email)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

z = x + y

print("Sum of two numbers:", z)

x = input("Enter first number: ")
y =int(input("Enter second number: "))
z = int(x)+int(y)
print(z)


x =  int(input("Enter a number :"))
y = int(input("Enter a number : "))
z = x-y
print("Sub " , z)

x =  5
input("Enter a number :")
y = input("Enter a number : ")
z = x+y
print("Sum " , z)


x = float(input("Enter a First Len : "))
y = float(input("Enter a Second Len : "))

h = (x**2+y**2)**.5
h = (x ** 2 + y **2 )**1/2
print("Hypotenuse length is", h)




print("+----------+")
print("|          |")
print("|          |")
print("|          |")
print("|          |")
print("|          |")
print("+----------+")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5 , end="")
print("+" + 10 * "-" + "+")

city = 'bhopal'
print(city[0])
print(city[2])
print(city[-1])
print(city[-5])

print(2==2)
print(2==2.2)
var = 0
print(var==0)
var == 1
print(var == 0)

var = 10
if var ==11:
   print("Var is 11")
print("HEllo")   

yash  = 11 
if yash==11:
    print("yash is 11")

num1 = int(input("Enter a First number "))
num2 = int(input("Enter a Second  number "))

if num1 > num2 :
   larger_num = num1
else :
   larger_num = num2 
   
print("Larger number is : ", larger_num)   
   
   

num1 = int(input("Enter a First number "))
num2 = int(input("Enter a Second  number "))
num3 = int(input("Enter a Third  number "))
if num1 > num2 and  num1 >num3 :larger_num = num1
elif   num2 >num3 and num2 >num1: larger_num = num2
else :  larger_num = num3
   
   
print("Larger number is : ", larger_num)   
   
   
num1 = int(input("Enter a First number "))
num2 = int(input("Enter a Second  number "))
num3 = int(input("Enter a Third  number "))

largest_num = max(num1,num2,num3)
minmum = min(num1,num2,num3)
print("Largest  number is : ", largest_num)  
print("Minimum number is  " ,minmum)

while True:
   print("I an Stack in a loop")

largest_number = -99999
number = int(input("Enter a number or type -1 to stop"))

while number !=-1:
   if number>largest_number:
     largest_number=number
     number = int(input("Enter a number or type -1 to stop"))
     
print("largest number is :",largest_number)     


user = str(input("Enter a sentence : "))

if user == "Spathiphyllum":
  print("Yes - Spathiphyllum is the best plant ever!")
elif user=="spathiphyllum":
  print("No, I want a big Spathiphyllum!")
else:
  print("Spathiphyllum! Not", user + "!")

income = float(input("Enter income :"))

if income<=85528:
    tax = income*0.18-556.2
    if tax <0:
        tax = 0
        
else:
    tax=14839.02+(income-85528)*0.32
print("the tax is " , round(tax) , "thalers")     

while number !=-1:
   if number>largest_number:
     largest_number=number
     number = int(input("Enter a number or type -1 to stop"))
     
print("largest number is :",largest_number)     
       


number =  int(input("Enter a number : "))
even_count  =0
odd_count =0
while number !=0:
    if number % 2==0:
        even_count +=1
    else:
        odd_count +=1  
    number =  int(input("Enter a number : "))     
print("Even :" , even_count)
print("odd :" , odd_count)        
    
num = [1,2,3,4]
print(num[3])
print(bool(4))
print(bool(6))
print(bool(-1))
print(bool(0))            
        
print(bool("a"))
print(bool("b"))
print(bool(" "))
print(bool(""))    

print(bool())
print(bool(None))
print(bool(null))    
            
counter =5
while counter!=0:
    print("Inside the loop " , counter)
    counter -=1
print("Outside the loop") 


counter =5 
while counter :
    print("Inside the loop " , counter)
    counter -=1
print("Outside the loop")                    

for counter in range(10):
    print("counter :" , counter)

for counter in range(2,8):
    print("Counter :" , counter)     

print("The break instructions : ")
for counter in range (1,6):
    if counter == 3:
      break
    print("Inside the loop",counter)
print("Outside the loop")     
    
    
print("The break instructions : ")
for counter in range (1,6):
    if counter == 3:
     continue
    print("Inside the loop",counter)
print("Outside the loop")       

largest_number = -99999
counter =0

while True:
    number = int(input("Enter a number or type -1 to end the program "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number
if counter !=0:
    print("The largest number is " , largest_number)
else:
    print("You haven't enter a number")            
        
        
largest_number =-9999999
counter = 0

while number != -1:
    if number ==-1:
        continue
    counter +=1
    
    if number > largest_number:
         largest_number = number
    number = int(input("Enter a number or type -1 to end the program "))
    
if counter:
    print("The largest number is " , largest_number)
else:
    print("You haven't enter a number")                  

counter =1 
while counter <5:
    print(counter)
    counter +=1
else:
    print("ELse" , counter)    
    
counter =5
while counter <5:
    print(counter)
    counter +=1
else:
    print("ELse" , counter)    


for counter in range (5):
    print(counter)
else:
    print("else " , counter)     
     
counter = 111
for counter in range (2,1):
   print(counter )
else:
    print("else", counter )        


     
blocks = int(input("Enter numbber of blocks : "))
counter = 0
while(blocks - counter > 0):
    counter +=1
    blocks = blocks - counter 
    
# print("height of paryamid : " , counter) 




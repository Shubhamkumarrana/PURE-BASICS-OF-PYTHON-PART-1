#string slicing
a= "shubham kumar rana"
print(a[::-1])      #pallindrome number
print(a[::])
ration =["rice","wheat","turmeric","and","so ","on"]
print(ration)
print(ration[1:2])
print(ration[::-1])
ration1 =["rice","wheat","turmeric","and","so ","on",5,69]
print(ration1[-1:])
num=[2,9,5,3,7]
num.sort() #for sortin in ascending
num.reverse()   #for sorting in descending
print(num[2::4])
print(max(num)) #to print the maximum number
print(min(num)) #to print the minimum number
num.append("45")  #to add number or string into the list,we uses append function
num.insert(3,56)  #to insert the string or number at a defined position
num.remove(3)  #to remove
print(num)
num.pop() #to delete the number from end
""" difference between list and tuple is-- list is mutable(can be changed), while on the other hand 
tuple-is immutable(cannot be changed), list is reprentated by [] and tuple is reprentated by ()"""
DICTIONARY
di={"shubham":"pizza","amit":"chole_bhatura","priya":{"visesh":"fish","prasant":"chicken"}}
print(di["shubham"])
di.update({"rudra":"junk food"})
print(di)
print(di["priya"]["visesh"])

dis={'tupple':'540265.32','list':'54131331', 'string':'+65685686'}
disc=input("enter data")
print(dis[disc])
"""exmaple1:----make a disctionary with user input to serach the meaning and also if  the word is not 
available the also print the word to be not available"""
dict={"shubham":"learner"}   #we can add  more words in this disctionary
print("enter the word")
key=input()
if key in dict:
    print("meaning of the  word is:-",key)
    print("\t",dict[key])
else:
    print(key,"not present in the dictionary! try again")

"""exercise 2::--- this is a small program which asks user to give proper age  as input for driving"""
age=int(input("what is your age"))
if age < 80:
    if age > 18:
        print("you can drive")
    elif age == 18:
        print("you have to apply for the license first")
    else:
        print("wrong data")
else:
    print("you have entered wrong age which does not meets the system requirement")


"""exercise 3::::design a calculator which will correctly solve all the arthematic operations except some operations like division"""
print("enter number a")
a=int(input())
print("enter number b")
b=int(input())
if a == 85 or 66 or 54 and b == 96 or 89 or 22:
    print("try again!!!")
    exit(0)
print("which operation you want: +    -    *    / ")
x = input()
if x == "+":
        print("a+b=",a+b)
elif x == "-":
        print("a-b=",a-b)
elif x == "*":
   print("a*b=",a*b)
elif x == "/":
        print("a/b=",a/b)
else:
        print("wrong choice",x)



list=[["shubham",78687],["ajay",87946],["ankita",97897],["minu",786093]]
disc1=dict(list)
print(disc1)
for item,number in disc1.items(): #if you want to print the all whole disc
    print(item,"is the family member of",number)
for item in disc1:   #if you want ot print only the key
    print(item)

"""write a program to create a pattern of stars by askkng the user"""
a=int(input("enter height"))
b=int(input("enter width"))
for a in range(0,b):
    for b in range(0,a):
        print("*",end=" ")
        b=b+1
    print("\r")

"""write a game in which user have to guess a hidden a number,
user is limited to guess only 5times """
import random

n=random.randint(0,10)

print("WELCOME")
print("HI!! you are given only 5 chances to guess a number")
for b in range(0,5):
    print("\n\n Guess the number below 10,")
    a = int(input())
    if a == n:
        print("correct answer is",n,"you guessed it right")
        for d in range(0,5):
                print("GREAT!!!! YOU WON")
        break

    elif a>=10:
        print("out of range....try again!!")

    else:
        print("wrong guessing....try again!!")
        print(5-b,"chances remaining")

        continue
    for d in range (0,5):
        print("\n YOU LOST!!!!",end="  ")

"""comparison operators like"""
""" double equals to(==),less than(<),greater than(>),not (!),less than or equalsto(<=),greater than or equals to(>=)"""

"""LOGICAL OPERATORS::-->  AND,OR , NOT """
"""IDENTITY OPERATORS --> IS"""
"""MEMBERSHIP OPERATOR--> IN"""
"""BITWISE OPERATOR--> IT WORKS WITH BINry numbers"""

""":FILE HANDLING"""

"""for reading ===    f = open("file name.txt")
for writing ====      f = open("file name.txt","w")
                      f.write("data")
                      f.close()


for writing after or adding  ===    f = open("file name.txt","a")
                                    f.write("data") 
                                    f.close()

for writing and reading together===  f = open("file name.txt","r+")
                                     f.write("data")   
                                     f.close()"""

"""f=open("shubham.txt","a")
f.write("i am in bca 4th sem\n")

f.close()"""




#PROGRAM TO CHECK THE NUMBER IS PALLINDROME OR NOT


n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")



#TO CHECK THE LARGEST AND SMALLEST NUMBER
num1=int(input("Enter First Number"))
num2=int(input("Enter Second Number"))
num3=int(input("Enter Third Number"))
if (num1> num2 and num1> num3):
    print("The Largest number is", num1)
elif (num2 > num1 and num2> num3):
    print ("The Largest number is", num2)
else:
    print ("The Largest number is", num3)



#TO CHECK ARMSTRONG NUMBER
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



#PROGRAM TO DISPLAY FIBONACCI SERIES
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1




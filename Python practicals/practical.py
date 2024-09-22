# 1. practical
print("Hello, World!")


# 2. practical
str1="hello"
str2="world"
concate_str= str1+" "+str2
print(concate_str)


# 3. practical
a=4
b=5
sum=a+b
print("Your Sum is : ",sum)


# 4. practical
print("My Name Is Lakhan")
print("My Age is 18")
print("I am in 5th semester")
print("I am pursuing in full time diploma")


# 5. practical 
num1= int(input("Enter Your Number 1 : "))
num2= int(input("Enter your Number 2 : "))
sum= num1+num2
print("sum is : ", sum)


# 6. practical
num1= int(input("Enter Your 1st Number : "))
num2= int(input("Enter Your 2nd Number : "))
sum = num1+num2
print("the sum is : ", sum)


# 7. practical
a=int(input("Enter 1st num : "))
b=int(input("Enter 2nd num : "))
c=int(input("Enter 3rd num : "))
d=int(input("Enter 4th num : "))
e=int(input("Enter 5th num : "))
avg=(a+b+c+d+e)/5
print("The Average is : ", avg)


# 8. practical
p=int(input("Enter the principal : "))
r=int(input("Enter the Rate : "))
t=int(input("Enter the Time : "))
simple_interest=(p*r*t)/100
print("The Simple Interest is : ", simple_interest)


# 9. practical
name= "Lakhan"
print(name[: : -1])


# 10. practical
a=int(input("Enter 1st num : "))
b=int(input("Enter 2nd num : "))
if a>b:
    print("largest number is ", a)
else:
    print("largest number is ", b)


# 11. practical
num=int(input("Enter Your num : "))
if num==0:
    print("num is ", num)
elif num > 0:
    print(num, "is positive")
else :
    print(num, "is negative")


# 12. practical
a=input("Enter your string : ")
b=int(input("Enter Your index : "))
if (b<len(a)) :
    print(a[b])
else:
    print("Enter smaller than", len(a), " index ")


# 13. practical
a=input("Enter your string : ")
b=int(input("Enter Your first index : "))
c=int(input("Enter Your last index : "))
d = c+1
if (d<len(a)) :
    print(a[b:d:1])
elif (b>c+1):
    print("string index can't be smaller then last index")
else:
    print("Out of Rate")


#14.practical 
a=int(input("Enter 1st num : "))
b=int(input("Enter 2nd num : "))
c=int(input("Enter 3rd num : "))
if (a>b and a>c):
    print(a, "is greater")
elif (b>c):
    print(b, "is greater")
else:
    print(c, "is greater")


# 15. practical
marks=int(input("Enter Your Marks : "))
if (marks<=100 and marks>=91):
    print(" A Grade ")
elif(marks<=90 and marks>=75):
    print("B Grade")
elif(marks<=74 and marks>=60):
    print("C Grade")
elif(marks<=59 and marks>=45):
    print("D Grade")
elif(marks<=44 and marks>=33):
    print("E Grade")
else:
    print(" oops! you are Fail ")


# 16. practicsl
bs=int(input("Enter Your Basic Salary : "))
if (bs == 20000):
    print("Yor Total Salary = ",bs)
elif (bs > 20000 and bs<=30000):
    da = bs*(10/100)
    hra = bs*(5/100)
    ts = bs+da+hra
    print("Yor Total Salary = ",ts)
elif (bs > 31000 and bs<=50000):
    da = bs*(8/100)
    hra = bs*(8/100)
    ts = bs+da+hra
    print("Yor Total Salary = ",ts)
elif (bs > 50000):
    da = bs*(5/100)
    hra = bs*(15/100)
    ts = bs+da+hra
    print("Yor Total Salary = ",ts)
else:
    print("!! Enter A Valid Basic Salary !!")



# 17. practical
num= int(input("Enter Your Number : "))
if(num % 2 == 0 and num % 5 == 0):
    print("Fizz and Buzz")
elif(num % 2 == 0):
    print("Fizz")
elif(num % 5 == 0):
    print("Buzz")
else:
    print("Nither Fizz or Buzz")


#18. practical
unit=int(input("Enter You Unit : "))
subsidie=200
if (unit<=200):
    print("Your Bill Is Free")
if (unit>=201 and unit<=400):
    bill=unit*9-subsidie
    print(bill,"Rs/-")
elif (unit>=401 and unit<=600):
    bill=unit*15-subsidie
    print(bill,"Rs/-")
else :
    print("Eror Not founded")
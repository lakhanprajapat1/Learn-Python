# count vowals in string 
str=(input("enter str: ")).lower()

vowals="aeiou"
count=0
for char in str:
    if char in vowals:
        count+=1
print("total vovals in string: ",count)

# reverse a string 
str=input("enter a string: ")
print(str[::-1]) 

# check string is palendrome.
str=input("enter a string: ").lower()
reverse_str=str[::-1]
if(str==reverse_str):
    print(str,"is palendrome")
else:
    print(str,"is not palendrome")

#find common charactor in two strings
str1=input("enter first string: ")
str2=input("enter second string: ")

set1=set(str1)
set2=set(str2)
common=set1 & set2

if common:
    print("common char in this strings is","".join(common))
else:
    print("nothing is common")

# to find odd or even number
a=int(input("enter a num: "))

if  (a % 2 ==0):
    print(a,"is even number")
else:
    print(a,"is odd number")
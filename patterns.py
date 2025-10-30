# math=int(input("enter a number:"))
# phy=int(input("enter a number:"))
# chem=int(input("enter a number:"))
# total=math+phy+chem
# print(total)
# avg=total/2
# print(avg)

# a=int(input("enter a number:"))
# if a%2==0:
#     print("a is even")
# else:
#     print("a is odd")

# check whether the given num is +ve or-ve
# num=float(input("enter a number:"))
# if num>0:
#     print("given num is postive")
# else:
 
#  print("given num is negative")

# smallest num
# num1=9
# num2=5
# if num1<num2:
#     print("num1 is smallest")

# else:
#     print("num2 is smallest")

# leap year
# year=int(input("enter a year:"))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print("year is leap year")
# else:
#     print("not a leap year")

# while True:
#     num=int(input("enter a num:"))
#     if num <= 0:
#         print("number is negative")
#         break


# n=10
# sum=n*(n+1)/2
# print(sum)

# write a prgm to read 1st 10 numbers and print the sum
# sum=0
# for i in range(10):
#     num=float(input("enter a num:"))
#     sum+=num
#     print(sum)

# sum of 1st and last digit is euqal to middle num
# a=int(input("enter a num:"))
# first=a//100
# middle=(a//100)%10
# last=a%10
# if first + last == middle:
 
 
#  print("yes")
# else:
#  print("no")


# marriage=input("enter your marriage status:")
# age=int(input("enter your age:"))
# gender=input("enter your gender:")
# if marriage:
#     print("yes")
# else:
#     if gender=="male" :
#         if age>30:
#             print("yes")
#     else:
#         print("no")
#         if gender=="female" :
#          if age>25:

#              print("yes")
#          else:
#                 print("no")

# read charcters continously until$
# num=0
# while True:
#     char=input("enter a char:")
#     if (char=='$'):
#         print(num)
#         break
#     num+=1

# char=input("enter your name:")
# if char.islower():
#     print("lower")
# else:
#      char.isupper()
#      print("upper")


# upper case to lower case
# char=input("enter your name:")
# upper_case=char.upper()
# lower_case=char.lower()
# print(upper_case)
# print(lower_case)

# name=input("enter yur name:")
# n=int(input("enter how many tomes you want to print yoyr name"))
# for i in range(n):
#     print(name)     

# n=int(input("enter a num"))
# if n%2==0:

#     sum=n*(n+1)/2

#     print(sum)

# num = 2
# while True:
#     print(num)
#     num += 2

# for i in range(1,100):
#     print(f"{i:2}",end="")

#     if i%5==0:
#         print(i)

# n=int(input("enter a num:"))


# prime number
# num=int(input("enter a num:"))
# if num>1:
#     for i in range(2,num):

#         if num % i==0:
#             print("num is not prime")
#             break
#     else:
#         print("prime")
    
# in colum
# for i in range(1,100):
#     print(f"{i:2}",end='')
#     if i%5==0:
#         print()
# in line
# for i in range(1,100):
#     print(f"{i:2}", end="")
#     if i%5==0:
#         print("|",end="")


# 3*3 matrix
# element=[]
# for i in range(9):
#     value=int(input(f"enter a element {i+1}:"))

#     element.append(value)
#     print("\n matrix((3 x 3):")
#     for i in range(0,9,3):

#         print(element[i],element[i+1] ,element[i+2])



# elements = []

# # Read 9 elements
# for i in range(9):
#     value = int(input(f"Enter element {i+1}: "))
#     elements.append(value)

# # Now print the 3×3 matrix
# print("\nMatrix (3 x 3):")
# for i in range(0, 9, 3):
#     print(elements[i], elements[i+1], elements[i+2])


# multiplication table
# num=int(input("enter a num:"))
# for i in range(11):
#     print(f"{num}*{i}={num*i}")


# number=[10,20,30,40,50,799]
# biggest= max(number)
# print(biggest)

# second smallest number and its position






# Read numbers
# num = list(map(int, input("Enter numbers: ").split()))

# # Find smallest
# num=[1,3,4,5,6,7,8]
# smallest = min(num)
# # Copy list and remove smallest
# num_copy = num.copy()
# num_copy.remove(smallest)
# # Find second smallest
# second_smallest = min(num_copy)
# print("Second smallest number is:", second_smallest)

# for i in range(1,100):
#     if i%3==0 and i%7==0:
#         print(i)


# prgm to find total num of +ve,-ve and zeros of a 10 real nums
# postive=0
# negative=0
# zero=0
# print("enter 10 numbers")
# for i in range(10):
#     num = float(input(f"Number {i+1}: "))

#     if num>0:
#         positive+=1

#     elif num<0:
#             negative+=1
        
#     else:
#             zero+=1
#             print(positive)
#             print (   negative)
#             print(zero)



# # Program to find total number of positive, negative, and zeros from 10 real numbers

# positive = 0
# negative = 0
# zero = 0

# print("Enter 10 numbers:")

# for i in range(10):
#     num = float(input(f"Number {i+1}: "))

#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zero += 1

# # Print totals after the loop
# print("\nTotal positive numbers:", positive)
# print("Total negative numbers:", negative)
# print("Total zeros:", zero)


# num=int(input("enter a num:"))
# sum_of_divisors=0
# for i in range(1,num):
#     if num %i==0:
#      sum_of_divisors+=i
# if sum_of_divisors==num:
#         print("is perfect")
# else:
#         print("nooo")


# i=int(input("enter a num"))
# for i in range(10):
#     if i%2==0:

#         print("even")
#         pass
#         break
#     else:
#         print("odd")
#         continue

# salary=int(input("enter a num"))
# age=int(input("enter a num"))
# for i in range(salary):
#     if salary==0:
#         break
#     elif salary>5000 and age>40:
#         pass
#     elif salary>75000 and age<40:
#         print("tax is 10%")
#     elif salary<5000:
#         print("salary is low")
#         continue

# num=int(input("enter a num:"))  
# for i in range(1,num):
#     print(f"{num}*{i}={num*i}")

#     if i==11:

#         break
#     else:
#         continue



    






             

    




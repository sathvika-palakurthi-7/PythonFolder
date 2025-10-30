# def max_num(a,b,c):
#     return max(a,b,c) 
# print(max_num(1,2,3))
 
# def count_vowles(s):
    
#     return sum(1 for char in s if char.lower() in 'aeiou') 
# print (count_vowles("hello world"))


# def factorial(n):
#     if n==0:
#        return 1
#     return n* factorial(n-1)
# print(factorial(4))


# l = []
# l = list()
# l.app

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*i
#         return f
# print(fact(5))

# import math
# print(math.factorial(5))

# text = "success"
# for char in set(text):
#     if text.count(char) > 1:
#         print(char)


# def factorial(n):
#     if n==0:
#         return 1
#     return n* factorial(n-1)
# print(factorial(4))


# str="sathwika"
# int=str
# print(int)

# def area_of_rec(l,w):
#     return l*w
#     print(area_of_rec(5,3))

# dic1={"a":1, "b":2}
# dic2={"a":1, "c":2}
# merge={**dic1 ,**dic2}
# print(merge)

# list1=[1,2,3]
# list2=[4,5,6,3]
# common=list(set(list1)&set(list2))
# print(common)

# list1=[1,2,3,4,5,6,7]
# list2=[5,6,7,8]
# common=list(set(list1) & set(list2))
# print(common)

# list1=[1,1,2,2,3,3,4,4,5,7,9,9]
# repnum=list(set(list1))
# print(repnum)


# def palindrom(s):
#     return s==s[::-1]
# print(palindrom("radar"))
# print(palindrom("hello"))

# def longest_word(sentence):
#     word=sentence.split()
#     return max(word, key=len)
# print (longest_word ("abc defghij k l mnop qrst uvw"))


# def first_non_repeating_char(s):
#     for char in s:
#         if s.count(char) == 1:
#             return char
#     return None

# print(first_non_repeating_char("nxtwave"))  # Output: 'n'


# def repeatedchar(s):
#     for char in s:
#         if s.count (char)==2:
#             return char      
# print(repeatedchar("sathwika"))


# str1 = "Hello"
# str2 = "World"
# result = str1  +""+ str2
# print(result) #Hello World


# def even_num(n):
#     if n%2==0:
#         print("even num")
#     else:
#         print("odd")
# even_num(9)


# def reverse(s):
#     result=""
#     for  char in s:
#      result=char+result
#     return result
    
# print(reverse("sathwikaa"))


# i=0
# while(i<3):
    
#     print(i)
# i=i+1

   

# def non_repetain_char(s):
#     for char in s:
#         if s.count(char)==1:
#             return char
#             return none
# print(non_repetain_char("sathwika"))



# def upper_case(u):
#     return sum(1 for char in u if char.isupper())
# print(upper_case("Sathwika"))


# def upper(s):
#     return s.upper()
# print(upper("sathwika"))


# def reverse(s):
#     return s[::-1]
# print(reverse("sathwika"))


# arrays

# arr=[1,2,3]
# reverse_arr=arr[::-1]
# print(reverse_arr)

# arr=[1,2,3,4,5]
# total=sum(arr)
# print("sum",total)

# arr=[50,100,50,100]
# n=sum(arr)
# print("sum",n)

# arr=[50,100,50,100]
# avg=sum(arr)/len(arr)
# print("avg",avg)

# arr=[50,10,30]
# avg=sum(arr)/len(arr)
# print(avg)

# arr1=[1,2,3,4]
# arr2=[5,6,7,8]
# sum=arr1+arr2
# print(sum)

# arr=[1,2,4,5,6]
# n=6
# total=n*(n+1)//2
# sum_arr=sum(arr)
# missing=total-sum_arr
# print(missing)

# def nonrep(arr):
#     arr=[1,1,2,3,4,4,5,6,8,8,9]
#     for num in arr:
#         if arr.count(num==1):
#             return arr
# print(nonrep)

# arr=[1,1,2,2,3,3,4,5,5]
# arr=sorted(set(arr))
# print(arr)


# number of characterss print
# text="hello world"
# count=0
# for char in text:
#     if char.isalpha():
#      count+=1
# print(count)        


# # repeted char count print
# text="hello world"
# for char in set(text):
#     print(char, "=" ,text.count(char))


# text="hello world"
# for char in set(text):
#     print(char,"=",text.count(char)) 


# def repe(n):
#     for char in n:
#         if n.count(char)>0:
#             return char
# print(repe("hello world"))
  

# def duplicate_arr(a):
#     for num in set(a): 
#         if a.count(num)>1:
#             print(num)
# duplicate_arr([1,1,2,2,4,6,7,8,8,8])


# def rep(a):
#     for num in set(a):
#         if a.count(num)>1:
#             print(num)
            
# rep([1,1,2,6,5,5,7,8,0,2,2,5,6])
       

# def duplicate_char(c):
#     for char in set(c):
#         if c.count (char)>1:
#             return char
# print(duplicate_char("hello world"))



# text="sdfghjk"
# print(text.capitalize())

# list=[1,3,2,4]
# list.sort()
# print(list)


# word = "hello"

# for i in range(len(word)):
#     print(i, word[i])


# names = ["A", "B", "C"]
# scores = [90, 85, 88]

# for name, score in zip(names, scores):
#     print(f"{name} scored {score}")



# for i in range(12):

#     print("5 * " ,"i=" ,5* i) 
#     if (i==5):
#         break

# i=0
# while i<5:
#     i+=1
#     if i==3:
#         continue
    # print(i)


# list=[1,2,3,4] 
# list.append(6)
# print(list)
 


# def reverse(list):
#         return list[::-1]

# list=[1,2,3,4,5]
# print(reverse(list))

# def duplicate(lst):
#     unique=[]
#     for item in lst:
#         if item not in unique:
#             unique.append(item)
#     return unique
        
# lst=[10,10,20,20,30,30]

# print(duplicate(lst))


# list=[ ifor i in range(10)]
# print(list)


# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def fibanocie(n):
#     if n==0 or n==1:
#         return 0
#     else:
#         return fibanocie (n-1) + fibanocie (n-2)
# print(fibanocie(42))
    


# print( f"{2*30}")


# class person:
#     name="harry"
#     occu="se"
#     networth=10
# a=person()
# print(a.name)
# print(a.occu)
# print(a.networth)

# encapsulation
# class student:
#     def __init__(self):
#         self.__name="ravi"
#     def show_name(self):
#         print("student name is:" ,self.__name)
# s1=student()
# s1.show_name()


# class Person:
#     def walk(self):
#         print("Person walks")

# class Student(Person):
#     def study(self):
#         print("Student studies")

# class Dog:
#     def speak(self):
#         print("Woof!")

# class Cat:
#     def speak(self):
#         print("Meow!")
# d=Dog()
# c=Cat()
# d.speak()
# c.speak()
  
# class circle:
#     def area(self):
#         num=float(input("enter the value of the radius:"))
#         result = 3.14159 * r * r
#         print("area of circleis:",result)
        
# class rec:
#     def area(self):
#         l=float(input("enter the value of l:"))
#         b=float(input("enter the value of b:"))
#         result=l*b
#         print("area of rec is:",result)  
# c=circle()
# re=rec()
# c.area()
# re.area()  
#                 
# decoraters are the way to modify extend behaviour of the func withut changing the actula code
# defined as @deocraters_name

# text="hello"


# num = int(input("Enter a 3-digit number: "))

# a = num // 100         # hundreds place
# b = (num // 10) % 10   # tens place
# c = num % 10           # ones place

# if (a**3 + b**3 + c**3) == num:
#     print(num, "is an Armstrong number.")
# else:
#     print(num, "is NOT an Armstrong number.")

# count freguency of yoyr word
# a="sathwika"
# d={}
# for char in a:
#     if char in d:
#         d[char]=+1
#     else:
#         d[char]=1        
# print(d)
    
# for i in range(1,6):

#     for j in range(5,i-1):
#         print(j,end='')
#     print()


# for i in range(5,0,-1):
#     for j in range(5,i,-1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         print(k,end="")
#     print()



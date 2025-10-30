# 1.Find the Missing Number: You are given a list of n-1 integers from a range of 1 to
#  n. There are no duplicates in the list. Your task is to find the one integer that is
#  missing from the list.

# list1=[1,2,4,5,6,9]
# n=9
# total=n*(n+1)//2
# sum=sum(list1)
# missing=total-sum
# print(missing)

# l1=[1,2,4,5,6,9]
# n=9
# missing_num=[]
# for i in range(1,n+1):
#     if i not in l1:
#         missing_num.append(i)
# print(missing_num)

# 2. Two Sum: Given a list of integers and a target number, find the indices of the two
#  numbers in the list that add up to the target. You can assume that each input has
#  exactly one solution and you may not use the same element twice.
# l1=[1,2,5,6]
# target=7
# for i in range(len(l1)):
#     for j in range(i+1, len(l1)):
#         if l1[i] + l1[j]==target:
#             print(i,j)

# from itertools import combinations
# l1=[1,2,5,6]
# target=7
# for(a,b,c) in combinations(enumerate(l1), 3):
#     if a[1]+b[1]+c[1]==target:
#         print(a[0],b[0],c[0])

    


#3. Reverse a String: Write a program that takes a string as input and returns the
#  string with its characters in reverse order. For example, "hello" should become
#  "olleh".

# def reverse(s):
#     return s[::-1]
# print(reverse("hello"))

# def reverse(s):
#     result=""
#     for  char in s:
#      result=char+result
#     return result
# print(reverse("hello"))

#4. Anagram Check: Given two strings, write a function to determine if the second
#  string is an anagram of the first. An anagram is a word or phrase formed by
#  rearranging the letters of another, such as "cinema" and "iceman".

# str1="cinema"
# str2="iceman"
# if sorted(str1)==sorted(str2):
#     print("the given strings are angrams")
# else:
#     print("no")

#5.Find Duplicates in a List: You are given a list of integers. Your task is to find and
#  return all the elements that appear more than once in the list.
# def duplicates(l1):
#     unique=[]
#     for item in l1:
#         if item not in unique:
#             unique.append(item)
#     return unique
# l1=[1,1,2,2,3,3,4,5,6,9,9]
# print(duplicates(l1))


#6. Palindrome Check: Write a function that checks if a given string is a palindrome.
#  A palindrome is a word, phrase, or sequence that reads the same backward as
#  forward, e.g., "madam" or "racecar".
# def palindrome(s):
#      return s==s[::-1]
# print(palindrome("madam"))

# text="madam"
# reverse_text=text[::-1]
# if reverse_text==text:
#      print("the given text is palindrome")
# else:
#      print("no")


# 7. FizzBuzz: Write a program that prints the numbers from 1 to 100. For multiples of
#  three, print "Fizz" instead of the number. For multiples of five, print "Buzz". For
#  numbers which are multiples of both three and five, print "FizzBuzz".

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("fizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# 8. Word Frequency Counter: Given a sentence, count the frequency of each word
#  and return the result as a dictionary where keys are the words and values are their
#  counts.

# s = list(input("Enter a sentence: ").split(" "))
# d = {}
# for i in s:
#     word = i.strip()  # remove extra spaces
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)


# 9.Matrix Transpose: You are given a 2D list (a list of lists) representing a matrix.
#  Your task is to find the transpose of the matrix, which means swapping the rows
#  and columns.

# matrix=[[]]








# 12. Find the First Non-Repeating Character: Given a string, find the first character
#  that does not repeat and return its index. If there is no such character, return -1.

# def non_repeating(c):
#     for char in c:
#         if c.count(char)==1:
#             return c.index(char)
#             return -1
# print(non_repeating("ssathwika"))


# 14.Find Common Elements in Two Lists: Given two lists, write a function to find
#  and return a list containing all the elements that are common to both lists. The
#  result should not contain duplicates.
# def function():
#  l1=[10,20,30,4,5,6,25]
#  l2=[10,99,88,6,76,25]
#  common=list(set(l1)&set(l2))
#  return common
# print(function())  



# 15.Group Anagrams: You are given a list of strings. Your task is to group the
#  anagrams together. The output should be a list of lists, where each inner list
#  contains words that are anagrams of each other

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# anagram={}
# for word in words:
#     key=''.join(sorted(words))
#     if key not in anagram:
#         anagram[key]=[word]
#     else:
#         anagram[key].append(word)
# print(list(anagram.values()))




#16. Find the Longest Substring Without Repeating Characters: Given a string, find
#  the length of the longest substring that does not contain any repeating
#  characters.

# def longest_substring(s):
#     word=s.split()
#     count=+1
#     return count
# print(longest_substring("abc def ghijkl mnkohdhdhjbsdub"))


#19. Check for a Subsequence: Given two strings, s and t, check if s is a
#  subsequence of t. A subsequence is a new string formed from the original string
#  by deleting some (or none) of the characters without disturbing the relative
#  positions of the remaining characters.

s="abc"
t="ahbgdc"
i=0
j=0
while i<len(s) & j<len(t):
    if s[i]==t[j]:
        i+=1
        j+=1
    if i==len(s):
            print("s is a substring")
    else:
            print("s is not a substing")


# s = "abc"
# t = "ahbgdc"

# i = 0  # pointer for s
# j = 0  # pointer for t

# while i < len(s) and j < len(t):
#     if s[i] == t[j]:  # match found
#         i += 1
#     j += 1

# if i == len(s):
#     print("s is a subsequence of t")
# else:
#     print("s is NOT a subsequence of t")




# 20.Find Pairs with a Given Sum: Given a list of numbers and a target sum, find all
#  pairs of numbers in the list that add up to the target sum. Return the result as a
#   list of tuples.
# l2=[]
# l1=[1,2,3,4,5,6]
# target=6
# for i in range(len((l1))):
#     for j in range(i+1,len(l1)):
#         # print(i,j)
#         if l1[i]+l1[j]==target:    
#             l2.append((l1[i],l1[j]))
# print(l2)

# str1="listen"
# str2="silent"
# a=sorted(str1)
# b=sorted(str2)
# if a==b:
#     print("yes")
# else:
#     print("no")





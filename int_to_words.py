#A simple python program to print an integer between 1 to 9999 in words
n=int(input('please enter an integer between 1 and 9999: '))

#Defining the required numbers in words in a dictionary with key value pairs
words = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
          8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
          14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
          19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
          70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred", 1000:"thousand"}

#if number is in thousands
if n//1000 >= 1:
    y = n//1000
    print(words[y], "thousand", end=" ")

#removing the "thousand" part of the number
x = n%1000

#if last 3 digits of the number is in hundreds
if x//100 >= 1:
    y = x//100
    print(words[y], "hundred", end=" ")

#removing the "hundred" pat of the number
x = n%100


if x//10 > 1:       #if last two digits of number is more than or equal to 20
    y = x//10
    print(words[y*10], end=" ")
    y = x%10
    if y:           #if number has a digit in once's place other than digit 0
        print(words[y])
else:
    if x:           #if last two digits of number is not 0
        print(words[x])

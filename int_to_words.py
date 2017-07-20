#A simple python program to print an integer between 1 to 9999 in words
number=int(input('please enter an integer between 1 and 9999: '))

#Defining the required numbers in words in a dictionary with key value pairs
words = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
          8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
          14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
          19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
          70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred", 1000:"thousand"}

#if number is in thousands
if number//1000 >= 1:
    temp_number = number//1000
    print(words[temp_number], "thousand", end=" ")

#removing the "thousand" part of the number
remainder = number%1000

#if last 3 digits of the number is in hundreds
if remainder//100 >= 1:
    temp_number = remainder//100
    print(words[temp_number], "hundred", end=" ")

#removing the "hundred" pat of the number
remainder = number%100


if remainder//10 > 1:       #if last two digits of number is more than or equal to 20
    temp_number = remainder//10
    print(words[temp_number*10], end=" ")
    temp_number = remainder%10
    if temp_number:           #if number has a digit in once's place other than digit 0
        print(words[temp_number])
else:
    if remainder:           #if last two digits of number is not 0
        print(words[remainder])

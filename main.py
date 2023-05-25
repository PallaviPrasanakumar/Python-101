# print("Hello world")
# print(10)
# print(20)
# print(10 , end=" and ")
# print(30)
# print(10,20,20,sep=" ,,",end=" and ")
# print(40)
# print("Hello world", "I am Pallavi","I m 26 years old" ,sep=",",end=".")
#
# multi_line_string="""
# Hello Wolrd
# Pallavi
# """
# print(multi_line_string)
#
# # print("Hello we are at demo of calculator application.")
# # print("Enter the first number", end=" ")
# # x = int(input())
# # print("Enter the second number", end=" ")
# # y = int(input())
# #
# # print("")
# # print("Sum is :" ,x + y)
#
# print(ord("a"))
# x='a'
# print(ord(x) - ord('a'))
#
# x=10
# y=20
# print(x+y)
# print(str(x) + str(y))
#
# x=chr(48)
# print(x)

"""
write a program to determine if year is leap
It is divisble by 100 , then it must be divisble by 400
else divisible by 4
"""
# print("Enter a year")
# year=int(input())
#
# if year % 400 == 0:
#     print("Year is leap year"
# elif year % 4 == 0 and year % 100 !=0 :
#     print("Year is leap year")
# else:
#     print("year is not  a leap year")

#write a program to print multiplication table of 3
print("Multiplication table for 3")
for i in range(1,11):

    print(3,"x" ,i, "=" , 3*i)
#write mulyiplication table from 1 to 5
for i in range(1,6):
    print("----------Multiplication table for for ",i)
    for j in range(1,11):
        print(i,"x",j, "=",i*j)

#Print the pattern

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end =" ")
    print("")

for i in range(0,4):
    for j in range(0,4):
        if j>= 3-i:
            print("*",end="")
        else:
            print(" ",end="")
    print("")

for i in range(0,4):
    for j in range(0,7):
        if 3-i <=j <= 3+i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")

def print_message():
    print("Hello I'm inside the function")

print("Before function")
print_message()
print("AFter function")

from math_function import power

print(power(2,3))


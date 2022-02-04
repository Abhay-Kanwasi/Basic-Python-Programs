# First import array all components

from array import *
from itertools import count

# 88 Ask the user for a list of five integers. Store them in an array, Sort the list and display it in reverse order.

# nums = array('i', []) # Here we created an blank array
# for i in range (0,5):
#     num = int(input("Enter a number : "))
#     nums.append(num) #here we add elements to it.
# nums = sorted(nums)
# nums.reverse()

# print(nums)



# 89 Create an array which will store a list of integers. Generate five random numbers and store them in the array Display the array(showing each item on a seperate line).

# import random
# nums = array('i',[])
# for i in range(0,5):
#     num1 = random.randint(1,61)
#     nums.append(num1)
# for i in nums:
#     print(i)



# 90 Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array, otherwise display the message "Outside the range". Once five numbers have been successfully added, display the message "Thank you" and display the array with each item shown on a seperate line.

# 1

# nums = array('i',[])
# for arr in range(0,5): #for loop misses first number in array
#     num = int(input("Enter a  number :"))
#     if num >= 10 and num <= 20: # We don't use 'or' operator here because in this program we have to satisfied both the conditions.
#         nums.append(num)
#     else:
#         print("Outside the range!")
# print("Thank you!")

# for i in nums:
#     print(i)

# 2

# nums = array('i', [])

# while len(nums) <= 5:
#     num = int(input("Enter a number between 10 and 20 :"))
#     if num >= 10 and num <= 20:
#         nums.append(num)
#     else:
#         print("Outside the range")

# for i in nums:
#     print(i)



# 91 Create an array which contains five numbers(two of which should be repeated). Display the whole array to the user. Ask the user to enter one of the numbers from the array and then display a message saying how many times that number appears in the list.

# nums = array('i',[2,3,2,4,3])
# print(nums)
# num = int(input("Choose a number from the array :"))
# print(nums.count
# (num))



# 92 Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers). Join these two arrays together into one large array. Sort this large array and display it so that each number appears in the seperate line.

# import random

# num1 = array('i',[])
# num2 = array('i',[])

# for i in range(0,3):
#     num = int(input("Enter a number: "))
#     num1.append(num)

# for i in range(0,5):
#     num = random.randint(1,100)
#     num2.append(num)

# num1.extend(num2)

# num1 = sorted(num1)

# for i in num1:
#     print(i)




# 93 Ask the user to enter five numbers. Sort them into order and present them to the user. Ask them to select one of the numbers. Remove it from the orignal array and save it in a new array.

# num = array('i',[])
# for i in range(0,5):
#     number = int(input("Enter a number :")) 
#     num.append(number) 
# num = sorted(num)
# for i in num:
#     print(num)
# num1 = int(input("Choose a number you want to remove :"))
# if number in num:
#     num.remove(num1)
#     num2 = array('i',[])
#     num2.append(num1)
#     print(num)
#     print(num2)
# else:
#     print("That is not a value in the array.")



# 94 Display an array of five numbers. Ask the user to select one of the numbers. Once they have selected a number, display the position of that item in the array, If they enter something that is not in the array, ask them to try again untill they select a relevent item.

# num = array('i',[])
# for i in range(0,5):
#     num1 = int(input("Enter a number :"))
#     num.append(num1)
# print(num)    
# num2 = int(input("Select a number from array : "))
# tryagain = True
# while tryagain == True:
#     if num2 in num:
#         print("This is in position",num.index(num2))
#         tryagain = False
#     else:
#         print("Not in array")
#         num = int(input("Select one of the number: "))


# 95 Create an array of five numbers between 10 and 100 which have two decimal places. Ask the user to enter a whole number between 2 and 5. If they enter something outside of that range, display a suitable error message and ask them to try again until they enter a valid amount. Divided each of the numbers in the array by the number the user entered and display the answers shown to two decimal places.

# import math
# #we take 5 decimal numbers in the array
# nums = array('f',[34.75,27.23,99.58,45.26,28.65])
# tryagain = True
# while tryagain == True:
#     num = int(input("Enter a number between 2 and 5 :"))
#     if num<2 or num >5:
#         print("Incorrect value, try again.")
#     else:
#         tryagain = False

# for i in range(0,5):
#     ans = nums[i]/num
#     print(round(ans,2)) # this print our answer in 2 decimal places.



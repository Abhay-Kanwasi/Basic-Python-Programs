#27 Ask the user to enter a number with lots of decimal places. Multiply this number by two and display the answer.

#introduce float

# num = float(input("Enter a number with a lot of decimal places :"))
# answer = 2 * num
# print(answer)


#28 Update program 27 so that it will display the answer to two decimal places.

# num = float(input("Enter a number :"))
# answer = num*2
# print(answer)
# print(round(answer, 2)) #introduce round


#29 Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places.

# import math
# num = int(input("Enter an integer that is over 500 : "))
# answer = math.sqrt(num) #introduce of square root
# print(round(answer, 2))

#30 Display pi to five decimal places

#without importing math

# pie = 22/7
# print(round(pie, 5))

#with importing math
# import math
# print(round(math.pi,5))

#31 Ask the user to enter the radius of a circle (measurement from the center point to the edge). Work out the area of the circle (pir*r square)

# import math
# radius = float(input("Enter the radius of the circle : "))
# area = math.pi * radius * radius
# print(round(area,2))

#32 Ask for the radius and the depth of a cylinder and work out the total volume(circle area*depth) rounded to three decimal places.

# import math
# radius = int(input("Enter the radius :"))
# depth = int(input("Enter the depth :"))
# area = math.pi * (radius**2)
# volume = area*depth
# print(round(volume,3))

#33 Ask the user to enter two numbers. Use whole number division to divide the first number by the second and also work out the remainder and display the answer in a user-friendly way(e.g. if they enter 7 and 2 display "7 divide by 2 is 3 with 1 remaining")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# division = num1//num2 
# remainder = num1%num2
# print(num1, "divided by", num2, "is", division, "with", remainder, "remaining")

#34 Display the following message :
# (1) Square
# (2) Triangle
# Enter a number :
# If the user enters 1, then it should ask them for the length of one of its sides and display the area. If they select 2, it should give them a suitable error message.

# print("1) Square")
# print("2) Triangle")
# print()
# menuselection = int(input("Enter a number :"))
# if menuselection==1:
#     side = int(input("Enter the length of one side: "))
#     area = side*side
#     print("The area of your chosen shape is ", area)
    
# if menuselection==2:
#     base = int(input("Enter the length of the base : "))
#     height = int(input("Enter the height of the triangle : "))
#     area = (base*height)/2
#     print("The area of your chosen shape is ", area)
# else:
#     print("Incorrect option selected. Please! check and try again !")
    


# 80 Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space betweeen and display the result. Finally, display the length of their full name(including the spaces)

# name = input("Enter your first name :")
# print(len(name))
# surname = input('Enter your surname :')
# print(len(surname))
# fullname = name + " " + surname
# print(fullname)
# print(len(fullname))


# 81 Ask their user to type in their favourite school subject. Display it with  "-" after each letter.

# sub = input("Enter your fav school subject :")
# for letter in sub:
#     print(letter,end= "-")


# 82 Show the user a line of text from your favouriter poem and ask for a starting and ending point. Display the characters between those two points.

# word = ("Zindagi swaar du ek naye bhar du duniya hi badal du ma to pyaara sa chamatkaar hu ")
# print(word)
# spoint = int(input("Enter the starting point : "))
# lpoint = int(input("Enter the ending point :"))
# print(word[spoint:lpoint])


# 83 Ask the user to type in a word in uppercase.If they type it in lower case, ask them to try again. Keep repeating this until they type in a msessage all in uppercase.


# uname = input("Enter your name in capital : ")
# tryagain = False
# while tryagain == False:
#     if uname.isupper():
#         print("Thank you")
#         tryagain = True
#     else:
#         print("Try again")
#         uname = input("Enter a message in uppercase: ")


# 84 Ask the user to type in their postcode. Display the first two letters in uppercase.

# postcode = input("Enter the postcode :")
# start = postcode[0:2]
# print(start.upper())


# 85 Ask the user to type in their name and then tell them how many vowels are in their name.

# count = 0
# name = input("Enter your name: ")
# name = name.lower()
# for x in name:
#     if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#         count = count + 1
# print(count,"vowels in the name.")


# 86 Ask the user to enter a new password. Ask them to enter again. If the two passwords match, display "Thank you", If the letters are correct but in the wrongcase, display the message "They must be in the same", otherwise display the message "Incorrect".

# new = input("Enter a password :")
# confirm = input("Enter the password :")
# if new == confirm:
#     print("Thank you !")
# elif new.lower() != confirm.lower():
#         print("They must be in the same.")
# elif new.capitalize != confirm.capitalize:
#             print("They must be in the same.")
# else:
#     print("Incorrect!")



# 87 Ask the user to type in a word and then display it backwards on seperate lines. For instance, if they in "Hello" it should display the opposite word "olleH" one word at a line.

# word = input("Enter a word :")
# length = len(word)
# num = 1
# for x in word:
#     position = length - num
#     letter = word[position]
#     print(letter)
#     num = num + 1


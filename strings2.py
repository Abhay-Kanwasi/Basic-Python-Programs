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


uname = input("Enter your name in capital : ")
tryagain = False
while tryagain == False:
    if uname.isupper():
        print("Thank you")
        tryagain = True
    else:
        print("Try again")
        uname = input("Enter a message in uppercase: ")

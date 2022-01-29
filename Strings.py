#20 Ask the user to enter their first name and then display the length of their name.

# name = input("Enter their first name : ")
# length = len(name) #len is used for counting the characters
# print(length)

#21 Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name.

# name = input("Enter your first name :")
# surname = input("Enter your surname :")
# full_name = name + " " + surname
# length = len(full_name)
# print(full_name, "and the length is : ", length)

#22 Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together.Display the finished result.

# name = input("Enter your name : ")
# name = name.title()
# surname = input("Enter your surname : ")
# surname = surname.title()
# full_name = name + " " + surname
# print(full_name)

#23 Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1).

# line = input("Enter a nurserry line :")
# length = len(line)
# start = int(input("Enter the starting number :"))
# end = int(input("Enter the ending number :"))
# part = (line[start:end])
# print(part)

#24 Ask the user to type in any word and display it in upper case.

# word = input("Enter a word :")
# word = word.upper()
# print(word)

#25 Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter their surname and join them together(without a space) and display the name in uppercase. If the length of the first name is five or more characters, display their first name in lower case.


# Option 1
# name = input("Enter your first name: ")
# length = len(name)
# if length<5:
#     surname=input("Enter your surname: ")
#     fullname = name + surname
#     fullname = fullname.upper()
#     print(fullname)
# else:
#     name= name.lower()
#     print(name)

# Option 2
# name = input("Enter your first name: ")
# if len(name)<5:
#     surname = input("Enter your surname:")
#     name = name+surname
#     print(name.upper())
# else:
#     print(name.lower)


#26 Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an "ay". If a word begins with a vowel you just add "way" to end, For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is dispalyed in lower case.

word = input("Please enter a word:")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "o" and first != "i" and first != "u":
    newword = rest+first+"ay"
else:
    newword = word + "way"
    print(newword.lower())
    










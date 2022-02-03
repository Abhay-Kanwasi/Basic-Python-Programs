# 69 Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the countries that have been shown to them and then display the index number(i.e position in the list) of that item in the tuple.

# country_tuple = ("India", "America", "Canada", "Japan","Pakistan")
# print(country_tuple)
# print()
# country = input("Choose a country name : ")
# print( country, "has index number", country_tuple.index(country))

# 70 Add to program 69 to ask the user to enter a number and display in that country.

# country_tuple = ("India", "America", "Canada", "Japan","Pakistan")
# print(country_tuple)
# print()
# country = input("Choose a country name : ")
# print( country, "has index number", country_tuple.index(country))
# print()
# choose = int(input("Enter a number betweem 0 to 4 :"))
# print("This index number has ", country_tuple[choose], "country")

# 71 Create a list of two sports. Ask the user what their favourite sport is and add this to the end of the list. Sort the list and display it.

# sport_list = ["Kabbadi","Cricket"]
# sport_list.append(input("Enter your favorite sport : "))
# sport_list.sort()
# print(sorted(sport_list))

# 72 Create a list of six school subjects. Ask the user which of these subjects they don't like. Delete the subject they have chosen from the list before you display the list again.


# subject_list = ["Hindi", "English", "Science", "Maths", "Sanskrit", "Soc-Science"]
# print(subject_list)
# subject_list.remove(input("Enter the subject you want to remove :"))
# subject_list.sort()
# print(sorted(subject_list))


# 73 Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with numbers starting from 1. Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list. Sort the remaining data and display the dictionary.

#This is how we add in dictionary with proper indexing
# food_dictionary = { }
# food1 = input("Enter a food you like :")
# food_dictionary[1] = food1 #here we store it in dictionary
# food2 = input("Enter a food you like :")
# food_dictionary[2] = food2
# food3 = input("Enter a food you like :")
# food_dictionary[3] = food3
# food4 = input("Enter a food you like :")
# food_dictionary[4] = food4
# print(food_dictionary)
# dislike = int(input("Which of these food you don't want : "))
# del food_dictionary[dislike] #here we delete that item from dictionary
# print(sorted(food_dictionary.values()))

# 74 Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number between 5 and 9. Display the list for those colors between the start and end number the user input.

# color_list = ["red","blue","green","yellow","pink","violet","white","black","orange","purple"]
# print(color_list)
# num = int(input("Enter a starting number between 0 and 4 :"))
# num1 = int(input("Enter a ending number between 5 and 9: "))
# print(color_list[num:num1])


# 75 Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a seprate line. Ask the user to enter a three-digit number. If the number they have typed in matches one in the list, display the position of that number in the list, otherwise display the message "That is not in the list".


# num_list = [ 321, 222, 231, 333, 2122, 213, 761]
# print(num_list)
# #We want it to print in seperate line which is not possible by \n in the list. So for this we use loop
# for i in num_list:
#     print(i)
# selection = int(input("Enter a three digit number :"))
# if selection in num_list:
#     print(selection, "is in position", num_list.index(selection))
# else:
#     print("That is not in the list.")


# 76 Ask the user to enter the names of three people they want to invite to a party and store them in a list. After they have entered all three names, ask them if they want to add another. If they do, allow them to add more names until they answer "no". When they answer "no". display how many people they have invited to the party.


# name1 = input("Enter a name of somebody you want to invite : ")
# name2 = input("Enter a name of somebody you want to invite : ")
# name3 = input("Enter a name of somebody you want to invite : ")
# party = [name1,name2,name3]
# another = input("Do you want to invite another(y/n): ")
# while another == "y":
#     newname = party.append(input("Enter that name : "))
#     another = input("Do you want to invite another(y/n) :")
# print("You have", len(party),"people coming to your party .")




#77 Change program 76 so that once the user has completed their list of names, on the list. Display the position of that name in the list. Ask the user if they still want that person to come to the party. If they answer "no", delete that entry from the list and display the list again.


# name1 = input("Enter a name of somebody you want to invite : ")
# name2 = input("Enter a name of somebody you want to invite : ")
# name3 = input("Enter a name of somebody you want to invite : ")
# party = [name1,name2,name3]
# another = input("Do you want to invite another(y/n): ")
# while another == "y":
#     newname = party.append(input("Enter that name : "))
#     another = input("Do you want to invite another(y/n) :")
# print("You have", len(party),"people coming to your party .")
# print(party)
# selection = input("Enter one fo the names :")
# print(selection, "is in position",party.index(selection), "on the list.")
# stillcome = input("Do you still want them to come(y/n):")
# if stillcome == "n":
#     party.remove(selection)
# print(party)


# 78 Create a list containig the titles of four TV programmes and display them on seperate lines. Ask the user to enter another show and a position they want it inserted into the list. Display the list again, showing all five TV programmes in their new positions.

titles = ["Naruto","One-Piece","AOT","One Punch Man"]
for i in titles:
    print(i)
print()
show = input("Enter another show :")
position = input("Enter the position you want it to be entered :")
titles.insert(position,show)
for i in titles:
    print (i)



# 79 Create an empty list called "nums". Ask the user to enter numbers. After each number is entered, add it to the end of the nums list and display the list. Once they have entered three numbers, ask them if they still want the last number they entered saved. If they say"no", remove the last item from the list. Display the list of numbers.

nums = []
count = 0
while count < 3:
    num = int(input("Enter a number :"))
    num.append(num)
    print(nums)
    count = count+1
lastnum = input("Do you want the last number sayed(y/n): ")
if lastnum == "n":
    nums.remove(num)
print(nums)
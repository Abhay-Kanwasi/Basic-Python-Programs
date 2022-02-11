#139 Create an SQL database called PhoneBook that contains a table called Names with the following data:

# ID : 1,2,3,4,5
# First Name : Simon,Karen,Darren,Anne,Mark
# Surname : Howels,Philips,Smith,Jones,Smith
# Phone Number : 01223349752,01954295773,01589749012,01323567322,01223855534

# import mysql

# with mysql.connect("PhoneBook.db") as db:
#     cursor = db.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
#         id integer PRIMARY KEY,
#         firstname text,
#         surname text,
#         phonenumber text);""")
# cursor.execute(""" INSERT INTO Names(id, firstname,surname,phonenumber)
#     VALUES("1", "Simion","Howels", "01223 349752")""")
# db.commit()
# cursor.execute(""" INSERT INTO Names(id, firstname,surname,phonenumber)
#     VALUES("2", "Karen","Philips", "01954295773")""")
# db.commit()
# cursor.execute(""" INSERT INTO Names(id, firstname,surname,phonenumber)
#     VALUES("3", "Darren","Smith", "01583749012")""")
# db.commit()
# cursor.execute(""" INSERT INTO Names(id, firstname,surname,phonenumber)
#     VALUES("4", "Anne","Jones", "01323567322")""")
# db.commit()
# cursor.execute(""" INSERT INTO Names(id, firstname,surname,phonenumber)
#     VALUES("5", "Mark","Smith", "01223855534")""")
# db.commit()

# db.close()


# 140 Using the PhoneBook database from program 139, write a program that will display the following menu.

"""Main Mwnu
1) View phone book
2) Add to phone book
3) Search for surname
4) Delete person from the phone book
5) Quit

Enter your selection :"""

# If the user selects 1, they should be able to view the entire phonebook. If they select 2, it should allow them to add a new person to the phonebook. If they select3, it should ask them for a surname and then display onlt the records of people with the same surname. If they select 4, it should ask for an ID and then delete that record from the table. If they select5, it should end the program. Finally, it should end the program. Finally, it should display a suitable message if they enter an incorrect selection from the menu. They should return to the menu after each action, until they select 5.

# import mysql

# def viewphonebook():
#     cursor.execute("SELECT * FROM Names")
#     for x in cursor.fetchall():
#         print(x)

# def addtophonebook():
#     newid = int(input("Enter ID: "))
#     newfname = input("Enter first name :")
#     newsname = input("Enter surname :")
#     newpnum = input("Enter phone number :")
#     cursor.execute("""INSERT INTO Names (id, firstname, surname,phonenumber) VALUES (?,?,?,?)""",(newid,newfname,newsname,newpnum))
#     db.commit()

# def selectname():
#     selectsurname = input("Enter a surname :")
#     cursor.execute("SELECT * FROM Names WHERE surname = ?", [selectsurname])
#     for x in cursor.fetchall():
#         print(x)
    
# def deletedata():
#         selectid = int(input("Enter ID :"))
#         cursor.execute("DELETE FROM Names WHERE id = ?", [selectid])
#         cursor.execute("SELECT * FROM Names")
#         for x in cursor.fetchall():
#             print(x)
#         db.commit()

# with mysql.connect("PhoneBook.db") as db:
#     cursor = db.cursor()

# def main():
#     again = "y"
#     while again == "y":
#         print()
#         print("Main Menu")
#         print()
#         print("1) View phone book")
#         print("2) Add to phonebook")
#         print("3) Search for surname")
#         print("4) Delete person from phone book")
#         print("5) Quit")
#         selection = int(input("Enter your selection :"))
#         print()

#         if selection == 1:
#             viewphonebook()
#         elif selection == 2:
#             addtophonebook()
#         elif selection == 4:
#             deletedata()
#         elif selection == 5:
#             again = "n"
#         else:
#             print("Incorrect selection entered")

# main()
# db.close()


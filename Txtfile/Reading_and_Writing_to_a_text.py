# 105 Write a new file called "Number.txt". Add five numbers to the document which are stored on the same line and only seperated by a comma. Once you have run the program, look in the location where your program is stored and you should see that file has been created. The easiest way to view the contents of the new text file on a windows system is to read it using Notepad.

# file = open("Numbers.txt","w")
# file.write("4, ")
# file.write("9, ")
# file.write("1, ")
# file.write("7, ")
# file.write("5, ")
# file.close()


# 106 Create a new file called "Names.txt". Add five names to the document, which are stored on seperate lines. Once you have run the program, look in the location where your program is stored and check that the file has been created properly.

file = open("Numes.txt","w")
file.write("Python\n")
file.write("R\n")
file.write("Ruby\n")
file.write("Secrate doc.\n")
file.write("Software\n")
file.close()
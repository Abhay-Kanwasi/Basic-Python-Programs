# Python-Basic-Program-Challenge-Series
In this series i cover each topics with various easy examples for every concept i create seprate file 

## Note

### Please use wrap text in all the .py files when you open it in VS Code if you want to avoid the unnecessary question following. 

### For 2D graphics or turle graphics use Spyder IDE

# 1. Basics
Python is case sensitive so it is important that you use the correct case, otherwise
your code will not work.
Text values need to appear in speech marks (") but numbers do
not.

When naming variables (i.e. values that you want to store
data in) you cannot use any dedicated words such as print,
input, etc. otherwise your code will not work.
When saving your files do not save them with any
dedicated words that Python already uses, such as print,
input, etc. If you do this it will not run and you will need to
rename the file before it works.
To edit a program you have saved and closed, right-click on the
file and select Edit with IDLE. If you just double-click on
the file it will only try to run it and you will not be able to edit it.

`basic things`

`addition`
answer = num1 + num2
Adds together num1 and num2 and stores the
answer in a variable called answer.

`subtraction`
answer = num1 - num2
Subtracts num2 from num1 and stores the
answer in a variable called answer.

`multiplication`
answer = num1 * num2
Multiplies num1 by num2 and stores the
answer in a variable called answer.

`division`
answer = num1 / num2
Divides num1 by num2 and stores the answer
in a variable called answer.

`whole number division`
answer = num1 // num2
A whole number division (i.e. 9//4 = 2) and
stores the answer in a variable called answer.

`diaplay the message`
print (“This is a message”)
Displays the message in the brackets. As the value we want displayed is a text value it
has the speech marks, which will not be displayed in the output. If you wanted to display
a numerical value or the contents of a variable, the speech marks are not needed.

`next line`
print (“First line\nSecond line”)
“\n” is used as a line break.

`take input`
textValue = input(“Enter a text value: ”)
Displays the question “Enter a text value: ” and stores the value the user enters in a
variable called textValue. The space after the colon allows a space to be added before
the user enters their answer, otherwise they appear squashed unattractively together.

`answer`
print (“The answer is”, answer)
Displays the text “The answer is” and the value of the variable answer.

`taking integer``
numValue = int(input(“Enter a number: ”))
Displays the question “Enter a number: ” and stores the value as an
integer (a whole number) in a variable called numValue Integers can be
used in calculations but variables stored as text cannot.



# 2. If and Else

I created ' if_else.py ' 
In this we see "If statement allow your program to make decision and change the route that is taken through
the program
In this i also cover basic concept of #Comparison_Operators
 >Operator   Description
 > ==         Equal to
 >!=         Not equal to
 > " >, <,"      Greater than, Less then
 > >=,<=      Greater than equals to, Less then equals to
  
 **Logical_Operators**
 Operator            Description
   and          Both conditions must be met
   or          Either conditions must be met

# 3. Strings

I created 'Strings.py'
String is the technical name for text. To define a block of code as a string, you need to
include it in either double quotes (") or single quotes ('). It doesn’t matter which you use so
long as you are consistent.
There are some characters you need to be particularly careful with when inputting them
into strings. These include:
" ' \
That is because these symbols have special meanings in Python and it can get confusing if
you use them in a string.

Multiple-Line Strings
If you want to input a string across multiple lines you can either use the line break (\n) or
you can enclose the entire thing in triple quotes. This will preserve the formatting of the
text.
  address = """123
  Oldtown
  ABI 43BF"""
  print(address)
 
 
### I also introduce some functions

`len(word)`
Fnds the length of the variable called word.

`word.upper()` 
Changes the string into upper case

`print(word.capitalize())`
Displays the variable so only the first word
has a capital letter at the beginning and
everything else is in lower case.

`word.title()'
Changes a phrase so that every word
has a capital letter at the beginning
with the rest of the letters in the
word in lower case (i.e.Title Case).

`text = “ This is some text. ”
print(text.strip(“ ”))`
Removes extra characters (in this case spaces) from the start and end of a string.

`print (“Hello world”[7:10])`
Each letter is assigned an index number to
identify its position in the phrase, including
the space. Python starts counting from 0, not
1.
Therefore, in this example, it would display
the value of positions 7, 8 and 9 ,which is
“orl”.
name = firstname+surname


# 4. Math
###I created math.py
Python can perform several mathematical functions, but these are only available when the
data is treated as either an integer (a whole number) or a floating-point (a
number with a decimal place). If data is stored as a string, even if it only contains numeric
characters, Python is unable to perform calculations with it (see page 24 for a fuller
explanation).

`import math.py`
In order to use some of the mathematical functions (math.sqrt(num)
and math.pi) you will need to import the maths
library at the start of your program. You do this by
typing import math as the first line of your
program.

`float`
num=float(input(“Enter number: “))
Allows numbers with a decimal point dividing the integer and fraction part.

`decimal places`
print(round(num,2))
Displays a number rounded to
two decimal places.

`square root`
**
To the power of
(e.g. 102 is 10**2).
math.sqrt(num)
The square root of a number, but you must have the line import
math at the top of your program for this to work.

'pie`
math.pi
Gives you pi (π) to 15 decimal places,
but you must have the line import
math at the top of your program for
this to work.

`whole number division`
x // y
Whole number division (e.g.15//2 gives
the answer 7).

`x%y`
x % y
Finds the remainder (e.g. 15%2 gives
the answer 1).

# 5. For loop
I created loops.py
A for loop allows Python to keep repeating code a set number of times. It is sometimes
known as a counting loop because you know the number of times the loop will run
before it starts.

The range function is often used in for loops and lists the starting number, the ending
number and can also include the steps (e.g. counting in 1s, 5s or any other value you wish).

`about loop`

for i in range(1,10):
print(i)
This loop uses a variable called “i” to keep track of the number of times
the loop has been repeated. It will start i at 1 (as that is the starting
value in the range function) and repeat the loop, adding 1 to i each time
and displaying the value of i until it reaches 10 (as dictated by the range
function), where it will stop. Therefore, it will not repeat the loop a tenth
time and will only have the following output:
1, 2, 3, 4, 5, 6, 7, 8, 9

`case1`

for i in range(1,10,2):
print(i)
This range function includes a third value
which shows how much is added to i in
each loop (in this case 2). The output will
therefore be: 1, 3, 5, 7, 9

`case2`

for i in range(10,1,-3):
print(i)
This range will subtract 3 from i each
time. The output will be: 10, 7, 4
for i

# 6 While loop

A while loop allows code to be repeated an unknown number of times
as long as a condition is being met. This may be 100 times, just the once or
even never. In a while loop the condition is checked before the code is run,
which means it could skip the loop altogether if the condition is not being
met to start with. It is important, therefore, to make sure the correct
conditions are in place to run the loop before it starts.

I created while_loop.py to cover it

# 7. Random

Python can generate random values. In reality, the values are not
completely random as no computer can cope with that; instead it uses an
incredibly complex algorithm that makes it virtually impossible to accurately
predict its outcome so, in effect, it acts like a random function.
There are two types of random value that we will be looking at:

Random numbers within a specified range;
A random choice from a range of items that are input.

To use these two options, you will need to import the random library. You do
this by typing import random at the start of your program

For this I created random.py 

### Some useful example of random which we use in random.py

`import random`
This must appear at the start of your program otherwise the random function will not
work.

`num = random.random()`
Selects a random floating-point number between 0 and 1 and
stores it in a variable called “num”. If you want to obtain a
larger number, you can multiply it as shown below:
import random
num = random.random()
num = num * 100
print(num)

`num = random.randint(0,9)`
Selects a random whole number
between 0 and 9 (inclusive).

`num1 = random.randint(0,1000)
num2 = random.randint(0,1000)
newrand = num1/num2
print(newrand)`
Creates a random floating-point number by
creating two random integers within two
large ranges (in this case between 0 and 1000) and dividing one by the other.

`num = random.randrange(0,100,5)`
Picks a random number between the
numbers 0 and 100 (inclusive) in steps of five,
i.e. it will only pick from 0, 5, 10, 15, 20, etc.

`colour = random.choice([“red”,“black”,“green”])`
Picks a random value from the options “red”, “black” or “green” and stores it as the
variable “colour”. Remember: strings need to include speech marks but numeric data
does not.

# 8. Turtle Graphics
For this I created turtle.py

It is possible to draw using a turtle in Python. By typing in commands
and using loops, you can create intricate patterns. Here is how it works.
A turtle will travel along a path that you define, leaving a pen mark behind it. As you control
the turtle, the pattern that is left is revealed. To draw the pentagon shown below you would
type in the following code.

import turtle

turtle.shape("turtle")
for i in range(0,5):
 turtle.forward(100)
 turtle.right(72)
turtle.exitonclick()

By combining these simple shapes and using nested loops (i.e. loops inside other loops)
it is possible to create beautiful patterns very easily.

`import turtle`
This line needs to be included
at the beginning of your
program to import the turtle
library into Python, allowing
you to use the turtle functions.

`scr = turtle.Screen()`
Defines the window as being
called “scr”. This means we can
use the shorthand “scr”, rather
than having to refer to the window
by its full name each time.

`scr.bgcolor(“yellow”)`
Sets the screen background
colour to yellow. By default, the
background colour will be
white unless it is changed.

`turtle.pensize(3)`
Changes the turtle pen size
(the thickness of the line that is
drawn) to 3. By default, this is 1
unless it is changed.

`turtle.penup()`
Removes the pen from
the page so that as the
turtle moves it does not
leave a trail behind it.

`turtle.pendown()`
Places the pen on the
page so that when the
turtle moves it will
leave a trail behind it.
By default, the pen is
down unless specified
otherwise.

`turtle.forward(50)`
Moves the turtle forward 50
steps.

`turtle.left(120)`
Turns the turtle 120° to
the left (counter
clockwise). turtle.right(90)
Turns the turtle 90° to
the right (clockwise).

`turtle.showturtle()`
Shows the turtle on the screen.
By default, the turtle is
showing unless specified
otherwise.

`turtle.hideturtle()`
Hides the turtle so it is not
showing on the screen.

`turtle.shape(“turtle”)`
Changes the shape of the turtle to look like a turtle
. By default, the turtle will look like a small arrow.

`turtle.exitonclick()`
When the user clicks on the
turtle window it will
automatically close.

`turtle.begin_fill()`
Entered before the code that draws a shape so it
knows to fill in the shape it is drawing.

`turtle.end_fill()`
Entered after the code that is drawing the shape to
tell Python to stop filling in the shape.

`turtle.color(“black”,“red”)`
Defines the colours filling in the shape. This
example will make the shape have a black outline
and a red fill. This needs to be entered before the
shape is drawn.

# 9. Dictionaries

So far, we have used variables that can store a single item of data in them. When you used
the random.choice([“red”,“blue”,“green”]) line of code you are picking a
random item from a list of possible options. This demonstrates that one item can hold
several pieces of separate data, in this case a collection of colours.
There are several ways that collections of data can be stored as a
single item. Three of the simpler ones are:
1. tuples
2. lists
3. dictionaries

`Tuples`

Once a tuple is defined you cannot change what is stored in it. This means that when you
write the program you must state what the data is that is being stored in the tuple and the
data cannot be altered while the program is running. Tuples are usually used for menu
items that would not need to be changed.

`Lists`

The contents of a list can be changed while the program is running and lists are one of
the most common ways to store a collection of data under one variable name in Python. The
data in a list does not all have to be of the same data type. For example, the same list can
store both strings and integers; however, this can cause problems later and is therefore not
recommended.

`Dictionaries`

The contents of a dictionary can also be changed while the program is running. Each
value is given an index or key you can define to help identify each piece of data. This index
will not change if other rows of data are added or deleted, unlike lists where the position of
the items can change and therefore their index number will also change.

Some things we used in dictionaries.py

`fruit_tuple = (“apple”,“banana”,“strawberry”,“orange”)`

Creates a variable name called “fruit_tuple” which stores four pieces of fruit within it. The
round brackets define this group as a tuple and therefore the contents of this collection of
data cannot be altered while the program is running.

`print(fruit_tuple.index(“strawberry”))`

Displays the index (i.e. the numeric key) of the item “strawberry”. In this example it
will return the number 2 as Python starts counting the items from 0, not 1.

`print(fruit_tuple[2])`

Displays item 2 from
“fruit_tuple”, in this case
“strawberry”.

`names_list = [“John”,“Tim”,“Sam”]`

Creates a list of the names and stores them in the
variable “names_list”. The square brackets define
this group of data as a list and therefore the contents
can be altered while the program is running.

`names_list.append(input(“Add a name: “))`

Asks the user to enter a name and will add that to the end of
“names_list”.
del names_list[1]
Deletes item 1 from
“names_list”. Remember
it starts counting from 0
and not 1. In this case it
will delete “Tim” from the
list.

`print(sorted(names_list))`

Displays names_list in alphabetical
order but does not change the order of
the original list, which is still saved in
the original order. This does not work
if the list is storing data of different
types, such as strings and numeric
data in the same list.

`names_list.sort()`

Sorts name_list into
alphabetical order and
saves the list in the new
order. This does not work
if the list is storing data of
different types, such as
strings and numeric data
in the same list.

`colours = {1:“red”,2:“blue”,3:“green”}`

Creates a dictionary called “colours”, where each item is
assigned an index of your choosing. The first item in each
block is the index, separated by a colon and then the
colour.

`colours[2] = “yellow”`

Makes a change to the data stored in position 2 of the colours dictionary. In this case it will
change “blue” to “yellow”.

`x = [154,634,892,345,341,43]`

Here we have created a list that contains
numbers. Please note: as it contains numeric
data, no speech marks are required.

`print(x[1:4])`

This will display data in positions 1, 2 and 3. In
this case 634, 892 and 345. Remember, Python
starts counting from 0 and will stop when it gets
to the last position, without showing the final
value.

`print(len(x))`

Displays the length of the list
(i.e. how many items are in the
list).
num = int(input(“Enter number: ”))
if num in x:
print(num,“is in the list”)
else:
print(“Not in the list”)
Asks the user to enter a number and checks
whether the number is in the list and displays an
appropriate message.

`for i in x:
print(i)`

Uses the items in the list in a for
loop, useful if you want to print
the items in a list on separate
lines.

`x.insert(2,420)`

Inserts the number
420 into position 2 and
pushes everything
else along to make
space. This will
change the index
numbers of the items
in the list.

`x.remove(892)`

Deletes an item from
the list. This is useful
if you do not know the
index of that item. If
there is more than one
instance of the data it
will only delete the
first instance.

`x.append(993)`

Adds the number 993 to the end of the list.


# 10. String Manipulation

**Explanation

A string is the technical name for a group of characters that you do not need to perform
calculations with. “Hello” would be an example of a string, as would “7B”.
Here we have a variable called name which is assigned the value “Simon”.

### Example which we used in string2.py

Please note: in the examples below, “msg” is a variable name containing a string.

`First one`
if msg.isupper():
print(“Uppercase”)
else:
print(“This is not in uppercase”)
If the message is in uppercase it will display the message
“Uppercase”, otherwise it will display the message “This
is not in uppercase”.

`Second one`
msg.islower()
Can be used in place of
the isupper () function
to check if the variable
contains lower case
letters.

`Third one`
msg=”Hello”
for letter in msg:
print(letter,end=”*”)
Displays the message, and between each character it will display a “*”.
The output in this example will be: H*e*l*l*o*


# 11. Numeric Arrays

Lists can store a jumble of different types
of data at the same time, including strings and numbers. Python arrays are similar to
lists, but they are only used to store numbers. Numbers can have varying ranges, but
in an array all pieces of data in that array must have the same data type.

`Integer`
Whole number between -32,768 and 32,767 
size = 2bytes

`Long`
Whole number between -2,147,483,648 and 2,147,483,647 
size = 4bytes

`Floating-point`
Allows decimal places with numbers ranging
from -1038 to 1038 (i.e. allows up to 38 numeric
characters including a single decimal point
anywhere in that number and can be negative or
positive value)
size = 4bytes

`Double`
Allows decimal places with numbers ranging
from -10308 to 10308.
size = 8bytes

When you create your array you need to define the type of data it will contain. You cannot
alter or change this while the program is running. Therefore, if you define an array as an 'i'
type (this allows whole numbers between the values −32,768 and 32,767) you cannot add a
decimal point to a number in that array later as it will cause an error message and crash the
program.

### Please note:
Other programming languages use the term array to
allow the storage of any data type, but in Python arrays only store numbers whereas lists
allow the storage of any data type. If you want to create a variable that stores multiple
strings, in Python you need to create a list rather than an array.

`importing array`

from array import *
This needs to be the first line of your program so that
Python can use the array library.

`for sorting`

nums = sorted(nums)
Sorts the array into
ascending order.

`new value`

newValue = int(input(“Enter number: “))
nums.append(newValue)
Asks the user to enter a new number which it will add to
the end of the existing array.

`new array`

newArray = array(‘i’,[])
more = int(input(“How many items: ”))
for y in range(0,more):
newValue=int(input(“Enter num: ”))
newArray.append(newValue)
nums.extend(newArray)
Creates a blank array called “newArray” which uses the
integer data type. It asks the user how many items they
want to add and then appends these new items to
newArray. After all the items have been added it will join
together the contents of newArray and the nums array.

`display`

for x in nums:
print(x)
Displays the array with
each item appearing on
a separate line.

`number reverse`

nums.reverse()
Reverses the order of
the array.

`remove`

1. getRid = int(input(“Enter item index: ”))
nums.remove(getRid)
Asks the user to enter the item they want to get rid of and then removes the first item
that matches that value from the array.

2. nums.pop()
This will remove the last
item from the array.

`count`

print(nums.count(45))
This will display how many times the value “45” appears in the array.

# 12. 2D Lists and Dictionaries

Technically it is possible to create a two-dimensional array in Python, but as Python arrays
are limited to storing numbers and most Python programmers feel more comfortable with
working with lists, 2D arrays are rarely used and 2D lists are far more common.
Imagine, for one terrifying moment, you are a teacher. Scary I know! Also
imagine you have four students and you teach those same students across
three different subjects. You may, if you are a conscientious teacher, need to
keep records of those students’ grades for each of their subjects. It is possible to create a
simple chart on paper to do this as follows:
Maths English French
Susan 45 37 54
Peter 62 58 59
Mark 49 47 60
Andy 78 83 62

### Logic we used in 2D_List_and_Dictionaries.py

`simple_array = [[2,5,8],[3,7,4],[1,6,9]]`

Creates a 2D list (as shown on the right) which uses
standard Python indexing for the rows and columns.

`print(simple_array)`

Displays all the data in the 2D
list.

`print(simple_array[1])`

Displays data from row 1, in this case
[3, 7, 4].

`print(simple_array[1][2])`

Displays data from row 1, column 2, in
this case 4.

`simple_array[2][1]= 5`

Changes the data in row 2,
column 1 to the value 5.

`simple_array[1].append(3)`

Adds the value 3 onto the end of the data in
row 1 so in this case it becomes [3, 7, 4, 3].

`data_set = {“A”:{“x”:54,“y”:82,“z”:91},“B”:{“x”:75,“y”:29,“z”:80}}`

Creates a 2D dictionary using user-defined labels for the rows and columns (as shown
above).

`print(data_set[“A”])`

Displays data from data set “A”.

`print(data_set[“B”][“y”])`

Displays data from row “B”, column “y”.

`grades[name]={“Maths”:mscore,“English”:escore}`

Adds another row of data to a 2D dictionary. In this case, name would be the row index
and Maths and English would be the column indexes.

`for name in grades:
print((name),grades[name][“English”])`

Displays only the name and the English grade for each
student.

`for i in data_set:
print(data_set [i][“y”])`

Displays the “y” column from each row.
del list[getRid]
Removes a selected
item.

`data_set[“B”][“y”] = 53`

Changes the data in “B”, “y”, to 53.


# 13. Reading and Writing to a Text File

### I create a seperate folder Textfile for storing this code and output text.

It is all very well being able to define a list, make changes and add new data, but if the next
time the program is run it returns to the original data and your changes are lost then it is
not a lot of use. Therefore, it is sometimes necessary to save data outside of the program
and this way the data can be stored, along with any changes that are made.
The easiest place to start learning about writing and reading from an external
file is with a text file.
When opening an external file you must specify how that file will be used within the
program. The options are below.

`Code - w`

Write mode: used to create a new file. Any existing files
with the same name will be erased and a new one
created in its place.

`Code - r`

Read mode: used when an existing file is only being
read and not being written to.

`Code - a`

Append mode: used to add new data to the end of the
file.

Text files are only used to write, read and append data. By the very nature of how they work
it is not easy to remove or alter individual elements of data once it is written to the file,
unless you want to overwrite the entire file or create a new file to store the new
data. If you want to be able to alter the individual elements once the file has
been created it is better to use a .csv file (see after some time) or an SQL database (see
after some time).

## Code we use here

`file = open(“Countries.txt”,“w”)
file.write(“Italy\n”)
file.write(“Germany\n”)
file.write(“Spain\n”)
file.close()`

Creates a file called “Countries.txt”. If one already exists then it will be overwritten with
a new blank file. It will add three lines of data to the file (the \n forces a new line after
each entry). It will then close the file, allowing the changes to the text file to be saved.

`file = open(“Countries.txt”,“r”)
print(file.read())`

This will open the Countries.txt file in “read”
mode and display the entire file.

`file = open(“Countries.txt”,“a”)
file.write(“France\n”)
file.close()`

This will open the Countries.txt file in “append”
mode, add another line and then close the file.
If the file.close() line is not included, the
changes will not be saved to the text file.


# 14. Reading and Writing to a .csv File

CSV stands for Comma Separated Values and is a format usually associated with importing
and exporting from spreadsheets and databases. It allows greater control over the data
than a simple text file, as each row is split up into identifiable columns. Below is an
example of data you may want to store.

Name   Age  Starsign
Brian  73   Taurus
Sandra 48   Virgo
Zoe    25   Scorpio

### When opening a .csv file to use, you must specify how that file will be used. The options are:

`w`

Creates a new file and writes to that file. If the file
already exists, a new file will be created, overwriting
the existing file.

`x`

Creates a new file and writes to that file. If the file
already exists, the program will crash rather than
overwrite it.

`r`

Opens for reading only and will not allow you to make
changes.

`a`

Opens for writing, appending to the end of the file.

### Code we use in Txtfile folder in  R_W_to_csv_file.py

`import csv`

This must be at
the top of your
program to allow
Python to use the
.csv library of
commands.



`file = open (“Stars.csv”,“w”)
newRecord = “Brian,73,Taurus\n”
file.write(str(newRecord))
file.close()`

This will create a new file called “Stars.csv”, overwriting any
previous files of the same name. It will add a new record and
then close and save the changes to the file.



`file = open (“Stars.csv”,“a”)
name = input(“Enter name: ”)
age = input(“Enter age: ”)
star = input(“Enter star sign: ”)
newRecord = name + “,” + age + “,” + star + “\n”
file.write(str(newRecord))
file.close()`

This will open the Stars.csv file, ask the user to enter the name, age
and star sign, and will append this to the end of the file.



`file = open(“Stars.csv”,“r”)
for row in file:
print(row)`

This will open the Stars.csv file in read
mode and display the records one row at
a time.



`file = open(“Stars.csv”,“r”)
reader = csv.reader(file)
rows = list(reader)
print(rows[1])`

This will open the Stars.csv file and
display only row 1. Remember, Python
starts counting from 0.



`file = open (“Stars.csv”,“r”)
search = input(“Enter the data you are searching for: ”)
reader = csv.reader(file)
for row in file:
if search in str(row):
print(row)`

Asks the user to enter the data they are searching for. It will display all rows that contain
that data anywhere in that row.



`import csv
file = list(csv.reader(open(“Stars.csv”)))
tmp = []
for row in file:
tmp.append(row)`

A .csv file cannot be altered, only added to. If you need to alter the file you need to
write it to a temporary list. This block of code will read the original .csv file and write it
to a list called “tmp”. This can then be used and altered as a list.



`file = open(“NewStars.csv”,“w”)
x = 0
for row in tmp:
newRec = tmp[x][0] + ”,” + tmp[x][1] + ”,” + tmp[x][2] + ”\n”
file.write(newRec)
x = x + 1
file.close()`

Writes from a list into a new .csv file called “NewStars.csv”.


# 15. Subprograms

Subprograms are blocks of code which perform specific
tasks and can be called upon at any time in the program to
run that code.

**Advantages

1. You can write a block of code and it can be used and reused
at different times during the program.

2. It makes the program simpler to understand as the code
is grouped together into chunks.


**Defining a subprogram and passing variables between subprograms

Below is a simple program that we would normally create
without subprograms but have written it with subprograms
so you can see how they work:

`def get_name():
 user_name = input("Enter your name :")
 return user_name
 
def print_Msg(user_name) :
 print("Hello", user_name)
 
def main()
 user_name = get_name()
 print_Msg(user_name)

main()`

**Explanation of this whole program : 

This program uses three subprograms get_name(), print_Msg() and main().
The get_name() subprogram will ask the user to input their name and then it will return
the value of the variable “user_name” so that it can be used in another subprogram. This is
very important. If you do not return the values, then the values of any variables that were
created or altered in that subprogram cannot be used elsewhere in your program.

The variable “user_name” appears in the brackets as the current value of the variable is
being imported into the subprogram so it can be used.
The main() subprogram will get the user_name from the get_name() subprogram
(using the variable user_name) as this was returned from the get_name() subprogram. It
will then use that user_name variable in the print_Msg() subprogram.
The last line “main()” is the actual program itself. All this will do is start the main()
subprogram running.
Obviously, there is no need to create such a convoluted way of performing what is in fact a
very simple program, but this is only used as an example of how subprograms are laid out
and variables can be used and passed between the subprograms.

**Please note:**

Python does not like surprises, so if you are going
to use a subprogram in a program, Python must have read the
“def subprogram_name()” line before so it knows where to
go to find it. If you try to refer to a subprogram before Python has
read about it, it panics and will crash. When calling a
subprogram, the subprogram must be written above the section
of code you use to call it. Python will read from the top down and run the first line it comes
across that has not been indented and does not start with the word def. In the program
above this would be main().

## Code we used on subprogram.py with explanation.

`Code 1`

def get_data():
user_name = input(“Enter your name: ”)
user_age = int(input(“Enter your age: ”))
data_tuple = (user_name, user_age)
return data_tuple

**Explanation**

Defines a subprogram called “get_data()” which will ask the user for their name and
age. As we want to send more than one piece of data back to the main program for other
parts of the program to use, we have combined them together. The return line can only
return a single value, which is why we combined the user_name and user_age variables
into a tuple (see page 58) called data_tuple.

`Code 2`

def message(user_name,user_age):
if user_age <= 10:
print(“Hi”, user_name)
else:
print(“Hello”, user_name)

**Explanation**

Defines a subprogram called message() which uses two variables that have previously
been defined (user_name and user_age).

`Code 3`

def main():
user_name,user_age = get_data()
message(user_name,user_age)

**Explanation**

Defines a subprogram called main() which obtains the
two variables from the get_data() subprogram. These
must be labelled in the same order as they were
defined in the tuple. It then calls the message()
subprogram to run with the two variables.

`Code 4`

main()

**Explanation**

Runs the main() subprogram.



# 16 Tkinter GUI


A GUI (graphical user interface) makes the program easier to use. It allows you, as the
programmer, to create screens, text boxes and buttons to help the user navigate through
the program in a more user-friendly way. Tkinter is a library of features in Python that
allows you to do this.

### Code we used in tkinterGUI.py

`Code 1`

from tkinter import *
This line must go at the beginning of the program to import the Tkinter library.

`Code 2`

window = Tk()
window.title(“Window Title”)
window.geometry(“450x100”)
Creates a window that will act as the
display, referred to as “window”, adds a title
and defines the size of the window.

`Code 3`

label = Label(text = “Enter number:”)
Adds text to the screen displaying the message
shown.

`Code 4`

entry_box = Entry (text = 0)
Creates a blank entry box. Entry boxes can be used by
the user to input data or used to display output.

`Code 5`

output_box = Message(text = 0)
Creates a message box which is used to display an
output.

`Code 6`

list_box = Listbox()
Creates a drop-down list box
which can only contain strings.

`Code 7`

button1 = Button(text = “Click here”, command = click)
Creates a button that will run the subprogram “click”.

`Code 8`

output_box [“bg”] = “red”
Specifies the background colour of the
object.

`Code 9`

output_box [“fg”] = “white”
Specifies the font colour of the object.

`Code 10`

output_box [“relief”] = “sunken”
Specifies the style of the box. This can be flat,
raised, sunken, grooved and ridged.

`Code 11`

entry_box [“justify”] = “center”
Specifies the justification of the text in an entry box,
but this does not work for message boxes.

`Code 12`

label.place(x = 50, y = 20, width = 100, height = 25)
Specifies the position in which the object will appear in the window. If the position is
not specified the item will not appear in the window.

`Code 13`

entry_box.delete(0, END)
Deletes the contents of an entry or
list box.

`Code 14`

num = entry_box.get()
Saves the contents of an entry box and stores it
in a variable called num. This does not work
with message boxes.

`Code 15`

answer = output_txt[“text”]
Obtains the contents of a message box and
stores it in a variable called answer. This does
not work with an entry box.

`Code 16`

output_txt[“text”] = total
Changes the content of a message box to
display the value of the variable total.

`Code 17`

window.mainloop()
This must be at the end of the program to make
sure it keeps working.











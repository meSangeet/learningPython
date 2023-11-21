'''
File handling in python

most important function -> open()

open() function takes two arguments ->
file name
mode -> 

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists



In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")



The open() function returns a file object, which has a read() method for reading content of the file.

eg-

f = open("file.txt", "rt")
print(f.read())

print(f.read(5)) -> returns first 5 characters of the file



//you can return one line by using the readline() function

print(f.readline())

by calling the readline() two times, you can read the first two lines



//looping through file line by line

f = open("text.txt")
for x in f:
    print(x)


//close the file when you are finished with it using f.close()



//appending

To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")


//writing

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())



# Python delete file

To delete a file you must import the OS module, and run its os.remove() function


import os
os.remove("filename.txt")

to check if file exists

os.path.exists("filename.txt")

to delete folder

os.rmdir("foldername")
'''



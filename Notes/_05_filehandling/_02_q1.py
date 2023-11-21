'''
1. Write a program that reads a text file “file1.txt". For each line, move the words of odd 
length to a new file “file2.txt”.

e.g.;
Input: 

file1.txt
-----------------
hi
this is new file
----------------
Output:

file1.txt
---------------
hi
this is file
---------------
file2.txt
------------------
new
-----------------
'''
import os


def func():
    f1 = open('_05_filehandling/file1.txt', 'r+')

    f2 = open('_05_filehandling/file2.txt', 'at')
    f3 = open('_05_filehandling/file3.txt', 'at')

    for line in f1:
        words = line.split()
        flag = False
        for word in words:
            eve = []
            modline = ''
            if len(word)%2 != 0:
                f2.write(word)
                f2.write(' ')
                flag = True
            else:
                f3.write(word)
                f3.write(' ')
        
        f3.write('\n')
        if flag:
            f2.write('\n')

    f1.close()
    f2.close()
    f3.close()

    f1 = open('_05_filehandling/file1.txt', 'w')
    f2 = open('_05_filehandling/file3.txt', 'r')
    f1.write(f2.read())
    f1.close()
    f2.close()
    os.remove('_05_filehandling/file3.txt')


if __name__ == "__main__":
    func()

'''
Write a program that reads a text file “file1.txt". For each line, move the words of even 
length to a new file “file2.txt”.
e.g.;
Input: 
file1.txt
hi
this is new file
Output:
file1.txt
new
file2.txt
hi
this is
'''
import os

def func():
    f1 = open('_05_filehandling/file1.txt', 'r+')
    f2 = open('_05_filehandling/file2.txt', 'a')
    f3 = open('_05_filehandling/file3.txt', 'a')

    for line in f1:
        words = line.split()
        flag1 = False
        flag2 = False
        for word in words:
            if len(word)%2 == 0:
                f2.write(word)
                f2.write(' ')
                flag1 = True
            else:
                f3.write(word)
                f3.write(" ")
                flag2 = True

        if flag1:
            f2.write('\n')
        if flag2:
            f3.write('\n')

    f1.close()
    f2.close()
    f3.close()

    f1 = open('_05_filehandling/file1.txt', 'w')
    f3 = open('_05_filehandling/file3.txt', 'r')

    f1.write(f3.read())

    f1.close()
    f3.close()

    os.remove('_05_filehandling/file3.txt')

if __name__ == "__main__":
    func()



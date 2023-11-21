#read a file student.txt count the number of occurenves of each word store it in a dictionary sort the dictionary in decreasing order of frequency of words and print the dictionary

f = open('_05_filehandling/student.txt', 'r')

freq = {}

for line in f:
    words = line.split();
    for word in words:
        word = word.strip(',?.').lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

def func(item):
    return item[1]
sooo = dict(sorted(freq.items(),key = func))

for item,free in sooo.items():
    print(f"{item} -> {free}")

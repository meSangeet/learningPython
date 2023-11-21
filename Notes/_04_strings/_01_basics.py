str = 'abcde'
ptr = ''
for i in str:
    ptr += chr(ord(i) + 2)

print(ptr)
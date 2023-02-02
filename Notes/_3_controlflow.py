# #if elif else condition

# a = int(input())
# b = int(input())

# if b>a:
#     print("b is greater than a")
#     #this indentation defines the block of the if condition, hence it is pretty important
# elif a>b:
#     print("a is greater than b")
# else:
#     print("a == b")



# # while loop


# n = int(input('enter the maximum number of iterations - '))

# i = 1

# while i <= n:
#     print(i)
#     i += 1

# print('done')

# #pass -> do nothing  or continue in c++
# #break -> exit the loop immediately



# for loop


listt = []

for i in range(10):
    print(i+1)
    listt.append(i**2)

size = listt.size()

for i in listt:
    print(i)

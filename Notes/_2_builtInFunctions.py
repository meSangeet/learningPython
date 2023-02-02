# some useful functions

#round() -> rounds the input value to a specified number of places or to the nearest integer.

print(round(4.556723, 3))

print(round(4.556723))

#divmod(x,y) -> outputs the quotient and the remainder in a tuple (we will see what a tuple is)

print(divmod(25,6)) #tuple is just an ordered pairs

#isinstance(value, datatype) returns True, if the first argument is an instance of that class. Multiple classes can also be checked at once.

print(isinstance(4,int))
print(isinstance('a',(int,float))) #checks if the value belongs to any of the classes or not

print(isinstance(2 + 3j, (str, complex)))

#pow(x,y,z) -> x raise to the power y then remainder by z

#pow(x,y) -> x raise to the power y

#input() -> to take the input, input type will only be string

a = input("enter something - ")

print(type(a))

b = int(a) #this will only work if the string can actually be converted to int or any other datatype as specified.

print(type(b), b)


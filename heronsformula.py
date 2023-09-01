a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))

s=a+b+c/2
A=(s*(s-a)*(s-b)*(s-c))**1/2

print("area of the triangle is",A)

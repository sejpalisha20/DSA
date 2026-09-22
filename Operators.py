#perform addition, substraction, multiplication and division
a = 20
b = 10
print("Addition:", a+b)
print("Substraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

#Find remainder and quotient of two numbers
a = 10
b = 23
print("Remainder:", a%b)
print("Quotient:", a//b)

#Check whether a number is even or odd
a = int(input("Enter number:"))
if a%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#compare two numbers using relational operators
a = 10
b = 20
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#Demonstrate logical operators
a = 10
b = 20
print(a<b and b>15)
print(a>b or b>15)
print(not(a<b))

#Demonstrate assignment operators
a = 10
a += 5
print("After += :",a)
a -= 2
print("After -= :",a)
a *= 3
print("After *= :",a)
a /= 2
print("After /* :",a)

#Find the largest of the two numbers
a = 25
b = 40
if a > b:
    print("Largest:",a)
else:
        print("Largest:",b)





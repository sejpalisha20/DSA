#Print numbers from 1 to 10 using for loop
for i in range(1,11):
    print(i)

#Print numbers from 10 to 1 using while loop
i = 10
while i >= 1:
    print(i)
    i-=1

#print multiplication table of a number
a = 5
for i in range(1,11):
    print(a, "x", i, "=", a * i)

#Find sum of numbers from 1 to n
n = 10
sum = 0
for i in range(1, n+1):
    sum = sum + i
    print("Sum:", sum)

#Find the factorial of a number
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial = factorial + i
    print("Factorial:", factorial)

#Print all even numbers between 1 to 100
for i in range(2,101,2):
    print(i)

#Reverse a number using a loop
a = 12345
reverse = 0
while a > 0:
    digit = a % 10
    reverse = reverse + 10 + digit
    a = a//10
    print("Reverse:",reverse)

#Count the digits of a number
num = int(input("Enter a number: "))
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Number of digits:", count

#Check whether a number is prime
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

#Print Fibonacci series up to n terms
n = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b





    


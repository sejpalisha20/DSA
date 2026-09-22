#Check whether a number is positive, negative, or zero
a = -5
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

#Check whether a person is eligible to vote
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

#Find the largest of the three numbers
a = 10
b = 25
c = 15
if a >= b and a >= c:
    print("Largest:",a)
elif b >= a and b >= c:
    print("Largest:",b)
else:
    print("Largest:",c)

#Check whether a year is a leap year
year = 2024
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a Leap Year")

#Create a grade system based on marks
marks = 85
if marks >= 90:
    print("Grade A+:")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")

#Check whether the number is divisible by
a = 55
if a % 5 == 0 and a % 11 ==0:
    print("Number is divisible by 5 and 11 both")
else:
    print("Number is not divisible by 5 and 11 both")

#Simple calculator using if-elif-else
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid operator.")


    




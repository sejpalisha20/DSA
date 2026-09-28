#write a function to print "Hello, World"
def hello():
    print("Hello, World!")

hello()

#Write a function that takes a name and prints a greeting
def greet(name):
    print("Hello", name)

greet("Isha")

#write a function to add to numbers
def add(a, b):
    return a + b

print(add(10, 20))

#write a function to find the square of a number
def square(n):
    return n * n

print(square(5))

#write a function to check whether a number is even or odd
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(7)

#write a function to find the maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 20))

#write a function to convert Celcius to Fahrenheit.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(25))

#write a function to calculate the area of a circle
def area_circle(r):
    return 3.14 * r * r

print(area_circle(5))

#write a function to calculate the factorial of a number
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(5))

#write a function to check whether a number is positive, negative or zero
def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-5)

#write a function to find the maximum of three numbers
def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(maximum(10, 25, 15))

#write a function to count vowels in a string
def count_vowels(text):
    count = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

print(count_vowels("Hello World"))

#write a function to reverse a string
def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello"))

#write a function to find whether a string is a palindrome
def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome("madam")

#write a function to find the sum of all the elements in a list
def list_sum(numbers):
    total = 0

    for n in numbers:
        total = total + n

    return total

print(list_sum([10, 20, 30, 40]))

#write a function to find the largest elemet in the list
def largest(numbers):
    large = numbers[0]

    for n in numbers:
        if n > large:
            large = n

    return large

print(largest([10, 25, 15, 40, 20]))

#write a function to remove all the duplicate elements from the list
def remove_duplicates(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

#write a function to count how many times an element appears in a list
def count_element(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count = count + 1

    return count

print(count_element([1, 2, 2, 3, 2, 4], 2))

#write a function to check whether a number is prime
def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(prime(7))

#write a function to return all prime numbers between two numbers
def primes_between(start, end):
    result = []

    for n in range(start, end + 1):
        if n >= 2:
            prime = True

            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break

            if prime:
                result.append(n)

    return result

print(primes_between(1, 20))

#write a function to calculate fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

#write a function to find the second largest number in the list
def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]

print(second_largest([10, 20, 5, 30, 25]))

#write a function to sort a list without using sort()
def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

print(sort_list([5, 2, 8, 1, 3]))

#write a function to merge two lists and remove duplicates
def merge_lists(list1, list2):
    result = []

    for n in list1 + list2:
        if n not in result:
            result.append(n)

    return result

print(merge_lists([1, 2, 3], [3, 4, 5]))

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        return f"{self.name} {self.age} yosh {self.grade}-sinf"

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    arr = []
    for i in range(n):
        arr.append(a)
        a, b = b, a + b
    return arr

def palindrome(word):
    return word == word[::-1]

def tubson(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def kvadratlar(nums):
    return [x ** 2 for x in nums]

def juft(nums):
    return [x for x in nums if x % 2 == 0]

def yigindi(nums):
    return sum(nums)

def katta(nums):
    return max(nums)

def kichik(nums):
    return min(nums)

def reverse_text(text):
    return text[::-1]

def vowel_count(text):
    vowels = "aeiou"
    count = 0
    for i in text.lower():
        if i in vowels:
            count += 1
    return count

def sort_nums(nums):
    return sorted(nums)

def unique_nums(nums):
    return list(set(nums))

def average(nums):
    return sum(nums) / len(nums)

def kopaytirish_jadvali(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

student = Student("Ali", 17, 11)
calc = Calculator()

print(student.info())
print(calc.add(10, 5))
print(calc.sub(10, 5))
print(calc.mul(10, 5))
print(calc.div(10, 5))

print(factorial(5))
print(fibonacci(10))
print(palindrome("level"))
print(tubson(13))
print(kvadratlar([1, 2, 3, 4]))
print(juft([1, 2, 3, 4, 5, 6]))
print(yigindi([1, 2, 3, 4]))
print(katta([3, 7, 2, 9]))
print(kichik([3, 7, 2, 9]))
print(reverse_text("Python"))
print(vowel_count("Assalomu alaykum"))
print(sort_nums([5, 2, 8, 1]))
print(unique_nums([1, 1, 2, 3, 3, 4]))
print(average([10, 20, 30, 40]))
kopaytirish_jadvali(5)

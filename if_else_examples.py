# ================================
# Python If ... Else Statement
# Full Explanation of Conditions in Python
# ================================

# Example 1️⃣: Basic if statement
# The code inside the if block runs only when the condition is True.
x = 10
if x > 5:  # Check if x is greater than 5
    print("x is greater than 5")  # This line will print because 10 > 5

# ----------------------------------------------------

# Example 2️⃣: if ... else
# The else block runs only when the condition in if is False.
age = 15
if age >= 18:  # Check if the person is 18 or older
    print("You are an adult.")  # Executes if the condition is True
else:
    print("You are under 18.")  # Executes if the condition is False

# ----------------------------------------------------

# Example 3️⃣: if ... elif ... else
# Used when checking multiple conditions one after another.
score = 75

if score >= 90:
    print("Excellent")  # Runs if score is 90 or higher
elif score >= 80:
    print("Very Good")  # Runs if score is between 80 and 89
elif score >= 70:
    print("Good")  # Runs if score is between 70 and 79
elif score >= 60:
    print("Pass")  # Runs if score is between 60 and 69
else:
    print("Fail")  # Runs if score is below 60

# ----------------------------------------------------

# Example 4️⃣: Using logical operators (and / or)
# Combine multiple conditions using 'and', 'or', or 'not'.
temperature = 25

if temperature > 20 and temperature < 30:
    print("The weather is nice.")  # Runs only if both conditions are True
else:
    print("The weather is not ideal.")  # Runs otherwise

# ----------------------------------------------------

# Example 5️⃣: Nested if statements
# You can place an if statement inside another if block.
num = 10

if num > 0:  # Outer condition: checks if num is positive
    print("Number is positive.")
    if num % 2 == 0:  # Inner condition: checks if the number is even
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("Number is negative.")  # If num <= 0

# ----------------------------------------------------

# Example 6️⃣: Login system using if ... else
username = "admin"
password = "12345"

# Both conditions must be True for successful login
if username == "admin" and password == "12345":
    print("✅ Login successful!")
else:
    print("❌ Invalid username or password.")

# ----------------------------------------------------

# Example 7️⃣: One-line if statement (Ternary Operator)
# Syntax: value_if_true if condition else value_if_false
a = 5
b = 10
result = "a is greater" if a > b else "b is greater"
print(result)  # Output: b is greater

# ----------------------------------------------------

# Example 8️⃣: Comparison operators in if statements
# ==  Equal
# !=  Not equal
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
x = 8
y = 12

if x != y:
    print("x and y are not equal")  # This will print because 8 != 12
if x <= y:
    print("x is less than or equal to y")  # This will print because 8 <= 12

# ----------------------------------------------------

# Example 9️⃣: Checking empty values in if
# In Python, the following are considered False:
# 0, "", [], {}, None
# Everything else is considered True.
value = ""

if value:
    print("Value is not empty.")
else:
    print("Value is empty.")  # This will print because value is an empty string

# ----------------------------------------------------

# Example 🔟: Getting input and checking conditions
# input() always returns a string, so we convert it to int before comparison.
user_score = int(input("Enter your score: "))

if user_score >= 90:
    print("Excellent! You got an A.")
elif user_score >= 80:
    print("Good job! You got a B.")
elif user_score >= 70:
    print("You passed with a C.")
else:
    print("You failed. Try again.")

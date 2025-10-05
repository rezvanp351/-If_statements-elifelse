# 🐍 Python If ... Else — Complete Beginner’s Tutorial

Welcome to the **Python If ... Else** tutorial!  
This repository provides a complete guide for beginners to understand how conditional statements work in Python using clear examples, code explanations, and a structured learning approach.

---

## 📘 What Are Conditional Statements?

Conditional statements in Python help your program **make decisions**.  
They check whether a condition is **True** or **False**, and then execute specific code blocks depending on the result.

**Syntax:**
```python
if condition:
    # code to execute when condition is True
elif another_condition:
    # code to execute when the first condition is False but this one is True
else:
    # code to execute if none of the conditions are True
```

---

## 🔹 Example 1: Simple If Statement
```python
x = 10
if x > 5:
    print("x is greater than 5")
```
💡 **Explanation:**  
Python checks if `x` is greater than 5. Since the condition is `True`, the message prints on the screen.

---

## 🔹 Example 2: If ... Else
```python
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")
```
🧠 **Explanation:**  
If the condition `age >= 18` is true, it prints the first message; otherwise, it runs the second one.

---

## 🔹 Example 3: If ... Elif ... Else (Multiple Conditions)
```python
score = 75
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Very Good")
elif score >= 70:
    print("Good")
else:
    print("Fail")
```
📚 **Explanation:**  
Python checks each condition one by one from top to bottom and executes only the first true condition.

---

## 🔹 Example 4: Logical Operators (`and`, `or`, `not`)
```python
temperature = 25
if temperature > 20 and temperature < 30:
    print("The weather is nice.")
else:
    print("The weather is not ideal.")
```
✅ **Explanation:**  
Using `and` means both conditions must be true for the statement to run.

---

## 🔹 Example 5: Nested If Statements
```python
num = 10
if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("Number is negative.")
```
💬 **Explanation:**  
An `if` inside another `if` is called a **nested if**.  
It helps you make decisions within another decision.

---

## 🔹 Example 6: One-Line If Statement (Ternary Operator)
```python
a = 5
b = 10
result = "a is greater" if a > b else "b is greater"
print(result)
```
✨ **Explanation:**  
A short, single-line form of the `if...else` statement, often used for quick comparisons.

---

## 🔹 Example 7: Boolean Conversion in If
```python
value = ""
if value:
    print("Value is not empty.")
else:
    print("Value is empty.")
```
💡 **Explanation:**  
Python treats empty strings (`""`), empty lists (`[]`), and zero (`0`) as **False** values.

---

## 🔹 Example 8: Login System
```python
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("✅ Login successful!")
else:
    print("❌ Invalid username or password.")
```
🔐 **Explanation:**  
Checks two conditions using `and`. Both must be true to pass the login test.

---

## 🔹 Example 9: Student Grade Checker
```python
user_score = int(input("Enter your score: "))

if user_score >= 90:
    print("Excellent! You got an A.")
elif user_score >= 80:
    print("Good job! You got a B.")
elif user_score >= 70:
    print("You passed with a C.")
else:
    print("You failed. Try again.")
```
🎓 **Explanation:**  
This is a practical use of if-elif-else — a grading system based on score ranges.

---

## 🧠 Summary Table

| Keyword | Description | Example |
|----------|--------------|----------|
| `if` | Executes when the condition is True | `if x > 5:` |
| `elif` | Adds more conditions after an `if` | `elif x == 5:` |
| `else` | Executes when all conditions are False | `else:` |
| `and` | Combines multiple conditions (all must be True) | `if a > 0 and b > 0:` |
| `or` | Combines multiple conditions (at least one must be True) | `if a > 0 or b > 0:` |
| `not` | Reverses the result of a condition | `if not a:` |

---

## 💻 How to Run This Code

Before running, ensure you have **Python 3.8 or higher** installed on your system.

1. Download or clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-if-else-tutorial.git
   ```
2. Navigate to the project directory:
   ```bash
   cd python-if-else-tutorial
   ```
3. Run the Python script:
   ```bash
   python if_else_examples.py
   ```

---

## 🏁 Output Samples

```
x is greater than 5
You are under 18.
Good
The weather is nice.
Number is positive.
It is an even number.
✅ Login successful!
b is greater
Value is empty.
```

---

## 🧩 Why This Project Is Useful
This project helps beginners understand:
- How decision-making works in Python.
- How to combine conditions with `and`, `or`, and `not`.
- How to structure readable and logical conditional code.
- Real-life use cases like login systems and grading examples.

---

## 📂 Project Structure
```
python-if-else-tutorial/
│
├── if_else_examples.py     # Main Python file with examples
├── README.md               # Documentation file (this file)
└── LICENSE (optional)
```

---

## 📎 Author
👩‍💻 **Created by:** Rezvan Panah  
📅 **Year:** 2025  
💬 **Language:** Python 3  
🎯 **Purpose:** Teaching conditional statements in Python in a clear and simple way.

---

## 💖 Support & Feedback
If this repository helped you, please consider:
- ⭐ **Starring** the repo  
- 🗨️ **Commenting** your thoughts  
- 📢 **Sharing** it with others learning Python  

Your feedback motivates more free educational content!

---

### 🔖 Tags
#Python #IfElse #LearnPython #PythonForBeginners #ConditionalStatements #PythonTutorial #ProgrammingBasics #CodingExamples #PythonCode #BeginnerFriendly

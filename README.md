# 🔢 Pattern & Range Analyzer

A simple **Python beginner project** that provides two useful features:

1. ⭐ **Pattern Generator** — User ke diye hue number ke according star pattern generate karta hai.
2. 🔍 **Range Analyzer** — Given range ke numbers ko Even/Odd check karta hai aur unka total sum calculate karta hai.
3. 🚪 **Exit** — Program ko safely close karta hai.

---

## 📌 Features

* Simple menu-driven Python program
* ⭐ Generates a right-angle star pattern
* 🔢 Checks numbers as **Even** or **Odd**
* ➕ Calculates the sum of numbers in a given range
* 🔁 Uses a continuous loop so the user can perform multiple operations
* 🚪 Exit option to stop the program
* Beginner-friendly use of `if-elif-else`, `for` loops, `while` loop, `range()`, and `%` operator

---

## 🛠️ Concepts Used

This project demonstrates some important Python concepts:

| Concept        | Use                                                |
| -------------- | -------------------------------------------------- |
| `print()`      | Output display karne ke liye                       |
| `input()`      | User se input lene ke liye                         |
| `int()`        | String input ko integer mein convert karne ke liye |
| `while` loop   | Menu ko repeatedly show karne ke liye              |
| `for` loop     | Pattern aur range ke liye                          |
| `if-elif-else` | User ki choice aur conditions check karne ke liye  |
| `range()`      | Numbers ki sequence banane ke liye                 |
| `%` operator   | Even/Odd check karne ke liye                       |
| `break`        | Program loop ko stop karne ke liye                 |
| f-string       | Dynamic output print karne ke liye                 |

---

# 🚀 How It Works

Program start hone par user ko ek menu diya jata hai:

```text
select an option from below
1.pattern
2.range analyzer
3.exit
```

User apni choice enter karta hai.

### Option 1 → Pattern

Agar user `1` select karta hai, program number of rows leta hai aur star pattern generate karta hai.

Example:

```text
enter the number : 5

*
**
***
****
*****
```

### How Pattern Works

Iske liye **nested `for` loops** use kiye gaye hain.

```python
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
```

* Outer loop → rows control karta hai.
* Inner loop → har row mein stars ki quantity control karta hai.
* `end=""` → stars ko same line mein print karta hai.
* `print()` → next row par move karta hai.

---

# 🔍 Option 2 → Range Analyzer

Agar user `2` select karta hai, program starting aur ending number leta hai.

Example:

```text
enter a number of rows : 1
enter a number of rows : 5
```

Program har number ko check karega:

```text
the number is 1 odd
the number is 2 even
the number is 3 odd
the number is 4 even
the number is 5 odd

sum of number is 15
```

### Even / Odd Logic

Even aur odd check karne ke liye `%` operator use hota hai:

```python
if i % 2 == 0:
    print(f"the number is {i} even")
else:
    print(f"the number is {i} odd")
```

Agar kisi number ko `2` se divide karne par remainder `0` aaye, number **Even** hai.

```text
4 % 2 = 0 → Even
```

Agar remainder `0` nahi hai, number **Odd** hai.

```text
3 % 2 = 1 → Odd
```

### Sum Calculation

Range ke har number ko total mein add kiya jata hai:

```python
total = total + i
```

Example:

```text
1 + 2 + 3 + 4 + 5 = 15
```

---

# 🚪 Option 3 → Exit

Agar user `3` select karta hai:

```text
exiting the program. goodbye
```

Program `break` statement ki help se `while` loop ko stop kar deta hai.

```python
elif choice == "3":
    print("exiting the program. goodbye")
    break
```

---

# 🔄 Program Flow

```text
             START
               │
               ▼
      Welcome Message
               │
               ▼
          Show Menu
               │
               ▼
        User Selects Option
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
   Pattern   Range     Exit
       │     Analyzer     │
       │       │          │
       ▼       ▼          ▼
    Stars   Even/Odd     BREAK
            + Sum          │
       │       │           ▼
       └───────┴──────►  END
               │
               ▼
          Show Menu Again
```

---

# 💻 Complete Code

```python
print("Welcome to Pattern and Range Analyzer")
print()

while True:

    print("Select an option from below")
    print("1. Pattern")
    print("2. Range Analyzer")
    print("3. Exit")

    choice = input("Select number: ")

    # Pattern Generator
    if choice == "1":

        number = int(input("Enter the number: "))

        for i in range(1, number + 1):
            for j in range(1, i + 1):
                print("*", end="")
            print()

        print()

    # Range Analyzer
    elif choice == "2":

        total = 0

        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        for i in range(start, end + 1):

            if i % 2 == 0:
                print(f"The number is {i} even")
            else:
                print(f"The number is {i} odd")

            total = total + i

        print(f"Sum of numbers is {total}")
        print()

    # Exit
    elif choice == "3":

        print("Exiting the program. Goodbye!")
        break

    # Invalid Input
    else:

        print("Enter valid input!")
```

---

# ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check it using:

```bash
python --version
```

### 2. Save the File

Save the program as:

```text
|
|___main.py
|
|___output.png
|
|___README.md
```

### 3. Run the Program

Open the terminal in the project folder and run:

```bash
python main.py
```

---

# 🧪 Example

```text
Welcome to Pattern and Range Analyzer

Select an option from below
1. Pattern
2. Range Analyzer
3. Exit

Select number: 1
Enter the number: 4

*
**
***
****

Select an option from below
1. Pattern
2. Range Analyzer
3. Exit

Select number: 2
Enter starting number: 1
Enter ending number: 5

The number is 1 odd
The number is 2 even
The number is 3 odd
The number is 4 even
The number is 5 odd

Sum of numbers is 15

Select an option from below
1. Pattern
2. Range Analyzer
3. Exit

Select number: 3
Exiting the program. Goodbye!
```

---

# 📚 What I Learned

Through this project, I practiced:

* Python variables
* User input
* Type conversion
* `while` loops
* `for` loops
* Conditional statements
* `range()`
* Modulus `%` operator
* `break` statement
* f-strings
* Basic problem-solving and program flow

---

# 🔮 Future Improvements

Some features that can be added later:

* 🔺 More types of patterns
* 🔢 Count total even and odd numbers
* 📊 Find maximum and minimum number
* 🧮 Calculate average
* 🎨 Add more menu options
* 📝 Save analysis results to a file

---

## 👨‍💻 Project Status

indrajit sinh



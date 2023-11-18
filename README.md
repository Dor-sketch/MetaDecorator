# MetaDecorator: Python Dynamic Decorator Injection 🧙‍♂️🔧

## Overview 🌟

This Python script dynamically injects decorators into class methods of a given Python file, showcasing metaprogramming, regular expression parsing, and dynamic code execution.

![cover image](cover.png)

---

## Key Features 🛠️

- **Dynamic Decorator Injection**: Automatically injects decorators into class methods without altering the original method code.
- **Metaclass Utilization**: Leverages Python's metaclass mechanism to extend class functionalities.
- **Regular Expression Parsing**: Uses regular expressions to identify and manipulate class definitions within a Python file.
- **Dynamic Code Execution**: Executes user-provided Python code dynamically within the context of the program.

## Usage 📖

The script prompts the user to input the name of a Python file and a snippet of Python code. It then modifies the specified file by adding a metaclass to each class, which in turn applies the provided code snippet as a decorator to all methods of these classes.

### Steps 🚶‍♂️

1. Clone the repository.
2. Run [the script](meta.py) in a Python environment.
3. Follow the on-screen prompts to specify the target Python file and the code snippet for injection.

## Example Usage 🌟

2 examples are included in the repository: [fruit.py](fruit.py) and [bank.py](bank.py). The user can input the name of either file to see the script in action.

### AppleBasket Class Example 🍎

Before MetaDecorator:

```python
class AppleBasket:
    def __init__(self, color, quantity):
        self.apple_color = color
        self.apple_quantity = quantity

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)

example1 = AppleBasket("red", 4)
example2 = AppleBasket("blue", 50)

print("Example1:", example1, "\nExample2:", example2)

```

output:

```bash
Example1: A basket of 4 red apples.
Example2: A basket of 50 blue apples.
```

After MetaDecorator (with input "fruit.py" and "print(self.apple_color)"):

```bash
red
blue
Example1: red
A basket of 4 red apples.
Example2: blue
A basket of 50 blue apples.
```

### BankAccount Class Example 🏦

Before MetaDecorator:

```python
class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)

account = BankAccount("Bob", 100)
print(account)
```

output:

```bash
Your account, Bob, has 100 dollars.
```

After MetaDecorator (with input "bank.py" and "print(self.amt)"):

```bash
100
100
Your account, Bob, has 100 dollars.
```

## Application 💡

This project is particularly useful for scenarios requiring dynamic analysis or modification of existing Python code, such as in debugging, profiling, or runtime analysis.

## Disclaimer ⚠️

This script modifies source files and executes code dynamically. It should be used with caution and only with files in a safe and controlled environment.

## Academic Origins and Acknowledgements 🎓

The initial version of this script was developed as part of a university course assignment for _Defensive System-Programming (20937)_ at the Open University of Israel. It earned a perfect score of 100. Since then, the code has been extensively modified and improved to enhance its functionality and applicability.

## License 📜

This project is open-source and available under the [MIT License](LICENSE).

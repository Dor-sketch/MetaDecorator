# MetaDecorator: Python Dynamic Decorator Injection 🧙‍♂️🔧

This Python script dynamically injects decorators into class methods of a given Python file, showcasing metaprogramming, regular expression parsing, and dynamic code execution.

<div style="text-align: center;">
    <img src="./images/cover.png" width="500" hight="10"
    style="border-radius: 10px; border: 1px solid #ddd; padding: 5px;">
</div>

### Table of Contents 📑

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=2 orderedList=false} -->

<!-- code_chunk_output -->

- [Key Features 🛠️](#key-features-️)
- [Usage 📖](#usage-)
- [Example Usage 🌟](#example-usage-)
- [Application 💡](#application-)
- [Disclaimer ⚠️](#disclaimer-️)
- [Academic Origins and Acknowledgements 🎓](#academic-origins-and-acknowledgements-)
- [License 📜](#license-)

<!-- /code_chunk_output -->

---

## Key Features 🛠️

- **Dynamic Decorator Injection**: Automatically injects decorators into class methods without altering the original method code.
- **Metaclass Utilization**: Leverages Python's metaclass mechanism to extend class functionalities.
- **Regular Expression Parsing**: Uses regular expressions to identify and manipulate class definitions within a Python file.
- **Dynamic Code Execution**: Executes user-provided Python code dynamically within the context of the program.
- **User-Friendly Interface**: Provides a simple and intuitive interface for the user to interact with the script.

---

## Usage 📖

![Alt text](images/UI_demo.png?raw=true "Program main menu")

The script prompts the user to input the name of a Python file and a snippet of Python code. It then modifies the specified file by adding a metaclass to each class, which in turn applies the provided code snippet as a decorator to all methods of these classes.

### Steps 🚶‍♂️

1. Clone the repository.
2. Run [the script](meta.py) in a Python environment.
3. Follow the on-screen prompts to specify the target Python file and the code snippet for injection.

---
## Example Usage 🌟

Two examples are included in the repository: [fruit.py](fruit.py) and [bank.py](bank.py). The user can input the name of either file to see the script in action.

1. Automated Debugging and Tracing: You can use this mechanism to automatically add debugging or tracing outputs to each method of your classes, which logs method calls, arguments, and return values. This would be incredibly useful in a development or testing environment where you want to trace the execution flow without cluttering the codebase with log statements.
Example Usage:

    ```python
    code_to_add = r'''
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug(f"Called {__name__}.{original_function.__name__} with args={args} kwargs={kwargs}")
    '''
    import_meta_class("my_module.py", code_to_add)
    ```

2. Performance Profiling: You can use this mechanism to automatically add performance profiling to each method of your classes, which logs the time taken to execute each method. This would be incredibly useful in a performance optimization scenario where you want to identify bottlenecks in your codebase.

    Example Usage:

    ```python
    code_to_add = r'''
    import time
    start_time = time.time()
    result = original_function(*args, **kwargs)
    end_time = time.time()
    print(f"Execution of {__name__}.{original_function.__name__} took {end_time - start_time} seconds")
    return result
    '''
    ```

3. Security and Access Control: You can use this mechanism to automatically add security checks or access control to each method of your classes, which verifies the user's permissions before executing the method. This would be incredibly useful in a security-sensitive application where you want to restrict access to certain methods based on user roles or permissions.

    Example Usage:

    ```python
    code_to_add = r'''
    if not user.has_permission(__name__, original_function.__name__):
        raise PermissionError(f"User {user} does not have permission to access {__name__}.{original_function.__name__}")
    '''
    ```

4. Data Validation and Sanitization: You can use this mechanism to automatically add data validation or sanitization to each method of your classes, which ensures that the input data is valid and sanitized before executing the method. This would be incredibly useful in a data-sensitive application where you want to prevent SQL injection or other security vulnerabilities.

    Example Usage:

    ```python
    code_to_add = r'''
    for arg in args:
        if not is_valid(arg):
            raise ValueError(f"Invalid argument {arg} for {__name__}.{original_function.__name__}")
    for key, value in kwargs.items():
        if not is_valid(value):
            raise ValueError(f"Invalid value {value} for key {key} in {__name__}.{original_function.__name__}")
    '''
    ```

5. Dependency Injection: This technique could be used to modify objects at runtime to inject dependencies, for example in a test environment where you might want to inject mock objects instead of real services.

    Example Usage:

    ```python
    code_to_add = r'''
    self.database = MockDatabase()  # Assuming original_function uses self.database
    '''
    import_meta_class("database_access_module.py", code_to_add)
    ```

    5. Caching and Memoization: You can use this mechanism to automatically add caching or memoization to each method of your classes, which caches the results of the method to improve performance. This would be incredibly useful in a computationally expensive application where you want to avoid redundant calculations.

    Example Usage:

    ```python
    code_to_add = r'''
    if args in cache:
        return cache[args]
    result = original_function(*args, **kwargs)
    cache[args] = result
    return result
    '''
    import_meta_class("my_module.py", code_to_add)
    ```

6. Dynamic Feauture Toggling: This approach can facilitate the implementation of feature toggles, allowing you to enable or disable features dynamically without restarting the application or changing the actual business logic code.

    Example Usage:

    ```python
    code_to_add = r'''
    if not feature_flags.is_enabled("new_feature"):
        return None
    '''
    import_meta_class("feature_module.py", code_to_add)

    ```

### Output 📝

<table>
<tr>
    <th colspan="2">
        <div style="margin-right: 20px;">
            <img src="./images/fruit_demo.png" width="500">
        </div>
        <a href="./fruit.py">🍎 fruit.py</a> output befor and after MetaDecorator: <code>print(self.apple_color)</code>
</div>
    </th>
</tr>
<tr>
    <td>

```bash
Example1: A basket of 4 red apples.
Example2: A basket of 50 blue apples.




```

</td>
<td>

```bash
red
blue
Example1: red
A basket of 4 red apples.
Example2: blue
A basket of 50 blue apples.
```

</td>
</tr>
    <tr>
        <th colspan="2">
            <div>
                <img src="./images/bank_demo.png" width="500">
            </div>
        <a href="./bank.py">🏦 bank.py</a> output befor and after MetaDecorator: <code>print(self.amt)</code>
        </th>
    </tr>
<tr>
<td>

```bash
Your account, Bob, has 100 dollars.


```

</td>
<td>

```bash
100
100
Your account, Bob, has 100 dollars.
```

</td>
</tr>
</table>

---

## Application 💡

This project is particularly useful for scenarios requiring dynamic analysis or modification of existing Python code, such as in debugging, profiling, or runtime analysis.

## Disclaimer ⚠️

This script modifies source files and executes code dynamically. It should be used with caution and only with files in a safe and controlled environment.

## Academic Origins and Acknowledgements 🎓

The initial version of this script was developed as part of a university course assignment for _Defensive System-Programming (20937)_ at the Open University of Israel. It earned a perfect score of 100. Since then, the code has been extensively modified and improved to enhance its functionality and applicability.

## License 📜

This project is open-source and available under the [MIT License](LICENSE).

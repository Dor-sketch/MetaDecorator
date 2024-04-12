""" The code ask the user for a python file name and a python code.
    It uses a meta class to add the code to all the methods in the other file.
    It forces the classes in the other file to use the meta class,
    by writing the meta class to their definitions.
    Whith the new defenitions, the code is added to all the methods like a decorator.
    This way, it is executed every time a method is called - without changing the
    original code of the methods.
    I chose this implementation to get the minimum changes to the original code,
    whith the insparation of the "ClsProtector" and the deco-classes from my class.
"""
from typing import Type
from typing import Callable
import re  # used to find the classes in the source file
import os  # used to get the current directory


DEFAULT_FILE_NAME = "fruit.py"
DEFAULT_CODE_TO_ADD = r'print("Hello World")'


def func_decorator(original_function: Callable, custom_code: str) -> Callable:
    """
    A decorator function that enhances the behavior of an existing method.

    :param original_function: The method to which custom code will be added.
    :param custom_code: The custom code to append to the original method.

    :return: A new callable function that combines the original method and the custom code.
    """

    def decorated_function_with_custom_code(*args, **kwargs):
        # Execute the original method first
        result = original_function(*args, **kwargs)

        # Prepare the local context for executing the custom code
        local_context = {"self": args[0]} if args else {}
        local_context.update(kwargs)

        # Execute the provided custom code within the local context
        exec(custom_code, globals(), local_context)

        return result if original_function.__name__ != "__str__" else str(result)

    return decorated_function_with_custom_code
def perform_meta_class_modification(
    file_name_string: str = DEFAULT_FILE_NAME, code_to_add: str = DEFAULT_CODE_TO_ADD
) -> None:
    """
    A function to import the meta class to the source file
    it also calls the add_class_decorations function
    to add the class decorator to the source file
    """
    with open(file_name_string, "r+", encoding="utf-8") as file:
        existing_content = file.read()
        if "add_class_decorations" in existing_content:
            return
        cur_file_name_no_extnsion = os.path.splitext(os.path.basename(__file__))[0]
        file.seek(0, 0)
        file.write(
            "import time\n"
            "def get_time():\n"
            "    return time.time()\n"
            "before = get_time()\n"
            "code_to_add = '"
            + "print(get_time() - before)"
            + "'\n"
            "from "
            + cur_file_name_no_extnsion
            + " import add_class_decorations, ClassDecorator\n"
            + existing_content
        )
        file.close()

    add_class_decorations(file_name_string)


class ClassDecorator(type):
    """
    A metaclass to add code to all the methods of a class.
    code_to_add is the code to add to the methods.
    It uses the func_decorator function to add the code to the methods.
    """

    def __new__(
        mcs: Type["ClassDecorator"],
        name: str,
        bases: tuple,
        dict: dict,
        code_to_add: str,
    ):
        newcls = type.__new__(mcs, name, bases, dict)
        for attr, item in newcls.__dict__.items():
            if callable(item):  # true if item is method
                setattr(newcls, attr, func_decorator(item, code_to_add))
        return newcls


def add_class_decorations(filename: str) -> None:
    """
    A function to find the classes in a source file with reg expressions
    :param filename: the name of the source file
    :return: None (the function changes the source file)
    """
    with open(filename, "r", encoding="utf-8") as file:
        source = file.read()

    pattern = r"class\s+(\w+)"
    # get a list of classes in source file
    matches = re.findall(pattern, source)

    if not matches:
        print("No classes found in the source file")
        return None

    for class_name in matches:
        with open(filename, "r+", encoding="utf-8") as file:
            source = file.read()
            pattern = r"class\s+" + class_name + r"\s*:"
            match = re.search(pattern, source)
            if match:
                location = int(match.end()) - 1  # -1 for ':' character
                later_content = source[location:]
                file.seek(location)
                file.write(
                    "(metaclass=ClassDecorator,code_to_add=code_to_add)" + later_content
                )
                file.truncate()
                source = file.read()


def import_meta_class(
    file_name_string: str = "fruit.py", code_to_add: str = "print('Hello World')"
) -> None:
    """
    A function to import the meta class to the source file
    it also calls the add_class_decorations function
    to add the class decorator to the source file
    """
    with open(file_name_string, "r+", encoding="utf-8") as file:
        existing_content = file.read()
        if "add_class_decorations" in existing_content:
            return  # the file is already imported
        cur_file_name_no_extnsion = os.path.splitext(os.path.basename(__file__))[0]
        file.seek(0, 0)
        file.write(
            "code_to_add = r'"
            + code_to_add
            + "'\n"
            + "from "
            + cur_file_name_no_extnsion
            + " import add_class_decorations, ClassDecorator\n"
            + existing_content
        )
        file.close()

    add_class_decorations(file_name_string)


def read_file_content(filename: str) -> str:
    """
    Read and return the content of a file.
    :param filename: the name of the file to read.
    :return: the content of the file as a string.
    :raises FileNotFoundError: if the file does not exist.
    :raises IOError: if the file cannot be read.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except (FileNotFoundError, IOError) as e:
        raise e  # Re-raise the exception to be handled by the caller


def restore_file_content(filename, content):
    """
    Restore original content
    :param filename: the name of the file to restore
    :param content: the original content of the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)



file = "fruit.py"
# try the perform_meta_class_modification function
perform_meta_class_modification(file)
# try the import_meta_class function
# import_meta_class(file)
# # try the add_class_decorations function
# add_class_decorations(file)
# # try the read_file_content function
# print(read_file_content(file))
exec(open(file).read())
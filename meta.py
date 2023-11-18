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
import re   # used to find the classes in the source file
import os   # used to get the current directory


def func_decorator(f, code_to_add_input):
    """
    A function to add code to a method.
    :param f: the method to add code to.
    :param code_to_add_input: the code to add to the method.
    :return: the method with the code added to it.
    """
    def ret(*args, **kwargs):
        # Execute the original method first
        result = f(*args, **kwargs)

        # Prepare the local context for the exec function
        local_context = {'self': args[0]} if args else {}
        local_context.update(kwargs)

        # Execute the provided code snippet in the local context
        exec(code_to_add_input, globals(), local_context)

        return result if f.__name__ != '__str__' else str(result)
    return ret


class Class_Decorator(type):
    """
    A meta class to add code to all the methods of a class.
    code_to_add is the code to add to the methods
    it uses the func_decorator function to add the code to the methods
    """
    def __new__(cls, name, bases, dict, code_to_add):
        newcls = type.__new__(cls, name, bases, dict)
        for attr, item in newcls.__dict__.items():
            if callable(item):  # true if item is method
                setattr(newcls, attr, func_decorator(item, code_to_add))
        return newcls


def add_class_decorations(filename):
    """
    A function to find the classes in a source file with reg expressions
    :param filename: the name of the source file
    :return: a list of tuples containing the class name and the line number
    """
    with open(filename, "r", encoding='utf-8') as file:
        source = file.read()

    pattern = r"class\s+(\w+)"
    # get a list of classes in source file
    matches = re.findall(pattern, source)

    if not matches:
        print("No classes found in the source file")
        return None

    for class_name in matches:
        with open(filename, "r+", encoding='utf-8') as file:
            source = file.read()
            pattern = r"class\s+" + class_name + r"\s*:"
            match = re.search(pattern, source)
            if match:
                location = int(match.end()) - 1  # -1 for ':' character
                later_content = source[location:]
                file.seek(location)
                file.write("(metaclass=Class_Decorator,code_to_add=code_to_add)"
                           + later_content)
                file.truncate()
                source = file.read()


def import_meta_class(file_name_string="fruit.py", code_to_add="print('Hello World')"):
    """
    A function to import the meta class to the source file
    it also calls the add_class_decorations function
    to add the class decorator to the source file
    """
    with open(file_name_string, "r+", encoding='utf-8') as file:
        existing_content = file.read()
        if "add_class_decorations" in existing_content:
            return None  # the file is already imported
        cur_file_name_no_extnsion = os.path.splitext(
            os.path.basename(__file__))[0]
        file.seek(0, 0)
        file.write("code_to_add = r'" + code_to_add + "'\n"
                   + "from " + cur_file_name_no_extnsion +
                   " import add_class_decorations, Class_Decorator\n"
                   + existing_content)
        file.close()

    add_class_decorations(file_name_string)


def backup_file_content(filename):
    """
    Backup the original content of a file
    :param filename: the name of the file to backup
    :return: the original content of the file
    """
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()


def restore_file_content(filename, content):
    """
    Restore original content
    :param filename: the name of the file to restore
    :param content: the original content of the file
    """
    with open(filename, "w", encoding='utf-8') as file:
        file.write(content)


if __name__ == "__main__":
    # make sure the current directory is the same as the source file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    main_file_name_string = input(
        "Enter python file name or press enter for default (fruit.py): ")
    if not main_file_name_string:
        main_file_name_string = "fruit.py"
    while not os.path.exists(main_file_name_string):
        print("File does not exist - please try again, or press \"q\" to quit")
        main_file_name_string = input("Enter python file name: ")
        if main_file_name_string == "q":
            exit()

    original_content = backup_file_content(
        main_file_name_string)  # Backup original content

    code_to_add = input(
        "Enter a python code or press enter for default (print(\"Hello World\")): ")
    if not code_to_add:
        code_to_add = r'print("Hello World")'
    # add the meta class to the source file and change classes definition to use it
    import_meta_class(main_file_name_string, code_to_add)

    with open(main_file_name_string, "r", encoding='utf-8') as f:  # run the source file
        main_code = f.read()
        exec(main_code)

    restore_file_content(main_file_name_string, original_content)

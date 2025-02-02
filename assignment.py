def format_string(name, age):
    """
    Create a formatted string using f-strings.
   Args:
       name (str): Person's name
       age (int): Person's age
   Returns:
       str: Formatted string
   """
    return f"My name is {name} and I am {age} years old"
    pass

def conditional_check(number):
    """
   Check if a number is greater, lesser, or equal to 10.
   Args:
       number (int): Number to check
   Returns:
       str: "Greater", "Lesser", or "Equal"
   """

    if number > 10 :
        return 'Greater'
    elif number < 10 :
        return 'Lesser'
    else:
        return 'Equal'
    pass

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for num in range(1, n +1):
        sum += num
    return sum
    pass

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    return (sum(numbers), max(numbers), min(numbers))
    pass

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    names =[]
    for key, value in students_dict.items():
        if value > 80:
            names.append(key)
    return names
    pass

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements =set()
    for i in list1:
        if i in list2:
            common_elements.add(i)
    return common_elements
    pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {'sum': a + b, 'difference': a - b, 'product': a * b, 
            'quotient': a / b if b!= 0 else None }

    pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {'and': x and y, 'or': x or y,
            'not_x': not x}
    pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {'and': a & b, 'or': a | b, 
            'xor': a ^ b}
    pass

def format_string(name, age):
    return f"My name is {name} and I am {age} years old".format(name, age)
    pass 

def conditional_check(number):
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"
    pass

def loop_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total 
    pass

def list_operations(numbers):
    Sum = sum(numbers)
    Max = max(numbers)
    Min = min(numbers)
    return (Sum, Max, Min)
    pass

def dict_operations(students_dict):
    result = []
    for name , score in students_dict.items():
        if score > 80:
            result.append(name)
    return result
    pass

def set_operations(list1, list2):
   set1 = set(list1)
   set2 = set(list2)
   return set1 & set2
   pass

def arithmetic_ops(a, b):
    return {
        "sum": a + b, 
        "difference": a - b, 
        "product": a * b, 
        "quotient": a / b
    }
    pass

def logical_ops(x, y):
    return { 
      "and": x and y, 
      "or" : x or y , 
      "not_x" : not x  
    }
    pass

def bitwise_ops(a, b):
   return {
    "and": a & b, 
    "or" : a | b, 
    "xor": a ^ b
   }
   pass

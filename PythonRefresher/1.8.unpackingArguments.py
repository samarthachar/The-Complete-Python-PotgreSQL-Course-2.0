def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product
    
print(multiply(3,3,3))

def add(x,y):
    return x + y

nums = [3,5]
print(add(*nums))

nums = {"x": 15, "y": 25}
print(add(**nums))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator providided to apply()."

print(apply(1,2,3,6,7, operator="*"))
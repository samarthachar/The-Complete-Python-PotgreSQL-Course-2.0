def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Error: Divisor cannot be 0")
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)

    
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find and element with {expected}" )
                       

friends = [
    {"name": "Tony" , "age": 50},
    {"name": "Satoru", "age": 29},
    {"name": "Itachi", "age": 19},
    {"name":"Seishiro", "age":17}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Satoru", get_friend_name))
print(search(friends, "Satoru", lambda friend: friend["name"]))
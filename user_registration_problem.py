import re

def UC01_valid_first_name(name):
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    if re.match(pattern, name):
        return True
    return False

print(UC01_valid_first_name("Hari"))
print(UC01_valid_first_name("Ha"))  
print(UC01_valid_first_name("hari"))
print(UC01_valid_first_name("Hari123"))
 
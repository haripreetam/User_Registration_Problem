import re

def UC01_valid_first_name(name):
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    if re.match(pattern, name):
        return "Valid first name"
    else:
        return "Invalid first name"


def UC02_valid_last_name(name):
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    if re.match(pattern, name):
        return "Valid last name"
    else:
        return "Invalid last name"

#for full name ^[A-Z][a-zA-Z]{2,}\s[A-Z][a-zA-Z]{2,}$ 

print(UC01_valid_first_name("Hari"))
print(UC01_valid_first_name("Ha"))  
print(UC02_valid_last_name("reddy"))
print(UC02_valid_last_name("Reddy"))
 
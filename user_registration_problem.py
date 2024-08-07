import re

def valid_first_name(name):
    '''Description : To validate the first name using regex pattern.
        Parameters : name - It is a string 
        Return : 'Valid first name' if the name is valid, else 'Invalid first name
    '''
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    if re.match(pattern, name):
        return "Valid first name"
    else:
        return "Invalid first name"

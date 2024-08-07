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
    
    
def valid_last_name(name):
    '''Description : To validate the last name using regex pattern.
        Parameters : name - It is a string 
        Return : 'Valid last name' if the name is valid, else 'Invalid last name
    '''
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    if re.match(pattern, name):
        return "Valid last name"
    else:
        return "Invalid last name"
    
    #for full name ^[A-Z][a-zA-Z]{2,}\s[A-Z][a-zA-Z]{2,}$ 


def valid_email(email):
    '''Description : To validate the email using regex pattern.
        Parameters : email - It is a string 
        Return : 'Valid email' if the name is valid, else 'Invalid email'
    '''
    pattern = r'^([a-zA-Z0-9]{3,})+(\.[a-zA-Z0-9]+)?@[a-zA-Z]{2,}\.[a-z]{2,}(?:\.[a-zA-Z]{2,})?$'
    #if more than two domain like ".gov.co.uk" then you can use '(){0,2}'
    if re.match(pattern, email):
        return "Valid email"
    else:
        return "Invalid email"
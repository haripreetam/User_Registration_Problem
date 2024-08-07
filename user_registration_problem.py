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
    

def valid_mobile_number(mobile_number):
    '''Description : To validate the mobile number using regex pattern.
        Parameters : mobile_number - It is a sequence of intergers
        Return : 'Valid mobile number' if the name is valid, else 'Invalid mobile number'
    '''
    pattern = r'^[0-9]{2}\s[0-9]{10}$'
    if re.match(pattern, mobile_number):
        return "Valid mobile number"
    else:
        return "Invalid mobile number"
    
def valid_password_r1(password):
    '''Description : To validate the password using regex pattern.
        Parameters : password - It is a string 
        Return : 'Valid password' if the name is valid, else 'Invalid password'
    '''
    # rule_1 pattern = r'^[a-zA-Z]{8,}$'
    # rule_2 pattern = r'^(?=.*[A-Z])[a-zA-Z]{8,}$'
    # rule_3 pattern = r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|-])[a-zA-Z\d!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|-]{8,}$'
    if re.match(pattern, password):
        return "Valid password"
    else:
        return "Invalid password"
    
 
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email: ")
mobile_number = input("Enter mobile number: ")
password = input("Enter the password")

print(valid_first_name(first_name))
print(valid_last_name(last_name))
print(valid_email(email))
print(valid_mobile_number(mobile_number))
print(valid_password_r1(password))
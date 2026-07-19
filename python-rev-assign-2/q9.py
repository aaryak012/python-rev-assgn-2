#Q9
def check_password(pwd):
    has_length = len(pwd) > 8
    has_number = any(char.isdigit() for char in pwd)
    
    return has_length and has_number


print(check_password("hello12345"))  
print(check_password("hello"))       
print(check_password("longpassword")) 
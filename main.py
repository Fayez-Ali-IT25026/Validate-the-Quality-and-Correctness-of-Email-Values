email = "fayez@.com"
valid = True
#Clean the email address by removing any leading or trailing whitespace
email = email.strip() #strips whitespace from the beginning and end of the email string

if email == "":
    print("Email address can not be empty.")
    valid = False
if "@" not in email and "." not in email:
    print("Email address is invalid.")  
    valid = False
if email.count('@') !=1:
    print("Email address must contain exactly one '@' symbol.") 
    valid = False
#endswith() method checks if the email address ends with a valid domain (.com, .net, .org)
if not email.endswith(('.com', '.net', '.org')):
    print("Email address must end with a valid domain (.com, .net, .org).")
    valid = False
#len() function checks the length of the email address
if len(email) > 254 :
    print("Email address is too long. Maximum length is 254 characters.")
    valid = False
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email address must start and end with an alphanumeric character.")
    valid = False
if valid:
    print("Email address is valid.")
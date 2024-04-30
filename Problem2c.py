import hashlib
from datetime import datetime
import os

# write the given user, password and role as parameters to the password file
def write_to_file(username, password, role) -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    salt = str(os.urandom(128))
    s = "" # password record consists of a string
    s += username
    s += ";" # use the ; character as the separator between important components of the record
    s += hashlib.sha3_512(password.encode('utf-8')).hexdigest() # hash the password and create a salt to append onto the password
    s += hashlib.sha3_512(salt.encode('utf-8')).hexdigest()
    s += ";"
    s += str(role)
    s += ";"
    s += str(current_time)
    s += ";"
    s += hashlib.sha3_512(salt.encode('utf-8')).hexdigest()
    s += ";"
    s += "\n" # new line to distinguish between users
    
    with open('passwd.txt', 'a') as f:
        f.writelines(s) # write this user down as a user in the file

# Check to see if the user exists in the file
def check_user_in_passwd_file(user, passwrd) -> bool:
    f = open("passwd.txt")
    s = f.readlines()
    for p in s:
        hashed = hashlib.sha3_512(passwrd.encode('utf-8')).hexdigest()
        salt = p.split(";")[4]
        if p.split(";")[0] == user and p.split(";")[1] == hashed + salt:
            return True # if the user and password exist return True, otherwise return False
    return False

# Here we actually retrieve the data of the user to be used.
def retrieve_user_data(user, passwrd) -> []:
    f = open("passwd.txt")
    s = f.readlines()
    for p in s:
        hashed = hashlib.sha3_512(passwrd.encode('utf-8')).hexdigest()
        salt = p.split(";")[4]
        if p.split(";")[0] == user and p.split(";")[1] == hashed + salt:
            return p   
        

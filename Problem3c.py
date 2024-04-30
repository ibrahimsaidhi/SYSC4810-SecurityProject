import Problem2c
import time

# helper that allows for the user to enter their given role into the system.
def enrollment_helper(username, password) -> None:
    flag = True
    print("Please enter one of the following options to let us know your role in the company")
    print("---------------------------------------------------------------------------------")
    print("[1001]: Client | [1002]: Premium Client | [1003]: Financial Advisor | [1004]: Financial Planner | [1005]: Teller ")
    print("[1006]: Compliance Officer | [1007]: Investment Analyst | [1008]: Technical Support")
    print("---------------------------------------------------------------------------------")
    while (flag):
        role = int(input("Enter role number: "))
        if role >= 1001 and role < 1009:
            Problem2c.write_to_file(username, password, role) # once we've gotten here, the user is fully enrolled into the system, and their credentials are saved into the passwd file
            flag = False
        else: 
            print("Not a valid role. Please try again")

    
def enrollment_mechanism() -> None:
    with open('blacklist.txt') as f:
        blacklist = f.read() # read from a blacklist that contains a lot of common passwords that aren't secure enough to use
    check = True
    username = ""
    # allow user to create a fresh username. An attempt to use an existing username results in another attempt
    while (check):
        found = False
        user = input("Enter a valid username: ")
        pass_f = open('passwd.txt', 'r')
        lines = pass_f.readlines()
        for l in lines:
            if l.split(";")[0] == user:
                found = True
        if found == True:
            print("Username is already taken, please enter another username")
        elif found == False:
            username = user
            check = False  
                
    flag = True
    upper = False
    lower = False
    number = False
    special = False
    print("Enter a password. Passwords must be at least 8 characters long and contain a lowercase, uppercase, and special letter")
    
    while flag:
        password = input("Enter password: ")
        spec = '[@!#$%&*?]'
        # here we run through the guidelines set by Finvest Holdings regarding passwords. This is our password checker!
        if password in blacklist:
            print("Sorry this password has been considered too weak, and may put your account at risk of being comprimised. Please enter a stronger password")
        elif password == username:
            print("The password must be distinct from the username. Try again")
        elif len(password) < 8:
            print("Password is less than 8 characters long. Please enter a longer password")        
        elif len(password) >= 8:
            for e in password:
                if e.isupper():
                    upper = True
                elif e.islower():
                    lower = True
                elif e.isnumeric():
                    number = True
                elif e in spec:
                    special = True

            if upper == True and lower == True and special == True and number == True: 
                flag = False
                print("Enrolled. Welcome to Finvest Holdings!")
                time.sleep(1)
                enrollment_helper(username, password) # if we get here, the password is safe to use. Now we determine the role of the user
            else:
                print("This password is missing either an uppercase letter, a lowercase letter, a number, or a special character") # otherwise the password is not safe!
                upper = False
                lower = False
                special = False
                number = False


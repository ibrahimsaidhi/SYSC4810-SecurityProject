import Problem1d
import Problem2c
import Problem3c
from datetime import datetime

# pieces together the enrollment and login mechanisms
def start_system() -> None:
    print("---------------------------------------------------")
    print("Finvest Holdings")
    print("Client Holdings and Information System")
    print("---------------------------------------------------")
    print("[E]: Sign-up with Finvest Holdings | [L]: Login | [Q]: Quit")
    print("---------------------------------------------------")
    flag = True
    while(flag):
        command = input("Enter command: ")

        #check command value
        if command == "Q":
            print("Quitting.... goodbye")
            flag = False
        elif command == "E":
            Problem3c.enrollment_mechanism() #enroll the user using the mechanism from Problem3c.py
            print("You are now fully enrolled in Finvest Holdings! Please login to the system again..")
            flag = False
        elif command == "L":
            user = input("Enter Username: ")
            passwd = input("Enter Password: ") # enter the credentials of the user
            if Problem2c.check_user_in_passwd_file(user, passwd) == True:
                print("Access Granted")
                arr = Problem2c.retrieve_user_data(user, passwd).split(";") #retrieve the user from the passwd file
                navigate_system(arr) # allow this user to navigate the system
                flag = False
            else:
                print("Incorrect credentials. Try again") # credentials are wrong, try again...
            
        else:
            print("Not a valid command")

# Connects the access-control matrix created in Problem1d.py after the user logs in
def navigate_system(user) -> None:
    print("Welcome " + user[0] + "!")
    print("----------------------------------------------")
    print("Main Menu:")
    # check the groupID of the user and provide the access control level they can carry by inputting their role as the argument to Problem1d.py's access control mech
    if user[2] == "1001":
        print("Role: Client")
        print("Commands are listed below...")
        print("| View Investment Portfolio | View Financial Advisor | View Account Balance |")
        Problem1d.access_control("Client")
    elif user[2] == "1002":
        print("Role: Premium Client")
        print("Commands are listed below...")
        print("| View Investment Portfolio | View Financial Advisor | View Financial Planner | View Investment Analyst | View Account Balance |")
        Problem1d.access_control("Premium Client")
    elif user[2] == "1003":
        print("Role: Financial Advisor")
        print("Commands are listed below...")
        print("| View Investment Portfolio | View Account Balance | Private Consumer Instruments |")
        Problem1d.access_control("Financial Advisor")
    elif user[2] == "1004":
        print("Role: Finanical Planner")
        print("Commands are listed below...")
        print("| View Investment Portfolio | View Account Balance | View Money Market Instruments | Private Consumer Instruments |")
        Problem1d.access_control("Financial Planner")
    elif user[2] == "1005":
        print("Role: Teller")
        print("Commands are listed below...")
        print("| View Investment Portfolio | View Account Balance |")
        Problem1d.access_control("Teller")
    elif user[2] == "1006":
        print("Role: Compliance Officer")
        print("Commands are listed below...")
        print("| View Account Balance | Validate Portfolio Modification |")
        Problem1d.access_control("Compliance Officer")
    elif user[2] == "1007":
        print("Role: Investment Analyst")
        print("Commands are listed below...")
        print("| View Investment Portfolio | View Account Balance | View Money Market Instruments | View Derivatives Trading | View Interest Instruments | Private Consumer Instruments |")
        Problem1d.access_control("Investment Analyst")
    elif user[2] == "1008":
        print("Role: Techncial Support")
        print("Commands are listed below...")
        print("| View Client Info |")
        Problem1d.access_control("Technical Support")


if __name__ == "__main__":
    start_system()
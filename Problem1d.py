#Function that creates an emulation of the access control policy suggested by Finvest Holdings
#Ibrahim Said, 101158275

def access_control(system_role) -> None:
    # the following are the access control permissions for each component of the system, stored as dictionaries.
    portfolio_access_dict = {
        "Client" : "r-",
        "Premium Client": "rw",
        "Financial Advisor": "rw",
        "Financial Planner": "rw",
        "Investment Analyst": "rw",
        "Teller": "r-",
        "Compliance Officer": "r-",
        "Technical Support": "--"
    }
    balance_access_dict = {
        "Client" : "r-",
        "Premium Client": "r-",
        "Financial Advisor": "r-",
        "Financial Planner": "r-",
        "Investment Analyst": "r-",
        "Teller": "r-",
        "Compliance Officer": "r-",
        "Technical Support": "--"
    }
    pci_access_dict = {
        "Client" : "--",
        "Premium Client": "--",
        "Financial Advisor": "r-",
        "Financial Planner": "r-",
        "Investment Analyst": "r-",
        "Teller": "--",
        "Compliance Officer": "--",
        "Technical Support": "--"
    }
    invest_access_dict = {
        "Client" : "--",
        "Premium Client": "--",
        "Financial Advisor": "--",
        "Financial Planner": "--",
        "Investment Analyst": "r-",
        "Teller": "--",
        "Compliance Officer": "--",
        "Technical Support": "--"
    }
    money_market_access_dict = {
        "Client" : "--",
        "Premium Client": "--",
        "Financial Advisor": "--",
        "Financial Planner": "r-",
        "Investment Analyst": "r-",
        "Teller": "--",
        "Compliance Officer": "--",
        "Technical Support": "--"
    }
    derivatives_trading_dict = {
        "Client" : "--",
        "Premium Client": "--",
        "Financial Advisor": "--",
        "Financial Planner": "--",
        "Investment Analyst": "r-",
        "Teller": "--",
        "Compliance Officer": "--",
        "Technical Support": "--"
    }
    view_financial_planner_dict = {
        "Client" : "--",
        "Premium Client": "r-",
        "Financial Advisor": "--",
        "Financial Planner": "--",
        "Investment Analyst": "--",
        "Teller": "--",
        "Compliance Officer": "--",
        "Technical Support": "--"
    }
    view_financial_advisor_dict = {
        "Client" : "r-",
        "Premium Client": "r-",
        "Financial Advisor": "--",
        "Financial Planner": "--",
        "Investment Analyst": "--",
        "Teller": "--",
        "Compliance Officer": "--",
        "Technical Support": "--"
    }

    view_investment_analyst_dict = {
        "Client" : "--",
        "Premium Client": "r-",
        "Financial Advisor": "--",
        "Financial Planner": "--",
        "Investment Analyst": "--",
        "Teller": "--",
        "Compliance Officer": "--",
        "Technical Support": "--"
    }

    view_client_info_dict = {
        "Client" : "r-",
        "Premium Client": "r-",
        "Financial Advisor": "--",
        "Financial Planner": "--",
        "Investment Analyst": "--",
        "Teller": "--",
        "Compliance Officer": "--",
        "Technical Support": "r-"
    }

    validate_dict = {
        "Client" : "--",
        "Premium Client": "--",
        "Financial Advisor": "--",
        "Financial Planner": "--",
        "Investment Analyst": "--",
        "Teller": "--",
        "Compliance Officer": "r-",
        "Technical Support": "--"
    }
    

    flag = True
    while (flag):
        system_component = input("Enter the component of the system you wish to view: ")
        command = input("Do you want to view or modify? Enter V/M (or Q to quit): ")
        # check the command to see if the user still wants to continue. Quit if they don't
        if command == "Q":
            flag = False
            print("Quitting...")
        # check the permissions for each system component by going through the respective dictionary and checking it with the role that was passed in as an argument
        # grant or deny permissions accordingly
        elif system_component == "View Investment Portfolio":
            if portfolio_access_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif portfolio_access_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif portfolio_access_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif portfolio_access_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "View Account Balance":
            if balance_access_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif balance_access_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif balance_access_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif balance_access_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "Private Consumer Instruments":
            if pci_access_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif pci_access_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif pci_access_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif pci_access_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "View Interest Investments":
            if invest_access_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif invest_access_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif invest_access_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif invest_access_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "View Money Market Instruments":
            if money_market_access_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif money_market_access_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif money_market_access_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif money_market_access_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "View Derivatives Trading":
            if derivatives_trading_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif derivatives_trading_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif derivatives_trading_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif derivatives_trading_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "View Financial Planner":
            if view_financial_planner_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif view_financial_planner_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif view_financial_planner_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif view_financial_planner_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "View Financial Advisor":
            if view_financial_advisor_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif view_financial_advisor_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif view_financial_advisor_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif view_financial_advisor_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")
            
        elif system_component == "View Client Info":
            if view_client_info_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif view_client_info_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif view_client_info_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif view_client_info_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "Validate Portfolio Modification":
            if validate_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif validate_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif validate_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif validate_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")

        elif system_component == "View Investment Analyst":
            if view_investment_analyst_dict.get(system_role)[0] == "-" and command == "V":
                print("Permission denied")
            elif view_investment_analyst_dict.get(system_role)[0] == "r" and command == "V":
                print("Permission granted")
            elif view_investment_analyst_dict.get(system_role)[1] == "w" and command == "M":
                print("Permission granted")
            elif view_investment_analyst_dict.get(system_role)[1] == "-" and command == "M":
                print("Permission declined")
        # if the role is not valid, give the user another try.
        else:
            print("Invalid role or component. Try again...")

        
    print("Logging out... Goodbye!")


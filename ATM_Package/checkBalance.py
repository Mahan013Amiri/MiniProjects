from ATM_Package.csvManagement import showBalanc

def checkBalance(AccountID):
    print(f"Your Balance:{showBalanc(AccountID)}")
    choice_=input("Would you like to do anything else? Y/N")
    return choice_


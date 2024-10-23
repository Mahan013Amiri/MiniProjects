from  ATM_Package.csvManagement import showTH

def checkTH(AccountID):
    print(f"Your Transaction History:{showTH(AccountID)}")
    choice_ = input("Would you like to do anything else? Y/N")
    return choice_
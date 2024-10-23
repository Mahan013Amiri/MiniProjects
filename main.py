from ATM_Package import AccountAccess, transfer, withdraw, checkBalance, updatePassword, TransactionHistory


def accessMenu():
    print("\t1)Sign Up\n", "\t2)LogIn\n", "\t0)Exit")
    while True:
        choice = input("your choice:")
        if choice == "1":
            AccountAccess.signUp()
            accessMenu()
            break
        elif choice == "2":
            userAccount = AccountAccess.logIn()
            serviceDashboard(userAccount)
            break
        elif choice == "0":
            print("goodbye")
            break
        else:
            print("wrong choice")


def serviceDashboard(userID):
    while True:
        print("\n\t[Features]")
        print("\n1)Balance\n2)Withdraw\n3)Transfer\n4)TransactionHistory\n5)ChangePassword\n6)SwitchAccount\n0)Exit")
        choice = input("your choice:")
        if choice == "0":
            print("goodbye\n", 40 * "*")
            break
        elif choice == "1":
            choice2 = checkBalance.checkBalance(userID)
            if choice2.lower() == "y":
                continue
            else:
                print("Finish")
                print("*" * 40)
                break
        elif choice == "2":
            choice2 = withdraw.withdraw(userID)
            if choice2.lower() == "y":
                continue
            else:
                print("Finish")
                print("*" * 40)
                break
        elif choice == "3":
            choice3 = transfer.transfer(userID)
            if choice3.lower() == "y":
                continue
            else:
                print("Finish")
                print("*" * 40)
                break
        elif choice == "4":
            choice2 = TransactionHistory.checkTH(userID)
            if choice2.lower() == "y":
                continue
            else:
                print("Finish")
                print("*" * 40)
                break
        elif choice == "5":
            choice2 = updatePassword.change_password(userID)
            if choice2.lower() == "y":
                continue
            else:
                print("Finish")
                print("*" * 40)
                break
        elif choice == "6":
            accessMenu()
        else:
            print("wrong choice")


accessMenu()

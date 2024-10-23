import random
from ATM_Package.csvManagement import appendSignup_csv, id_exist,checkPass,getId

def signUp():
    name = input("name:")
    password = input("password:")
    seedMoney = input("seedMoney:").lstrip("0")
    while True:
        if not name.isalpha():
            print("dont use number in name")
            name = input("name:")
        if (not password.isalnum()) or (len(password) != 4):
            print("Dont use alphabet in password and The password must be 4 digits long")
            password = input("password:")
        if not seedMoney.isdigit():
            print("dont use alphabet in seedMoney")
            seedMoney = input("seedmoney:")
        break
    accountID = ""
    for i in range(1, 17):
        accountID += str(random.randrange(0, 10))
        if i % 4 == 0:
            accountID += "-"
    accountID = accountID.rstrip("-")
    account = {
        "name": name,
        "password": password,
        "seedMoney": int(seedMoney),
        "accountID": accountID
    }
    appendSignup_csv(account)

# def getId():
#     username = input("enter your AccountID:")
#     return username

def logIn():
    while True:
        username=getId()
        if id_exist(username):
            password = input("enter your password:")
            if checkPass(username,password):
                print("welcome to your account\n",40*"*")
                return username
            else:
                print("your password is wrong")
        else:
            print(f"this {username} isn't exist!")




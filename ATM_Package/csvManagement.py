import csv


def appendSignup_csv(account_data):
    data = {
        "Name": account_data["name"],
        "AccountID": account_data["accountID"],
        "Password": account_data["password"],
        "Balance": account_data["seedMoney"],
        "TransactionHistory": []
    }
    print(data)
    with open("databaseCSV.csv", mode="a", newline="") as file:
        fieldnames = ["Name", "AccountID", "Password", "Balance", "TransactionHistory"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
        file.seek(0, 2)  # حرکت به انتهای فایل
        if file.tell() == 0:  # اگر فایل خالی بود
            writer.writeheader()
        # نوشتن یک ردیف به فایل CSV
        writer.writerow(data)
        file.flush()


def id_exist(id):
    with open("databaseCSV.csv", "r") as file:
        reader_ = csv.DictReader(file)
        for line in reader_:
            id_account = [line["AccountID"]]
            if id in id_account:
                return True


def checkPass(id, password):
    with open("databaseCSV.csv", "r") as file:
        reader_ = csv.DictReader(file)
        for line in reader_:
            if line["AccountID"] == id and line["Password"] == password:
                return True


def getId():
    username = input("enter your AccountID:")
    return username


def showPass(id):
    with open("databaseCSV.csv", "r") as file:
        reader_ = csv.DictReader(file)
        for line in reader_:
            if line["AccountID"] == id:
                password = line["Password"]
                return password


def showBalanc(id):
    with open("databaseCSV.csv", "r") as file:
        reader_ = csv.DictReader(file)
        for line in reader_:
            if line["AccountID"] == id:
                balance = line["Balance"]
                return int(balance)


def showName(id):
    with open("databaseCSV.csv", "r") as file:
        reader_ = csv.DictReader(file)
        for line in reader_:
            if line["AccountID"] == id:
                name = line["Name"]
                return name


def showTH(id):
    with open("databaseCSV.csv", "r") as file:
        reader_ = csv.DictReader(file)
        for line in reader_:
            if line["AccountID"] == id:
                TH = line["TransactionHistory"]
                return TH


def checkBalanceCSV():
    ...

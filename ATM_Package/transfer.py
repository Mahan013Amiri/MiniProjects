from ATM_Package.csvManagement import showBalanc,id_exist
import csv
def transfer(accid):
    destination_card = input("Enter the destination card number:")
    if id_exist(destination_card):
        amount=abs(int(input("Enter the amount you want to transfer:")))
        if showBalanc(accid) >amount:
            update_balanse(accid,destination_card,amount)
            choice_ = input("Would you like to do anything else? Y/N")
            return choice_
        else:
            print("Insufficient funds!")
            transfer(accid)
    else:
        print("not exist this account id!")
        transfer(accid)


def update_balanse(id1,id2,amount):
    balance1=showBalanc(id1)
    balance2=showBalanc(id2)


    # خواندن کل فایل و اعمال تغییرات
    with open("databaseCSV.csv", "r") as file:
        reader_ = csv.DictReader(file)
        lines = list(reader_)  # خواندن تمام خطوط

    # ایجاد لیست برای فیلدها
    fieldnames = reader_.fieldnames

    # تغییر خط مورد نظر
    for line in lines:
        if line["AccountID"] == id1:
            line["Balance"] = balance1-amount  # بروزرسانی موجودی
            line["TransactionHistory"] = eval(line["TransactionHistory"])
            line["TransactionHistory"].append({"Type": "Send","ID":id2, "Amount": amount})
    for line in lines:
        if line["AccountID"] == id2:
            line["Balance"] = balance2+amount  # بروزرسانی موجودی
            line["TransactionHistory"] = eval(line["TransactionHistory"])
            line["TransactionHistory"].append({"Type": "Receive", "ID": id2, "Amount": amount})
    # بازنویسی کل فایل
    with open("databaseCSV.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # نوشتن سرستون‌ها
        writer.writerows(lines)  # نوشتن کل داده‌های به‌روزشده
        file.flush()

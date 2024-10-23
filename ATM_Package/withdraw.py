from ATM_Package.csvManagement import showBalanc
import csv
def withdraw(id):
    balance=showBalanc(id)
    withdraw_ =int(input("Enter the amount you wish to withdraw:")).__abs__()
    if withdraw_ > balance:
        print("Insufficient funds")
    else:
        balance-=withdraw_

    # خواندن کل فایل و اعمال تغییرات
    with open("databaseCSV.csv", "r") as file:
        reader_ = csv.DictReader(file)
        lines = list(reader_)  # خواندن تمام خطوط

    # ایجاد لیست برای فیلدها
    fieldnames = reader_.fieldnames

    # تغییر خط مورد نظر
    for line in lines:
        if line["AccountID"] == id:
            line["Balance"] = balance  # بروزرسانی موجودی
            line["TransactionHistory"]=eval(line["TransactionHistory"])
            line["TransactionHistory"].append({"Type":"Withdraw","Amount":withdraw_})

    # بازنویسی کل فایل
    with open("databaseCSV.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # نوشتن سرستون‌ها
        writer.writerows(lines)  # نوشتن کل داده‌های به‌روزشده
        file.flush()
    choice_ = input("Would you like to do anything else? Y/N")
    return choice_
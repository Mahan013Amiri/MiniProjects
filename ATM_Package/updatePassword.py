import csv


def change_password(id):
    while True:
        new_password = input("enter your new password:")
        if new_password == input("enter your new password again:"):
            # خواندن کل فایل و اعمال تغییرات
            with open("databaseCSV.csv", "r") as file:
                reader_ = csv.DictReader(file)
                lines = list(reader_)  # خواندن تمام خطوط

            # ایجاد لیست برای فیلدها
            fieldnames = reader_.fieldnames

            # تغییر خط مورد نظر
            for line in lines:
                if line["AccountID"] == id:
                    line["Password"] = new_password  # بروزرسانی موجودی

            # بازنویسی کل فایل
            with open("databaseCSV.csv", "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # نوشتن سرستون‌ها
                writer.writerows(lines)  # نوشتن کل داده‌های به‌روزشده
                file.flush()
            print("Your password has been successfully changed.")
            break
        else:
            print("he passwords do not match. Please try again.")
    choice_ = input("Would you like to do anything else? Y/N")
    return choice_
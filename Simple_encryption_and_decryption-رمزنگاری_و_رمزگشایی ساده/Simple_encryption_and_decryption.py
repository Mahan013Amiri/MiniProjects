Encrypt = ""
Decrypt = ""
while True:
    print("Select\n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit")
    choice = input("your choice... ")
    if choice == "1":
        txt = input("TXT : ")
        for i in txt:
            Encrypt += chr(ord(i) * 3 + 6)
        print(Encrypt)
        continue
    if choice == "2":
        for i in Encrypt:
            Decrypt += chr((ord(i) - 6) // 3)
        print(Decrypt)
        break
    elif choice == "3":
        print("bye")
        break
    else:
        print("The entered number is incorrect!")

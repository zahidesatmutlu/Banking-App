from database import *
from customer_menu import *

while True:
    print("1- Giriş")
    print("2- Kayıt ol")
    print("3- Uygulamayı kapat")

    pref = input("Seçim: ")
    if pref == "1":
        identity = input("TC kimlik numarası: ")
        password = input("Şifre: ")
        search = search_customer(identity, password)
        if search == None:
            print("TC kimlik no veya şifre hatalı!")
            continue
        while True:
            customer_menu(identity)
            pref = input("Seçiminizi giriniz: ")
            if pref == "1":
                print("Bakiye: ", balance_inquiry(identity))
            if pref == "2":
                amount = input("Eklemek istediğiniz miktarı giriniz: ")
                add_balance(amount, identity)
                print("Bakiye güncellendi!")
            if pref == "3":
                amount = float(input("Çekmek istediğiniz miktarı giriniz: "))
                balance = balance_inquiry(identity)[0]
                if amount > balance:
                    print("Yeterli bakiye bulunmuyor!")
                else:
                    reduce_balance(amount, identity)
                    print("Bakiye güncellendi!")
            if pref == "4":
                receiver_person = input("Para göndermek istediğiniz kişinin TC numarasını giriniz: ")
                search = search_customer_for_sending(receiver_person)
                amount = float(input("Göndermek istediğiniz miktarı giriniz: "))
                balance = balance_inquiry(identity)[0]
                if amount > balance:
                    print("Yeterli bakiye bulunmuyor! En fazla {} TL gönderilebilir!".format(balance))
                else:
                    send_money(identity, receiver_person, amount)
                    print("Para gönderme işlemi başarılı!")
            if pref == "5":
                print("Çıkış yapıldı!")
                break

    if pref == "2":
        identity = input("TC kimlik numarası: ")
        password = input("Şifre: ")
        balance = input("Bakiye: ")
        search = search_customer(identity, password)
        if search != None:
            print("Bu TCye ait hesap zaten var!")
            continue
        insert(identity, password, balance)
        print("Kayıt işlemi başarılı!")
        continue
    if pref == "3":
        print("Uygulama sonlandırıldı!")
        break

import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

while True: 
    print ("-----------------------------")
    print("Selamat datang!")
    print()
    print("---Menu---")
    print("1. Daftar Email")
    print("2. Tambah Email")
    print("3. Mengirim Email")
    print("4. Keluar")
    print("------------------------------")
    menu = input("Piih Menu: ")
    print()

    if menu == '2':
        print("Masukkan Email Baru ")
        print ("-----------------------------")
        Email = input(str("Email:  "))
        with open('contact.txt', 'a') as f:
               f.append(Email)
               f.append('\n')
        print()
        print("Email berhasil ditambahkan!")

    elif menu == '3':
    #Login e-mail
        print("Silahkan Login Terlebih Dahulu ")
        gmail_user = input(str("Masukkan akun gmail: "))
        gmail_app_password = gmail_app_password = getpass.getpass("Masukkan Password:")

    #Sumber : https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['Subject'] = input("Masukkan Subjek E-mail: ")
        body = input("Masukkan Isi E-mail: ")

    #Masukkan lampiran
        filename = input("Masukkan nama File beserta formatnya: ")
        path = input("Masukkan Path File: ")
        attachment = open(path, "rb") 
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

    #read penerima
        with open('contact.txt', 'r') as f:
	        penerima = f.readlines()
       
    #Sumber: https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
    #bila tidak bisa
        for y in range(len(penerima)):
            receiver = f"{penerima[y]}"
            msg['To'] = receiver
            msg.attach(MIMEText(body, 'plain'))
           
            try:          
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_app_password)
                text = msg.as_string()
                server.sendmail(gmail_user, receiver, text)
                server.quit()

                print('Email sent!')
            except Exception as exception:
                print("Error: %s!\n\n" % exception)

    #daftar e-mail
    elif menu == '1':
        print("Daftar Email ")
        print ("-----------------------------")
        with open('contact.txt', 'r') as f:
            Daftar = f.read()
            print(Daftar)
            
    #keluar program
    elif menu == '4':
        print ("-----------------------------")
        print("Program berakhir, TERIMA KASIH!")
        break

    else : 
        print ("-----------------------------")
        print("Menu tidak tersedia")
#this is a simple login verfication, using a I/O file to save the information
                ##### made by herick lima #####
import json

f = open("login/usr.json", 'a')
f.close()


print("\n1 - Login\n\n")
print("2 - Registrar-me\n\n")
menu = input()

if menu == '2':
    #emailIn = input("Email:\n") #input a email
    #emailCpr = "asd"
    
    try:
        with open(file="login/usr.json", mode='r') as usr:   #open the file email.txt
            userInfo = json.load(usr)
            
        email = userInfo["email"]
        passwd = userInfo["password"]

        emailIn = input("Email: ")
        passwdIn = input("Password: ")

        emailCpr = "sad"

        for i in email:
            if i == emailIn:
                emailCpr = i
                print("Este email ja existe!")

        while emailIn == emailCpr:
                emailIn = input("Email: ")

        
    finally:
        usr.close()


    try:
        email.append(emailIn)
        passwd.append(passwdIn)
        index = 0
        with open(file="login/usr.json", mode='w') as usr:
            for i in userInfo["email"]:
                userInfo

            json.dumps(userInfo, usr)
    finally:
        usr.close()
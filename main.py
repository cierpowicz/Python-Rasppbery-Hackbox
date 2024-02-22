import os

# ostatnio prubowałem wysłać plik .txt na email 

settings = {
    'email_settings':{
        'sender':'',
        'reciver':'piotrekzrydek@gmail.com'
    },

    "user_settings":{
        'user_name':'maczo',
        'user_password':'dupa'
    }
}




print (settings['email_settings'].get('reciver'))


def print_all_MAC_addr():
    os.system('nmcli -f BSSID dev wifi')


# use `nmcli dev wifi list > .txt` command, and then send the file to email 
#
#

def print_wifis_info():

    command = 'nmcli dev wifi list'
    os.system(command)


def send_email():
    pass

def login_function():
    os.system('clear')
    login = ""
    password = ""

    while True:
        print("Hayy, welcome !!! Type your login and password:")
        login = input("login: ")
        password = input("password: ")

        if login == settings['user_settings'].get('user_name') and settings['user_settings'].get('user_password'):
            break

        else:
            os.system('clear')
            print ("Złu login lub hasło")
            pass



def main():

    os.system('clear')

    anser_1 = ""
    
    while True:

        # Lets login

        

        # here is menu of this program

        print (f"EMAIL reciver: ")
        print("Hit your option: \n (0) Exit \n (1) Print all MAC near routers (AP) \n (2) Scan network \n (3) Scan network and send email \n (4) Set setting (email_reciver, ip_to_scan)")
        anser_1 = input("-->")

    
        if anser_1=="1":
            os.system('clear')
            print_all_MAC_addr

        elif anser_1 == "0":
            os.system('clear')
            break

        elif anser_1=="2":
            os.system('clear')
            print_wifis_info()




        else:
            pass



login_function()
main()
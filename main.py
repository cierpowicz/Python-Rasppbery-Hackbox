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

#
# Simple return sectrion 
#


def return_my_ip_adress():
    ip_addres = os.system("hostname -I | awk '{print $1}")

    return ip_addres

def return_my_MAC_address():
    mac_address = os.system('cat /sys/class/net/*/address |head -1')

    return mac_address
#
# More advance sectrion 
#

def print_some_data():
    ip_addres = return_my_ip_adress()
    MAC_addres = return_my_MAC_address()

    print(f"IP: {ip_addres} \n MAC: {MAC_addres}")




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
        print("Hit your option: \n (0) Exit \n (1) Print network info (ip,MAC,mask)")
        anser_1 = input("-->")

    
        if anser_1=="1":
            os.system('clear')
            print_some_data()

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
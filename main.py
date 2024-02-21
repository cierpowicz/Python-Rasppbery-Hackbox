import os

# ostatnio prubowałem wysłać plik .txt na email 
# poszło średnio bo nie ma neta na kali linx lol 
#
#
#
#
#

EMAIL = ''


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



def main():

    os.system('clear')

    anser_1 = ""
    
    while True:

        print (f"EMAIL reciver: {EMAIL}")
        print("Hit your option: \n (1) Print all MAC near routers (AP) \n (2) Scan network \n (3) Scan network and send email")
        anser_1 = input("-->")

    
        if anser_1=="1":
            os.system('clear')
            print_all_MAC_addr

        elif anser_1=="2":
            os.system('clear')
            print_wifis_info()

        else:
            pass

main()
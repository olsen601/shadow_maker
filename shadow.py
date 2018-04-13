import pcrypt as crypt
import random


# Common password list
common_password = [ 'password', '123456', '12345678', '1234', 'qwerty',
                    '12345', 'dragon', 'baseball', 'football', 'letmein',
                    'monkey', 'abc123', 'mustang', 'michael', 'shadow',
                    'master', 'jennifer', '111111', '2000', 'jordan',
                    'superman', 'harley', '1234567', 'hunter', 'trustno1',
                    'ranger', 'buster', 'thomas', 'tigger', 'robert',
                    'soccer', 'sunshine', 'test', 'killer', 'hockey',
                    'george', 'charlie', 'andrew', 'michelle', 'love' ]


def rpg():
    random_password = ''.join([random.SystemRandom().choice("abcdefghijklmnopqrstuvwxyz123456789") for l in range(8)])

    return random_password


def rpg_list():
    random_password_list = []
    random_password_list.extend([rpg() for r in range(40)])

    return random_password_list

def mkfile(name):
    new_file = open(name+'.txt', 'w').close()
    file = open(name+'.txt', 'a')
    return file


def encrypt_list(pwd_list, file):

    for i in range(40):
        salt = crypt.mksalt(crypt.METHOD_SHA512)
        hash = crypt.crypt(pwd_list[i], salt)
        file.write('user'+str(i+1)+":"+str(hash)+":"+str((16840+i))+":0:99999:7:::"+"\n")


def menu():

    print("""
    MENU- generate sudo shadow text file
    1) Common password base
    2) Random password base
    q) Quit
    """)

    choice = input("Menu Choice: ")

    return choice

def handle_choice(choice):

    if choice == "1":

        file = mkfile('common_shadow')
        encrypt_list(common_password, file)

    elif choice == "2":

        file = mkfile('random_shadow')
        plain_file = mkfile('random_passwords')
        random_list = rpg_list()
        for i in range(40):
            plain_file.write("Password "+str(i+1)+": "+random_list[i]+"\n")
        encrypt_list(random_list, file)

    elif choice == "q":
        main.choice = 'q'

    else:
        print("Please enter a valid menu option.")


def main():

    quit = 'q'
    choice = None


    while choice != quit:
        choice = menu()
        handle_choice(choice)



if __name__ == '__main__':
    main()

def login_system():
    preference = input('''Press 1 to login
Press 2 to create account
Press 0 to exit

Your preference - ''')

    def status(preference):
        if int(preference) == 1:
            old_user()
        elif int(preference) == 2:
            new_user()
        elif int(preference) == 0:
            print('Thanks for using!')
        elif int(preference) == 3:
            login_system()
        else:
            print('I did not get that!!!')

    def old_user():
        usrn = input('Enter username: ')
        passw = input('Enter password: ')
        with open("Login.txt", "r") as file:
            if (usrn + "," + passw + "\n") in file.readlines():
                print('LOGIN SUCCESSFUL')
            else:
                print('Either username or password is wrong. Try again')
                old_user()
        preference_1 = input('''Press 0 to exit
Press 3 to display menu''')
        status(preference_1)
        

    def new_user():
        username = input('Enter the username you want: ')
        with open("username.txt","r") as file:
            for line in file:
                while username in line:
                    print('Username already exists! Try with a new one')
                    username = input('Enter the username you want: ')
        password = input('Enter the password that you want: ')
        re_password = input('Please confirm your password: ')
        while re_password != password:
            print("Passwords do not match")
            re_password = input('Please confirm your password: ')
        user_file = open("Login.txt","a")
        user_file.write (username)
        user_file.write (",")
        user_file.write (password)
        user_file.write("\n")
        user_file.close()

        use_file = open("username.txt","a")
        use_file.write (username)
        use_file.write("\n")
        use_file.close()
        print('Account created!')
        preference_2 = input('''Press 0 to exit
Press 3 to display menu
        
        Your prefernce - ''')
        status(preference_2)

    status(preference)

login_system()

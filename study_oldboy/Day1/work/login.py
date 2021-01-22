#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import sys,os,getpass

user_info_file = 'user_info'
user_lock_file = 'user_lock'

def register():    
    print("__________register__________")

    if not os.path.isfile(user_info_file):
        file = open(user_info_file,'w')
        file.close()

    while True:
        name = input("Please input your name:")
        if name == '':
            print("username can not be null,Please input your name again!")
        else:
            file = open(user_info_file, 'r')
            user_info_list = file.readlines()
            file.close()
            flag = 0
            for line in user_info_list:
                info = line.split()
                if name == info[0]:
                    flag = 1
                    break
            if flag == 1:
                print("Username is existed, Please input a new username!")
            else:
                break
    while True:
        passwd1 = input("Please input your passwd:")
        passwd2 = input("Please confirm your passwd:")
        if passwd1 != passwd2:
            print("The entered password is inconsistent, Please input your passwd again!")
        else:
            passwd = passwd1
            break

    file = open(user_info_file, 'a')
    info = '\n' + name + ' ' + passwd + ' ' + '0'
    file.write(info)
    file.close()
    print("User registration is successful!")


def login():
    print("\n__________logining__________")

    while True:
        name = input("name: ")
        if name == '':
            print("username can not be null,Please input your name again!")
        else:
            break
    passwd = input("password: ")

    file_lock = open(user_lock_file, 'r')
    user_lock = file_lock.readlines()
    lock_flag = 0
    for line_user_lock in user_lock:
        if name == line_user_lock:
            lock_flag = 1
            print("The user name is locked, Please try other user name!")
            break

    if lock_flag == 1:
        while True:
            name = input("name: ")
            if name == '':
                print("username can not be null,Please input your name again!")
            else:
                break
        passwd = input("password: ")
    else:
        file = open(user_info_file, 'r')
        user_info = file.readlines()
        count = 0
        flag = 0
        for line_str in user_info:
            line_list = line_str.split()
            line_user = line_list[0]
            line_passwd = line_list[1]
            if name == line_user:
                passwd_true = line_passwd
                flag = 1
                break

        if flag == 1:
                if passwd == passwd_true:
                    print("Welcom to our system......")
                    while True:
                        status = input("Input [Enter] to exit.")
                        if status == '':
                            sys.exit("Thank you for your visit, Goodbye!")
                else:
                    while count < 3:
                        count = count + 1

                        if count == 3:
                            print("you have tried 3 times password fault, user will be locked!")
                            file = open(user_lock_file, 'a')
                            file.write('\n' + name)
                            break
                        else:
                            print(
                                "username password is incorrect, you have tried {count} time,3 time false user will be locked!".format(
                                    count=count))
                        is_exit = input("you want to try again! [y/n]")
                        if is_exit == 'y' or is_exit == 'Y':
                            passwd = input("password: ")
                        else:
                            sys.exit("Thank you for your visit, Goodbye!")
                        if passwd == passwd_true:
                            print("Welcom to our system......")
                            while True:
                                status = input("Input [Enter] to exit.")
                                if status == '':
                                    sys.exit("Thank you for your visit, Goodbye!")

        else:
            print("username is not exited, please to registry your user!")

if __name__ == "__main__":
    while True:
        print('''
            Welcome to our system.as follows:
            1.Register your user.
            2.login your user.
            3.exit.
        ''')

        choice = input("Please input your choice:")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            sys.exit("Thank you for your visit, Goodbye!")
        else:
            print("Please input a right choice!")
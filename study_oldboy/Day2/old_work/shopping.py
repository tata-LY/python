#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

goods_list = [
    ('Apple Watch', 4000),
    ('Iphone 8', 5998),
    ('Bike', 1200),
    ('Coffe', 35),
    ('book', 78),
    ('NotePad', 3400),
]

shopping_list = []
while True:
    balance = input("Your balance: ")
    if balance.isdigit():
        balance = int(balance)
        break
    else:
        print("Invalid option, Please input your balance again!")
# balance = 12000
while True:
    '''
    for index in range(0,len(goods_list)):
        print("{index}. [{goods}] : {price}".format(index=index, goods=goods_list[index][0], price=goods_list[index][1]))
    '''
    for index,item in enumerate(goods_list):
        print("{index}. {item}".format(index=index, item=item))
    print("Enter [q] to exit.")
    your_choice = input("Your choice: ")
    if your_choice.isdigit():
        your_choice = int(your_choice)
        if your_choice >= 0 and your_choice < len(goods_list):
            goods = goods_list[your_choice][0]
            goods_price = goods_list[your_choice][1]
            if balance >= goods_price:
#                shopping_list.append([goods, goods_price])
                shopping_list.append(goods_list[your_choice])
                balance = balance - goods_price
                print("[{goods}] have added your shopping cart, now your balance: {balance}".format(goods=goods, balance=balance))
            else:
                print("Your balance is insufficient!")
                print("\033[31;1mYour balance is {balance}, not enough to buy {goods}.\033[1m".format(balance=balance, goods=goods))
        else:
            print("Your choice good is not exited, Please choose again!")
    elif your_choice == 'q':
        print("Your shopping cart list: ")
        for item in shopping_list:
            print("{goods} : {price}".format(goods=item[0], price=item[1]))
        print("your balance: {balance}".format(balance=balance))
        exit()
    else:
        print("Invalid option, Please choose again!")
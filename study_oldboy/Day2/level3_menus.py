#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

data = {
    "湖南": {
      "长沙": {
            "长沙大学": ["星沙", "二本"],
            "商学院": ["河西", "二本"]
        },
        "湘潭": {
            "湘潭大学": ["清哥哥", "槟榔", "一本"],
            "工程学院": ["博子哥","二本" ]
        },
        "株洲": {
            "工业大学": ["河西", "湘哥哥", "二本"],
            "工业学院": ["河东", "三本"]
        },
    },
    "湖北": {
        "武汉": {
            "武汉大学": ["热干面", "一本"],
            "长江大学": ["长江", "二本"]
        },
        "荆州": {
            "荆州大学": ["关羽失荆州", "二本"],
        },
    },
    "广东": {
        "深圳": {
            "深圳大学": ["南山区", "一本"],
        },
        "广州": {
            "中山大学": ["一本"],
        },
    },
}

while True:
    key1 = []
    for k,v in data.items():
        key1.append(k)
        print(key1.index(k),k)
    choice = input("第一层目录：选择[0-{length}]进入：".format(length=len(key1)-1))
    if choice.isdigit():
        choice = int(choice)
        now_data1 = data[key1[choice]]
        if choice >= 0 and choice < len(key1):
            while True:
                key2 = []
                for k, v in now_data1.items():
                    key2.append(k)
                    print(key2.index(k), k)
                choice2 = input("第二层目录：选择[0-{length}]进入：".format(length=len(key2) - 1))
                if choice2.isdigit():
                    choice2 = int(choice2)
                    now_data2 = now_data1[key2[choice2]]
                    if choice2 >= 0 and choice2 < len(key2):
                        while True:
                            key3 = []
                            for k,v in now_data2.items():
                                key3.append(k)
                                print(key3.index(k),k)
                            choice3 = input("第三层目录：选择[0-{length}]进入：".format(length=len(key3)-1))
                            if choice3.isdigit():
                                choice3 = int(choice3)
                                now_data3 = now_data2[key3[choice3]]
                                if choice3 >=0 and choice3 < len(key3):
                                    while True:
                                        print(key3[choice3], now_data3)
                                        choice4 = input("最后一层目录了，Enter[b]返回: ")
                                        if choice4 == "b":
                                            break
                                elif choice3 == "b":
                                    break
                            elif choice3 == "b":
                                break
                elif choice2 == "b":
                    break
    elif choice == "b":
        exit("Goodbye!")



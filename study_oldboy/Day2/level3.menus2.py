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

data_list = [data]  # 用list来存储当前字典深度的所有字典list
choice_value = ''

def print_info(list, choice_value ):
    depth = len(list)
    if depth < 4:
        now_data = data_list[depth-1]
        key = []
        for k, v in  now_data.items():
            key.append(k)
            print(key.index(k), k)
        choice = input("第{depth}层目录：选择[0-{length}]进入：".format(depth=depth,length=len(key)-1))
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(key):
                data_list.append(now_data[key[choice]])
                return data_list, key[choice]
        elif choice == "b":
            if depth == 1:
                exit("Goodbye!")
            else:
                del data_list[-1]
                return data_list, choice_value
        elif choice == "q":
            exit("Goodbye!")
        else:
            return data_list
    else:
        print(choice_value, data_list[-1])
        choice = input("最后一层目录了，Enter[b]返回: ")
        if choice == "b":
            del data_list[-1]
            return data_list, choice_value
        else:
            return data_list, choice_value
while True:
    data_list, choice_value  = print_info(data_list, choice_value)
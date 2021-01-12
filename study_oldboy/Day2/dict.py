#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

student = {
    'stu01' : 'Liu Yang',
    'stu02' : 'Zhang Juan Juan',
    'stu03' : 'Liu Yi Yi'
}
print(student)
print(student['stu01'])

student['stu01'] = '刘洋'
print(student)

student['stu04'] = 'Liu Zhang Yi Yi'
print(student)

del student['stu04']
print(student)

student.pop('stu03')
print(student)

student.popitem()  # 随机删除
print(student)

student1 = {'stu01': '刘洋', 'stu02': 'Zhang Juan Juan', 'stu03': 'Liu Yi Yi', 'stu04': 'Liu Zhang Yi Yi'}

print(student1.get('stu09'))  # 这样取值 不存在的就不会报错

print('stu03' in student1)


av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] = "可以在国内做镜像"

print(av_catalog)
print(av_catalog.keys())
print(av_catalog.values())


av_catalog.setdefault('台湾', {'www.taiw.com': [1,2]})  # 不存在就插入
print(av_catalog)
av_catalog.setdefault('大陆', {'www.taiw.com': [1,2]})   # 存在了就不会修改
print(av_catalog)


student1 = {'stu01': '刘洋', 'stu02': 'Zhang Juan Juan', 'stu03': 'Liu Yi Yi', 'stu04': 'Liu Zhang Yi Yi'}
student2 = {
    'stu01': 'Liu Yang',
    'a': 'A',
    'b': 'B'
}

student1.update(student2)
print(student1)

print(student1.items())
for index,item in student1.items():
    print(index, item)

student3 = dict.fromkeys([1,2,3],["A","B","C"])    # 如果修改的话，第一层不会修改，深层会同时修改。
print(student3)

student3[1][0] = 'a'
print(student3)


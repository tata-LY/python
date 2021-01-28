#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 16:05
# @Author  : liuyang
# @File    : 11.3_module_xml.py
# @Software: PyCharm

# 自己创建xml文档

import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
name.text = "LiuYang"
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
age.text = '29'
sex = ET.SubElement(personinfo, "sex")
sex.text = "M"

personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "ZhangJuan"
age = ET.SubElement(personinfo2, "age")
age.text = '28'
sex = ET.SubElement(personinfo2, "sex")
sex.text = "W"

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("11_xml2.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式

#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by LiuYang

# 自己创建xml文档

import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
name.text = "LiuYang"
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
age.text = '26'
sex = ET.SubElement(personinfo, "sex")
sex.text = "M"

personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "ZhangJuan"
age = ET.SubElement(personinfo2, "age")
age.text = '25'
sex = ET.SubElement(personinfo2, "sex")
sex.text = "W"

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("xml2.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式

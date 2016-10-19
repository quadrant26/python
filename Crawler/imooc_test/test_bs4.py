'''
'''

from bs4 import BeautifulSoup
import re
'''
1. 创建 beautifulsoup 对象
2. 搜索节点 
    find_all
    find
3. 访问节点 ，名称， 属性

soup = BeautifulSoup(
    html_doc,                    # HTML 文档字符串
    'html.parse'                 # HTML 解析器
    from_encoding = 'utf-8'      # HTML 文档的编码
)

find_all(name, attrs, string)
    find_all('a')
    find_all('a', href='/view/123.html')
    find_all('a', href=re.compie(r'/view/\d+\.html'))
    find_all('a', class_=' abc', string='python')
find()
'''
str_html = """
    <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="format-detection" content="telephone=no,email=no" />
<meta name="viewport" content="width=device-width, initial-scale=1.0,user-scalable=no,minimum-scale=1.0,maximum-scale=1.0" />
<link rel="icon" href="images/favicon.ico" type="image/x-icon" />
<title>菠菜夺宝</title>
<link rel="stylesheet" href="css/db.main.css">
</head>
<body class="bgbodyf2f0">
<div class="page">
    <!-- head -->
    <div class="bheades borderbox">
        <a href="javascript:history.back()" class="goback">回退</a>
        <h2>我的地址</h2>
        <a href="addressadd.html" class="addtexts">添加地址</a>
    </div>
    <!-- head end -->
    <div class="m_hideing"></div>
    <div class="content">
        <div class="address">
            <section class="">
                <a href="javascript">
                    <div class="address"><strong>hehhehe</strong><span>198*****324</span></div>
                    <div class="hasaddress"><span>[默认]</span>泸沽湖，位于四川省盐源县与云南省宁蒗县交界处，为川滇共辖</div>
"""

soup = BeautifulSoup(str_html, 'html.parser', from_encoding="utf-8")
print("获取所有的链接")

links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())

print("获取 javascript 的链接")
link_node = soup.find('a', href="javascript")
print(link_node.name, link_node['href'], link_node.get_text())

print("正则匹配")
link_node = soup.find('a', href=re.compile(r'jav'))
print(link_node.name, link_node['href'], link_node.get_text())


print("获取p段落文字")
p_node = soup.find('p', class_="title")
print(p_node.name, p_node.get_text())



















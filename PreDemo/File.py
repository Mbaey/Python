#coding:utf-8
#encoding='UTF-8' 编码方式
f = open(r"data/temp.txt", "r+", encoding='UTF-8')
s = f.read()
print(f.name)
print(s)

#encode 编码 -> byte
#decode 解码 -> str
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
# write content to a file
with open("./data2.txt", "w", encoding="utf-8") as file:
    for line in range(4):
        file.write(str(line))

# support append
with open("./data3.txt", "a", encoding="utf-8") as file:
    for line in range(4):
        file.write(str(line))
    print(file.readlines())

"""
模式	含义	备注
'r'	只读	文件必须存在
'w'	只写	文件存在就清空，不存在就创建
'a'	追加写	文件存在就加在后面，不存在就创建
'x'	独占写	文件存在就报错，不存在才创建
'b'	二进制模式	常和其他模式一起用，比如 'rb'、'wb'
't'	文本模式	默认模式，读写字符串
'+'	读写模式	读和写都能做，比如 'r+'、'w+'
"""
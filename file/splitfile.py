f = open('record.txt')

boy = []
girl = []

str = "小甲鱼"
print(str[:3] == "小甲鱼")

for each_line in f:
    if each_line[:6] != "======":
        if each_line[:3] == "小甲鱼":
            boy.append(each_line)
        elif each_line[:3] == "小客服":
            girl.append(each_line)

fboy = open("boysay.txt", 'w')
fgirl = open("girlsay.txt", "w")

fboy.writelines(boy)
fgirl.writelines(girl)

fboy.close();
fgirl.close()

f.close()
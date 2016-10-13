# __doc__

def sum2(*params, base=3):
    result = 0;
    for i in params:
        if type(i) == int or type(i) == float:
            result += i
        else:
            continue

    if base == 3:
        return result*base
    elif base == 5:
        return result

print(sum2(1,2,3,4,5,6, base=3))
print(sum2(1,'a',3,4,5,6, base=3))
print(sum2(1,2,3,4,5,6, base=5))


def shuixianhua():
    for i in range(100, 1000):
        sum = 0
        temp = i

        while temp:
            sum = sum + (temp%10) ** 3
            temp //= 10

        if sum == i:
            print(i)

shuixianhua()

str1 = "You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted."
substr = "im"
def findstr(s, substr):
    result = 0
    length = len(s);
    ido = 0
    
    while True:
        idx = s.find(substr, ido, length)
        if idx != -1:
            result += 1
            ido = idx+1
        else:
            break
            
    print("子字符串在目标字符串中共出现",result,"次")

findstr(str1, substr)

def findstr2(desstr, substr):
    count = 0
    length = len(desstr)
    if substr not in desstr:
        print('在目标字符串没有找到子字符串！')
    else:
        for each1 in range(length-1):
            if desstr[each1] == substr[0]:
                if desstr[each1+1] == substr[1]:
                    count += 1
    print("子字符串在目标字符串共出现了"+count+"次")
    
    

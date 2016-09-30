# 转成二进制

def mbin(n):
    result = ''
    
    if n :
        result = mbin(n//2)
        return result + str(n%2)
    else:
        return result

print(mbin(3))


list1 = []
def get_digits(n):
    
    if n > 0:
        list1.insert(0, n%10)
        get_digits(n//10)

get_digits(12345)
print(list1);

def is_finlian(n, start, end):
    if start > end:
        return 1
    else:
        return is_finlian(n, start+1, end-1) if n[start] == n[end] else 0

str1 = "上海自来水来自海上"
length = len(str1)-1

if is_finlian(str1, 0, length):
    print('\"%s\" 是回文联！' % str1)
else:
    print('\"%s\" 不是回文联！' % str1)



def age(n):
        if n == 1:
                return 10
        else:
                return age(n-1) + 2

print( age(5) )

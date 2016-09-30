name = ['F', 'i', 'h', 'C']
name.insert(2, 's')
print(name)


# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
# one
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
print(member)
member.append(88)
member.insert(1, 88)
member.insert(3, 90)
member.insert(5, 85)
member.insert(7, 90)
print(member)

for k in member:
    print(k)

count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2

for each in range(len(member)):
    if each % 2 == 0:
        print(member[each])

old = [1, 2, 3, 4, 5]
new = old
old = [6]
print(new)
print(old)



list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0] = "小鱿鱼"
print(list1)

list2 = [4,2,6,7,1,9,0]
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list3 = list2.copy()
print(list3)

list4 = list3
list4 = [6]
print(list3) 

list3.clear()
print(list3)

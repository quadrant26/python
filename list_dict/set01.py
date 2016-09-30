# 列表
# 插入元素
# append(元素)
# extend([数组])
# insert(位置, 元素)

member = ['jiayu', 'buding', 'heiye']
print(member)

member.append("wawa")
print(member)

member.extend(['taohua', 'xinghua'])
print(member)

member.insert(1, '牡丹')
print(member)

print(member[1])

temp = member[0]
member[0] = member[1]
print(member)
member[1] = temp
print(member)

# 删除元素
# remove(元素)
# del()
# pop(位置) 位置 不是必须的
member.remove('heiye')
print(member)

del member[1]

print(member.pop())
name = member.pop()

# slice
# slice[num:num]
# slice[:]
# slice[:3]
print( member[1:3])



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
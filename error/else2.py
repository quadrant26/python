
try:
    int('哎不错')
except ValueError as reason:
    print('出错了：' + str(reason))
    
else:
    print('没有任何异常')

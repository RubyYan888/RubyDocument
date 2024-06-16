def 字符频率(字符串):
    频率 = {}
    for 字符 in 字符串:
        if 字符 in 频率:
            频率[字符] += 1
        else:
            频率[字符] = 1
    return 频率

print(字符频率("hello world"))

def 是否为素数(数字):
    if 数字 <= 1:
        return False
    for i in range(2, int(数字 ** 0.5) + 1):
        if 数字 % i == 0:
            return False
    return True

print(是否为素数(29))

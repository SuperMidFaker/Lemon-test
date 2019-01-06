a = input('请输入重量(g)：')


def trance(weight):
    a = int(weight)/1000
    return str(a)+'kg'


print(trance(a))

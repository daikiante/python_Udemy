def get_total(a,b,c):
    return a + b + c

def get_average(a,b,c):
    return (a + b + c) / 3

a = int(input('a :'))
b = int(input('b :'))
c = int(input('c :'))

print('合計：',get_total(a,b,c))
print('平均：',get_average(a,b,c))
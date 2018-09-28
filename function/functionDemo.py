def add(*args):
    result = 0
    for arg in args:
        result = result + arg
    return result
print(add(1, 2, 3, 4))

def print_info(name,age):
    print('name: %s' % name)
    print("age: %d" %age)
print_info( name='easin', age=27)

def info(*args,**kwargs):
    print(args)
    print(kwargs)
    for i in kwargs:
        print('%s : %s'%(i,kwargs[i]))
info('easin','age',hobby='girl',score=90)


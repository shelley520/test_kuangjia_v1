import inspect


def a():
    print(inspect.stack()[1].function)
    print('**************')

def b():
    a()

b()
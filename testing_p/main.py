
def text_decor(wfunc):
    def wrap():
        print('Hello')
        wfunc()
        print('Goodbye')
    return wrap

@text_decor
def simple_func():
    print('I just simple python func')

simple_func()


@text_decor
def multiply(num1, num2):
    print(num1 * num2)

multiply(3, 5)

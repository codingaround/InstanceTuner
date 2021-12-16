from instanceTuner import setFunction
from setInstance import *


def printException(fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
        print('there is no error')
    except Exception as e:
        print(e)


@setFunction
def test():
    print('first test')


@setFunction
def test(x: str):
    print('second test', x)


@setFunction
def test(x: int):
    print('third test', x)


test()
test('2nd')
test(3)
printException(test, 4.0)

print('\n'*2)


Number = InstanceOperator('or', int, float)


class Test2:
    @setFunction
    def __init__(self, a: Number, b: Number) -> None:
        super().__init__()
        self.a = a
        self.b = b

    @setFunction
    def __init__(self, a: Number) -> None:
        super().__init__()
        self.a = a
        self.b = a

    def get(self):
        return self.a * self.b


print('Test2')

t = Test2(4)
print(t.get())

t = Test2(4, 5)
print(t.get())

printException(Test2)

print('\n'*2)


class Test3:
    @setFunction
    def __init__(self, a: Number, b: Number) -> None:
        super().__init__()
        self.a = a
        self.b = b

    @setFunction
    def __init__(self, a: Number) -> None:
        super().__init__()
        self.a = a
        self.b = a

    def get(self):
        return self.a + self.b


print('Test3')

t = Test3(4)
print(t.get())

t = Test3(4, 5)
print(t.get())

printException(Test3)

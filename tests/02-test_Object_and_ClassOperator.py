# from instanceTuner.operator import *


def hasInstanceCheck(__instance):
    try:
        isinstance(object, __instance)
        return True
    except Exception as e:
        return False


class ClassOperator:

    """
    We wanna say if an object is equal 
    to a class by using isinstance method.

    its __init__ takes one arguments :
    cls: must be a class

    for example :
    """

    def __init__(self, cls) -> None:
        """
        __init__ takes one arguments :
        cls: must be a class
        """

        assert '__init__' in dir(cls), 'cls must be a class'
        self.cls = cls

    def __repr__(self) -> str:
        return f'{self.cls}'

    def __instancecheck__(self, __instance) -> bool:
        return __instance is self.cls

    @staticmethod
    def setClasses(classes):
        return [ClassOperator(cls) for cls in classes]


class Operator:

    """
    This class is just a base class for
    ClassOperator and InstanceOperator
    """

    def __init__(self, operator: str) -> None:
        """
        operator: an string which must be 'or' or 'not'
        """

        assert operator in ('or', 'not'), 'use "or" "not"'
        self.operator = operator


class InstanceOperator(Operator):

    """
    A class to do isinstance job, 
    an alternative which is reusable by its instance

    it tells you if some object is instance of set of instances
    or in other usage, if its not.

    its __init__ takes at least two arguments :
    operator: an string which must be 'or' or 'not'
    *instances: must use at least one Variable Positional for it and
    these Variables must be a class or instance which have __instancecheck__

    operator will use for determine if instances
    are what we want or what we avoid

    for using it you should use: 
    isinstance(someInstance, instanceOfInstanceOperator)

    it tells you if someInstance is instance of instanceOfInstanceOperator
    or not, by returning True if it's actually an instance and operator is 'or',
    or ruturns False if it's not actually an instance and operator is 'or',
    or ruturns True if it's not actually an instance and operator is 'not',
    or ruturns False if it's actually an instance and operator is 'not'.
    """

    def __init__(self, operator: str, *instances) -> None:
        """
        __init__ takes at least two arguments :
        operator: an string which must be 'or' or 'not'
        *instances: must use at least one Variable Positional for it and
        these Variables must be a class or instance which have __instancecheck__

        operator will use for determine if instances
        are what we want or what we avoid
        """

        super().__init__(operator)

        assert len(
            instances) > 0, 'this class operat on instances, you must use instances too'

        for i in instances:
            assert hasInstanceCheck(i)

        self.instances = instances

    def __repr__(self) -> str:
        result = f' {self.operator} '.join([str(i) for i in self.instances])
        return result if self.operator == 'or' else ' not ' + result

    def __instancecheck__(self, __instance) -> bool:
        """
        this method returns True if __instance 
        is actually an instance of instances and operator is 'or',
        or ruturns False if it's not actually an instance and operator is 'or',
        or ruturns True if it's not actually an instance and operator is 'not',
        or ruturns False if it's actually an instance and operator is 'not'.
        """

        if self.operator == 'or':
            # 'or'
            for i in self.instances:
                if isinstance(__instance, i):
                    return True
            return False

        # 'not'
        for i in self.instances:
            if isinstance(__instance, i):
                return False
        return True


class ObjectOperator(InstanceOperator):

    """
    A class based on InstanceOperator for completing it

    if we use this class instead of InstanceOperator,
    when __instancecheck__ is called and self.operator
    is 'or', we are saying if an object is instance of
    a class or the class itself.
    when self.operator is 'not', we are saying if 
    an object is not instance of a class and 
    not the class itself.

    for example:
    """

    def __init__(self, operator: str, *instances) -> None:
        objects = instances + tuple(ClassOperator.setClasses(instances))
        super().__init__(operator, *objects)


class Test:

    pass


iop = InstanceOperator('or', int, Test)

print(isinstance(int, iop))
print(isinstance(1, iop))
print(isinstance(Test, iop))
print(isinstance(Test(), iop))

print('\n'*2)


iop = InstanceOperator('not', int, Test)

print(isinstance(int, iop))
print(isinstance(1, iop))
print(isinstance(Test, iop))
print(isinstance(Test(), iop))

print('\n'*2)


iop = InstanceOperator(
    'or', Test, ClassOperator(Test))

print(isinstance(Test, iop))
print(isinstance(Test(), iop))

print('\n'*2)


iop = InstanceOperator(
    'not', Test, ClassOperator(Test))

print(isinstance(Test, iop))
print(isinstance(Test(), iop))

print('\n'*2)


oop = ObjectOperator('or', Test)

print(isinstance(Test, oop))
print(isinstance(Test(), oop))

print('\n'*2)


oop = ObjectOperator('not', Test)

print(isinstance(Test, oop))
print(isinstance(Test(), oop))

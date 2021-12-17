#from instanceTuner.instanceTuner import ArgsCheck, setFunction
# from instanceTuner.setInstance import InstanceOperator, MapInstances, ClassOperator


from typing import Any


def hasInstanceCheck(__instance):
    try:
        isinstance(object, __instance)
        return True
    except Exception as e:
        return False


class Operator:
    def __init__(self, operator: str) -> None:
        assert operator in ('or', 'not'), 'use "or" "not"'
        self.operator = operator


class ClassOperator(Operator):  # write doc
    def __init__(self, operator: str, cls) -> None:
        super().__init__(operator)
        assert '__init__' in dir(cls), 'cls must be a class'
        self.cls = cls

    def __instancecheck__(self, __instance: Any) -> bool:
        return __instance is self.cls


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
        its __init__ takes at least two arguments :
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

    def __instancecheck__(self, __instance: Any) -> bool:
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


class Test:

    pass


iop = InstanceOperator(
    'not', Test, ClassOperator('or', Test))

print(isinstance(Test, iop))
print(isinstance(Test(), iop))


iop = InstanceOperator(
    'or', Test, ClassOperator('or', Test))

print(isinstance(Test, iop))
print(isinstance(Test(), iop))

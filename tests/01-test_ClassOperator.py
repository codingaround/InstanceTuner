from instanceTuner.operator import InstanceOperator, ClassOperator


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

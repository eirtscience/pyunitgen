
from .templates import Templates


class PyUnitReport(list):

    def __init__(self):
        pass

    def add(self, value):
        self.append(value)

    def __str__(self):
        unitTestsStr = '\n\n'.join(
            unitTest for unitTest in self if unitTest != '')

        return Templates.unitTestBase % unitTestsStr

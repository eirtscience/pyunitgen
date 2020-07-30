
from .templates import Templates


class PyUnitReport(list):

    def __init__(self):
        pass

    def add(self, value):
        self.append(value)

    def getReport(self):
        if len(self) > 0:
            unitTestsStr = '\n\n'.join(
                unitTest for unitTest in self if unitTest != '')
            return Templates.unitTestBase % unitTestsStr
        return None


class PyUnitReportValidation(PyUnitReport):
    pass

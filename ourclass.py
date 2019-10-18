class Record(object):
    def __init__(self, name, initialization, usability):
        self.name = name
        self.initialization = initialization
        self.usability = usability


class RecordOperators(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class FunctionRecord(object):
    def __init__(self,name,operators,operands):
        self.name = name
        self.operators = operators
        self.operands = operands
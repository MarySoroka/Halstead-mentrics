class Record(object):
    def __init__(self, name, initialization, usability):
        self.name = name
        self.initialization = initialization
        self.usability = usability


class RecordOperators(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
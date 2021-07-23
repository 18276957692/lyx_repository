class Person(object):
    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender

    def __str__(self):
        return "[%s,%s,%s]" % (self.id, self.name, self.gender)

    def __repr__(self):
        return "[%s,%s,%s]" % (self.id, self.name, self.gender)

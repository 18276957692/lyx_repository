# -*- coding: utf-8 -*
class JosephusCircle(list):
    def __init__(self, people_list, step, start):
        assert step > 0
        self.people_list = people_list
        self.step = step
        self.start = start
        self.josephus_list = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.people_list) > 0:
            self.start = (self.start + self.step - 1) % len(self.people_list)
            self.josephus_list.append(self.people_list.pop(self.start))
            return self.josephus_list[-1]
        else:
            raise StopIteration

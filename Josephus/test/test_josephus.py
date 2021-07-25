# -*- coding: utf-8 -*
import unittest

from src.ui.usecase.josephus_iter import JosephusCircle

STEP = 3
START = 0


class TestJosephusCircle(unittest.TestCase):
    def test(self):
        josephus_list = []
        people_list = [1, 2, 3, 4, 5, 6, 7, 8]
        [
            josephus_list.append(person)
            for person in JosephusCircle(people_list, STEP, START)
        ]
        self.assertEqual([3, 6, 1, 5, 2, 8, 4, 7], josephus_list)

import unittest
import sys
sys.path.append("F:\\sumer\\josephus\\src\\ui\\usecase\\entity\\person.py")
from person import Person


class TestPerson(unittest.TestCase):
    def test(self):
        self.assertEqual(
            ("2021001,Alice,women"), Person("2021001", "Alice", "women").__str__()
        )

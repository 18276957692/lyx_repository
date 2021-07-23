import zipfile
import csv

from .entity.reader import Reader
from .entity.person import Person

CSV_END = ".csv"


class CsvReader(Reader):
    def read(self):
        assert self.filepath.endswith(CSV_END)

        with open(self.filepath, "r", encoding="utf-8") as file:
            person_list = []
            csv_file = csv.reader(file)
            next(csv_file)

            for row in csv_file:
                id, name, gender = row
                person_list.append(Person(id, name, gender))
            return person_list

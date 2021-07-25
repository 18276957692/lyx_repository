# -*- coding: utf-8 -*
import xlrd

from .entity.person import Person
from .reader import Reader

EXCEL_END = ".xlsx"


class ExcelReader(Reader):
    def __init__(self, filepath, sheet_name):
        self.filepath = filepath
        self.sheet_name = sheet_name

    def read(self):
        assert self.filepath.endswith(EXCEL_END)

        person_list = []
        excel_file = xlrd.open_workbook(self.filepath, "r")
        sheet = excel_file.sheet_by_name(self.sheet_name)

        for row in range(1, sheet.nrows):
            id, name, gender = sheet.row_values(row)
            person_list.append(Person(id, name, gender))

        return person_list

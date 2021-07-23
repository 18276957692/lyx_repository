# -*- coding: utf-8 -*
import zipfile

from .entity.reader import Reader
from .csv_reader import CsvReader
from .excel_reader import ExcelReader

CSV_END = ".csv"
EXCEL_END = ".xlsx"
SHEET_NAME = "Sheet1"


class ZipReader(Reader):
    def __init__(self, filepath, inter_filename, sheet_name=""):
        self.filepath = filepath
        self.inter_filename = inter_filename
        self.sheet_name = sheet_name

    def read(self):
        assert self.inter_filename.endswith(CSV_END) or self.inter_filename.endswith(
            EXCEL_END
        )

        zip_file = zipfile.ZipFile(self.filepath,'r')
        read_file = zip_file.extract(self.inter_filename)

        if self.inter_filename.endswith(CSV_END):
            person_list = CsvReader(read_file).read()
            return person_list
        else:
            person_list = ExcelReader(read_file, SHEET_NAME).read()
            return person_list

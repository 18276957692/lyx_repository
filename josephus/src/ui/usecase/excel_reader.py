import xlrd as xd

from .entity.person import Person
from .entity.reader import Reader


CSV_FILE = "resource\\person_list_csv.csv"
EXCEL_FILE = "resource\\person_list_xlsx.xlsx"
ZIP_FILE = "resource\\test_zip_file.zip"
CSV_END = ".csv"
EXCEL_END = ".xlsx"
SHEET_NAME = "Sheet1"


class ExcelReader(Reader):
    def __init__(self, filepath, sheet_name):
        self.filepath = filepath
        self.sheet_name = sheet_name

    def read(self):
        assert self.filepath.endswith(EXCEL_END)

        person_list = []
        excel_file = xd.open_workbook(self.filepath, "r")
        sheet = excel_file.sheet_by_name(self.sheet_name)

        for row in range(1, sheet.nrows):
            id, name, gender = sheet.row_values(row)
            person_list.append(Person(id, name, gender))

        return person_list

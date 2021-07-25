# -*- coding: utf-8 -*
import unittest

from src.ui.usecase.csv_reader import CsvReader
from src.ui.usecase.zip_reader import ZipReader
from src.ui.usecase.excel_reader import ExcelReader

SHEET_NAME = "Sheet1"
CSV_TEST_FILE = "test\\resource\\_test_csv.csv"
ZIP_TEST_FILE = "test\\resource\\_test_zip.zip"
EXCEL_TEST_FILE = "test\\resource\\_test_excel.xlsx"
EXCEL_RESULT = [
    [2021001.0, "Mary", "women"],
    [2021002.0, "Jack", "man"],
    [2021003.0, "Mandy", "women"],
]
CSV_RESULT = [
    ["2021001", "Mary ", "women"],
    ["2021002", "Jack", "man"],
    ["2021003", "Mandy", "women"],
]


class TestReader(unittest.TestCase):
    def test_csv_in_zip(self):
        person_list = []
        read_list = ZipReader(ZIP_TEST_FILE, CSV_TEST_FILE).read()
        [
            person_list.append([person.id, person.name, person.gender])
            for person in read_list
        ]
        self.assertEqual(CSV_RESULT, person_list)

    def test_excel_in_zip(self):
        person_list = []
        read_list = ZipReader(ZIP_TEST_FILE, EXCEL_TEST_FILE, SHEET_NAME).read()
        [
            person_list.append([person.id, person.name, person.gender])
            for person in read_list
        ]
        self.assertEqual(EXCEL_RESULT, person_list)

    def test_excel(self):
        person_list = []
        read_list = ExcelReader(EXCEL_TEST_FILE, SHEET_NAME).read()
        [
            person_list.append([person.id, person.name, person.gender])
            for person in read_list
        ]
        self.assertEqual(EXCEL_RESULT, person_list)

    def test_csv(self):
        person_list = []
        read_list = CsvReader(CSV_TEST_FILE).read()
        [
            person_list.append([person.id, person.name, person.gender])
            for person in read_list
        ]
        self.assertEqual(CSV_RESULT, read_list)


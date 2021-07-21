# -*- coding: utf-8 -*
import unittest
from Josephus_reader_file import ZipReader,ExcelReader,CsvReader
from Josephus_reader_file import JosephusCircle
from Josephus_reader_file import Person

SHEET_NAME='Sheet1'
CSV_TEST_FILE='test_csv.csv'
ZIP_TEST_FILE='test_zip.zip'
EXCEL_TEST_FILE='test_excel.xlsx'
EXCEL_RESULT=[[2021001.0,'Mary','women'],[2021002.0,'Jack','man'],[2021003.0,'Mandy','women']]
CSV_RESULT=[['2021001','Mary ','women'],['2021002','Jack','man'],['2021003','Mandy','women']]
STEP=3
START=0


class TestPerson(unittest.TestCase):
    def test(self):
        self.assertEqual(('2021001,Alice,women'),Person('2021001','Alice','women').__str__())


class TestJosephusCircle(unittest.TestCase):
    def test(self):
        josephus_list=[]
        people_list=[1,2,3,4,5,6,7,8]
        [josephus_list.append(person) 
        for person in JosephusCircle(people_list,STEP,START)]
        self.assertEqual([3,6,1,5,2,8,4,7],josephus_list)


class TestReader(unittest.TestCase):
    def test_csv_in_zip(self):
        person_list=[]
        read_list=ZipReader(ZIP_TEST_FILE,CSV_TEST_FILE).read()
        [person_list.append([person.id,person.name,person.gender]) for person in read_list]
        self.assertEqual(CSV_RESULT,person_list)
   
    def test_excel_in_zip(self):
        person_list=[]
        read_list=ZipReader(ZIP_TEST_FILE,EXCEL_TEST_FILE,SHEET_NAME).read()
        [person_list.append([person.id,person.name,person.gender]) for person in read_list]
        self.assertEqual(EXCEL_RESULT,person_list)
   
    def test_excel(self):
        person_list=[]
        read_list=ExcelReader(EXCEL_TEST_FILE,SHEET_NAME).read()
        [person_list.append([person.id,person.name,person.gender]) for person in read_list]
        self.assertEqual(EXCEL_RESULT,person_list)

    def test_csv(self):
        person_list=[]
        read_list=CsvReader(CSV_TEST_FILE).read()
        [person_list.append([person.id,person.name,person.gender]) for person in read_list]
        self.assertEqual(CSV_RESULT,read_list)


if __name__ == '__main__':
    unittest.main()


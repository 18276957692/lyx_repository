# -*- coding: utf-8 -*
import zipfile
import csv
import xlrd as xd

class Reader(object):
    def __init__(self,filename,inter_filename=''):
        self.filename=filename
        self.inter_filename=inter_filename


class ZipReader(Reader):
    def zip_reader(self):
        assert self.inter_filename.endswith(".csv")or self.inter_filename.endswith(".xlsx")
        
        zip_file=zipfile.ZipFile(self.filename,'r')
        read_file=zip_file.extract(self.inter_filename)

        if self.inter_filename.endswith(".csv"):
            person_list=CsvReader(read_file).csv_reader()
            return person_list
        else: 
              person_list=ExcelReader(read_file).excel_reader()
              return person_list


class CsvReader(Reader):
    def csv_reader(self):
        assert self.filename.endswith(".csv")

        with open(self.filename,'r',encoding="utf-8")as file:
            person_list=[]
            csv_file=csv.reader(file)
            next(csv_file)

            for rows in csv_file:
                person_list=creat_people_list(rows,person_list)
            return person_list


class ExcelReader(Reader):
    def excel_reader(self):
        assert self.filename.endswith(".xlsx")

        person_list=[]
        excel_file=xd.open_workbook(self.filename,"r")
        sheet=excel_file.sheet_by_name("Sheet1")

        for row in range(1,sheet.nrows):
            person_list=creat_people_list(sheet.row_values(row),person_list)
        return person_list


class Person(object):
    def __init__(self,person_number,person_name,person_gender):
        self.person_number=person_number
        self.person_name=person_name
        self.person_gender=person_gender

    def print_person(person):
        print(person.person_number,person.person_name,person.person_gender)


def creat_people_list(person_attri,read_list):
    person_number,person_name,person_gender=person_attri
    read_list.append(
        Person(person_number,person_name,person_gender))
    return read_list


def josephus_problem(people_list,killed_step,killed_index,killed_list):
    assert len(people_list)>0
    assert killed_step>0
    assert killed_index<=len(people_list)

    killed_index=(killed_index+killed_step-1)%len(people_list)
    killed_list.append(
        people_list.pop(killed_index))
    return killed_index,killed_list


def josephus_ring_list(killed_step,killed_index):
    killed_list=[]
    for i in range(len(people_list)):
        (killed_index,killed_list)=josephus_problem(people_list,killed_step,killed_index,killed_list)
        
    for person in killed_list:
        person.print_person()       


if __name__ == '__main__':
    #people_list=ExcelReader("person_list_xlsx.xlsx").excel_reader()
    #people_list=CsvReader('person_list_csv.csv').csv_reader()
    people_list=ZipReader('test_zip_file.zip','person_list_csv.csv').zip_reader()
    josephus_ring_list(3,0)
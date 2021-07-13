# -*- coding: utf-8 -*
import zipfile
import csv
import pandas as pd
import xlrd as xd

class Reader(object):
    def creat_list(person_message,read_list):
        person_number,person_name,person_gender=person_message
        read_list.append(
            Person(person_number,person_name,person_gender))
        return read_list

class ZipReader(object):
    def zip_reader(zip_name,inter_filename):
        zip_file=zipfile.ZipFile(zip_name,'r')
        read_file=zip_file.extract(inter_filename)
        if inter_filename.endswith(".csv"):
            person_list=CsvReader.csv_reader(read_file)
            return person_list
        elif inter_filename.endswith(".xlsx"):
             person_list=ExcelReader.excel_reader(read_file)
             return person_list
        else:
            print('该文件类型不可读！')

class CsvReader(object):
    def csv_reader(csv_name):
        with open(csv_name,'r',encoding="utf-8")as file:
            csv_file=csv.reader(file)
            next(csv_file)
            person_list=[]

            for rows in csv_file:
                person_list=Reader.creat_list(rows,person_list)
            return person_list

class ExcelReader(object):
    def excel_reader(excel_name):
        excel_file=xd.open_workbook(excel_name,"r")
        sheet=excel_file.sheet_by_name("Sheet1")
        person_list=[]

        for row in range(1,sheet.nrows):
            person_list=Reader.creat_list(sheet.row_values(row),person_list)
        return person_list

class Person(object):
    def __init__(self,person_number,person_name,person_gender):
        self.person_number=person_number
        self.person_name=person_name
        self.person_gender=person_gender

    def print_person(person):
        print(person.person_number,person.person_name,person.person_gender)

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
    #people_list=ExcelReader.excel_reader('person_list_xlsx.xlsx)
    #people_list=CsvReader.csv_reader('person_list_csv.csv')
    people_list=ZipReader.zip_reader('test_zip_file.zip','person_list_csv.csv')
    josephus_ring_list(3,0)
# -*- coding: utf-8 -*
import zipfile
import csv
import xlrd as xd

CSV_FILE='person_list_csv.csv'
EXCEL_FILE='person_list_xlsx.xlsx'
ZIP_FILE='test_zip_file.zip'
CSV_END=".csv"
EXCEL_END=".xlsx"
SHEET_NAME='Sheet1'
STEP=3
START=0

class Reader(object):
    def __init__(self,filepath):
        self.filepath=filepath

    def read(self):
        pass


class ZipReader(Reader):
    def __init__(self,filepath,inter_filename,sheet_name=''): 
        self.filepath=filepath
        self.inter_filename=inter_filename
        self.sheet_name=sheet_name

    def read(self):
        assert self.inter_filename.endswith(CSV_END)or self.inter_filename.endswith(EXCEL_END)
        
        zip_file=zipfile.ZipFile(self.filepath)
        read_file=zip_file.extract(self.inter_filename)

        if self.inter_filename.endswith(CSV_END):
            person_list=CsvReader(read_file).read()
            return person_list
        elif self.inter_filename.endswith(EXCEL_END): 
             person_list=ExcelReader(read_file,SHEET_NAME).read()
             return person_list
        else:
            raise StopIteration


class CsvReader(Reader):
    def read(self):
        assert self.filepath.endswith(CSV_END)

        with open(self.filepath,'r',encoding="utf-8")as file:
            person_list=[]
            csv_file=csv.reader(file)
            next(csv_file)

            for row in csv_file:
                id,name,gender=row
                person_list.append(
                    Person(id,name,gender))
            return person_list
      

class ExcelReader(Reader):
    def __init__(self,filepath,sheet_name):
        self.filepath=filepath
        self.sheet_name=sheet_name

    def read(self):
        assert self.filepath.endswith(EXCEL_END)

        person_list=[]
        excel_file=xd.open_workbook(self.filepath,"r")
        sheet=excel_file.sheet_by_name(self.sheet_name)

        for row in range(1,sheet.nrows):
            id,name,gender=sheet.row_values(row)
            person_list.append(
                Person(id,name,gender))

        return person_list


class Person(object):
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender

    def __str__(self):
        return '[%s,%s,%s]'%(self.id,self.name,self.gender)
 
    def __repr__(self):
        return '[%s,%s,%s]'%(self.id,self.name,self.gender)


class JosephusCircle(list):
    def __init__(self,people_list,step,start) :
        assert step>0
        self.people_list=people_list
        self.step=step
        self.start=start
        self.josephus_list=[]

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.people_list)>0:
            self.start=(self.start+self.step-1)%len(self.people_list)
            self.josephus_list.append(
                self.people_list.pop(self.start))
            return self.josephus_list[-1]
        else: 
            raise StopIteration 


if __name__ == '__main__':
    #people_list=ExcelReader(EXCEL_FILE,'Sheet1').read()
    people_list=CsvReader(CSV_FILE).read()
   # people_list=ZipReader(ZIP_FILE,CSV_FILE).read()
    print(people_list)
   # killed_list=JosephusCircle(people_list,STEP,START) 

    #for person in killed_list:
     #   print(person)

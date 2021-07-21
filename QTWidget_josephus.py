# -*- coding: utf-8 -*
import sys
import json
from typing import Literal
from PySide6.QtCore import Signal,QObject
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QMainWindow, QPushButton, QTextEdit,QVBoxLayout,QMessageBox
from Josephus_reader_file import ZipReader,ExcelReader,CsvReader
from Josephus_reader_file import JosephusCircle
from Josephus_reader_file import Person

CSV_FILE='person_list_csv.csv'
EXCEL_FILE='person_list_xlsx.xlsx'
ZIP_FILE='test_zip_file.zip'
CSV_END=".csv"
EXCEL_END=".xlsx"
SHEET_NAME='Sheet1'
STEP=3
START=0

class Window(QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("约瑟夫环")
        self.resize(250,350)#主窗口尺寸 

        self.edit = QLineEdit("请点击以下文件，获取参与游戏人员名单")
        self.text=QTextEdit(self) 

        self.button_csv=QPushButton("csv")
        self.button_excel=QPushButton("excel")
        self.button_zip_csv=QPushButton("csv_in_zip")
        self.button_zip_excel=QPushButton("excel_in_zip")
        self.button_josephus=QPushButton("输出约瑟夫环弹出顺序")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button_csv)
        layout.addWidget(self.button_excel)
        layout.addWidget(self.button_zip_csv)
        layout.addWidget(self.button_zip_excel)
        layout.addWidget(self.text)
        layout.addWidget(self.button_josephus)
        self.setLayout(layout)

        self.button_csv.clicked.connect(self.get_peoplelist_from_csv)              
        self.button_excel.clicked.connect(self.get_peoplelist_from_excel)
        self.button_zip_csv.clicked.connect(self.get_peoplelist_from_zip_csv)
        self.button_zip_excel.clicked.connect(self.get_peoplelist_from_zip_excel)
        self.button_josephus.clicked.connect(self.output_josuphus_list)

    def get_peoplelist_from_csv(self):
        people_list=CsvReader(CSV_FILE).read()
        self.text.setPlainText(f'''{people_list}''')

    def get_peoplelist_from_excel(self):
        people_list=ExcelReader(EXCEL_FILE,SHEET_NAME).read()
        self.text.setPlainText(f'''{people_list}''')

    def get_peoplelist_from_zip_csv(self):
        people_list=ZipReader(ZIP_FILE,CSV_FILE).read()
        self.text.setPlainText(f'''{people_list}''')

    def get_peoplelist_from_zip_excel(self):
        people_list=ZipReader(ZIP_FILE,EXCEL_FILE).read()
        self.text.setPlainText(f'''{people_list}''')

    def output_josuphus_list(self): 
        input_people=self.text.toPlainText()
        people_list=input_people.split('[[')[1].split(']]')[0]
        josuphus_list=JosephusCircle(people_list.split("], ["),STEP,START) 
        people=[]
        for person in josuphus_list:
            people.append(person.__str__())
            self.text.setPlainText(f'''{people}''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
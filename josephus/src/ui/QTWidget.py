# -*- coding: utf-8 -*
import sys
import json

from PySide6.QtCore import Signal, QObject
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication, 
    QDialog, 
    QLineEdit, 
    QMainWindow, 
    QPushButton, 
    QTextEdit,
    QVBoxLayout,
    QMessageBox
)

from usecase.josephus_iter import JosephusCircle
from usecase.entity.person import Person
from usecase.csv_reader import CsvReader
from usecase.zip_reader import ZipReader
from usecase.excel_reader import ExcelReader


CSV_FILE = "test\\resource\\person_list_csv.csv"
EXCEL_FILE = "test\\resource\\person_list_xlsx.xlsx"
ZIP_FILE = "test\\resource\\zip_file.zip"
CSV_IN_ZIP_FILE = "csv_in_zip.csv"
EXCEL_IN_ZIP_FILE = "excel_in_zip.xlsx"
CSV_END = ".csv"
EXCEL_END = ".xlsx"
SHEET_NAME = "Sheet1"
STEP = 3
START = 0

class JosephusWindow(QDialog):

    def __init__(self, parent=None):
        super(JosephusWindow, self).__init__(parent)
        self.setWindowTitle("约瑟夫环")
        self.resize(250, 350)#主窗口尺寸 

        self.edit = QLineEdit("请点击以下文件，获取参与游戏人员名单")
        self.text = QTextEdit(self) 

        self.button_csv = QPushButton("csv")
        self.button_excel = QPushButton("excel")
        self.button_csv_in_zip = QPushButton("csv_in_zip")
        self.button_excel_in_zip = QPushButton("excel_in_zip")
        self.button_josephus = QPushButton("输出约瑟夫环弹出顺序")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button_csv)
        layout.addWidget(self.button_excel)
        layout.addWidget(self.button_csv_in_zip)
        layout.addWidget(self.button_excel_in_zip)
        layout.addWidget(self.text)
        layout.addWidget(self.button_josephus)
        self.setLayout(layout)

        self.button_csv.clicked.connect(self.get_peoplelist_from_csv)              
        self.button_excel.clicked.connect(self.get_peoplelist_from_excel)
        self.button_csv_in_zip.clicked.connect(self.get_peoplelist_from_zip_csv)
        self.button_excel_in_zip.clicked.connect(self.get_peoplelist_from_zip_excel)
        self.button_josephus.clicked.connect(self.output_josuphus_circle)

    def get_peoplelist_from_csv(self):
        people_list = CsvReader(CSV_FILE).read()
        self.text.setPlainText(f"""{people_list}""")

    def get_peoplelist_from_excel(self):
        people_list = ExcelReader(EXCEL_FILE,SHEET_NAME).read()
        self.text.setPlainText(f"""{people_list}""")

    def get_peoplelist_from_zip_csv(self):
        people_list = ZipReader(ZIP_FILE,CSV_IN_ZIP_FILE).read()
        self.text.setPlainText(f"""{people_list}""")

    def get_peoplelist_from_zip_excel(self):
        people_list = ZipReader(ZIP_FILE,EXCEL_IN_ZIP_FILE).read()
        self.text.setPlainText(f"""{people_list}""")

    def output_josuphus_circle(self): 
        read_people = self.text.toPlainText()
        people_list = read_people.split("[[")[1].split("]]")[0]
        killed_list = JosephusCircle(people_list.split("], ["),STEP,START) 
        people = []
        for person in killed_list:
            people.append(person.__str__())
            self.text.setPlainText(f"""{people}""")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JosephusWindow()
    window.show()
    sys.exit(app.exec_())
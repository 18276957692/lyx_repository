# -*- coding: utf-8 -*
import csv
import click

from .usecase.josephus_iter import JosephusCircle
from .usecase.entity.person import Person
from .usecase.zip_reader import ZipReader
from .usecase.excel_reader import ExcelReader
from .usecase.csv_reader import CsvReader

CSV_FILE = "test\\resource\\person_list_csv.csv"
EXCEL_FILE = "test\\resource\\person_list_xlsx.xlsx"
ZIP_FILE = "test\\resource\\test_zip_file.zip"
CSV_END = ".csv"
EXCEL_END = ".xlsx"
SHEET_NAME = "Sheet1"
STEP = 3
START = 0

# @click.command()
# @click.option('--file_type', type=click.Choice(['csv','excel','csv_in_zip','excel_in_zip']),help='type of file')
def josephus_console_interface():
    print("文件类型可选：'csv','excel','csv_in_zip','excel_in_zip'")
    file_type = input("请输入需要读取的文件类型：")
    assert (
        file_type == "csv"
        or file_type == "excel"
        or file_type == "csv_in_zip"
        or file_type == "excel_in_zip"
    )

    if file_type == ("csv"):
        people_list = CsvReader(CSV_FILE).read()
    elif file_type == ("excel"):
        people_list = ExcelReader(EXCEL_FILE, SHEET_NAME).read()
    elif file_type == ("csv_in_zip"):
        people_list = ZipReader(ZIP_FILE, "person_list_csv.csv").read()
    else:
        people_list = ZipReader(ZIP_FILE, "person_list_xlsx.xlsx").read()

    print("参与游戏的人员列表：")
    print(people_list)

    alter = input("输入yes可修改参与游戏的人员列表：")
    if alter == "yes":
        alter_list = input("请输入修改后的人员列表：")
        josephus_list = alter_list.split("[[")[1].split("]]")[0].split("], [")
    else:
        josephus_list = people_list

    killed_list = JosephusCircle(josephus_list, STEP, START)
    print("约瑟夫环人员弹出顺序：")
    for person in killed_list:
        print(person)

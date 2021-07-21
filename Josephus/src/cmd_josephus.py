# -*- coding: utf-8 -*
import csv
import click
from Josephus_reader_file import ZipReader, ExcelReader, CsvReader
from Josephus_reader_file import JosephusCircle
from Josephus_reader_file import Person

CSV_FILE = "person_list_csv.csv"
EXCEL_FILE = "person_list_xlsx.xlsx"
ZIP_FILE = "test_zip_file.zip"
CSV_END = ".csv"
EXCEL_END = ".xlsx"
SHEET_NAME = "Sheet1"
STEP = 3
START = 0

# @click.command()
# @click.option('--file_type', type=click.Choice(['csv','excel','csv_in_zip','excel_in_zip']),help='type of file')
def josephus_control_interface():
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
        people_list = ZipReader(ZIP_FILE, CSV_FILE).read()
    else:
        people_list = ZipReader(ZIP_FILE, EXCEL_FILE).read()

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


if __name__ == "__main__":
    josephus_control_interface()

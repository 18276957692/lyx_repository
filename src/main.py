from ui.QT_interfacet import JosephusWindow
from ui.console_interface import josephus_console_interface
from PySide6.QtWidgets import QApplication
import click
#import sys


#@click.command()
#@click.option('--type', type=click.Choice(['QT','cmd']),help='type of interface')
def show_josephus(type):
    assert type=="cmd"or type=="QT"

    if type=='cmd':
        josephus_console_interface()
    elif type=='QT' :
        app = QApplication()
        window = JosephusWindow()
        window.show()
        app.exec_()


if __name__ == "__main__":
    show_josephus('QT')
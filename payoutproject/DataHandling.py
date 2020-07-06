import pandas as pd
import numpy as np
import os.path

from logger import ltlogger


class DataHandler():
    def __init__(self, path_to_file):
        # self.csv_file = csv_file
        self.path_to_file = path_to_file

    def _CheckIfCSVExists(self):  # private
        # D:\Dropbox\PayoutProject.xlsx
        try:
            os.path.isfile(self.path_to_file)
            return "File Exists!", True
        except:
            return "File Does Not Exist!", False

    def PrintInformation(self):
        errormsg, fileexists = self._CheckIfCSVExists()
        if fileexists:
            file = pd.read_excel(self.path_to_file)
            print(file)
        else:
            print(errormsg)


if __name__ == '__main__':
    print("hello world")
    datafile = DataHandler('D:\Dropbox\PayoutProject.xlsx')
    datafile.PrintInformation()
    # use it like ordinary open like this:
    # w = SafeWriter("filename.txt", "w")
    # w.write("can be used among multiple threads")
    # w.close()  # it is really important to close or the program would not end

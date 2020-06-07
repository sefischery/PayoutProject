import pandas as pd
import numpy as np
import os.path

from queue import Queue, Empty
from threading import Thread

class SafeWriter:
    def __init__(self, *args):
        self.filewriter = open(*args)
        self.queue = Queue()
        self.finished = False
        Thread(name = "SafeWriter", target=self.internal_writer).start()

    def write(self, data):
        self.queue.put(data)

    def internal_writer(self):
        while not self.finished:
            try:
                data = self.queue.get(True, 1)
            except Empty:
                continue
            self.filewriter.write(data)
            self.queue.task_done()

    def close(self):
        self.queue.join()
        self.finished = True
        self.filewriter.close()




class DataHandler():
    def __init__(self,path_to_file):
        #self.csv_file = csv_file
        self.path_to_file = path_to_file

    def __CheckIfCSVExists(self): #private
        #D:\Dropbox\PayoutProject.xlsx
        try:
            os.path.isfile(self.path_to_file)
            return ("File Exists!",True)
        except:
            return ("File Does Not Exist!",False)

    def PrintInformation(self):
        errormsg, fileexists = self.__CheckIfCSVExists()
        if fileexists:
            file = pd.read_excel(self.path_to_file)
            print(file)
        else:
            print(errormsg)

if __name__ == '__main__':
    print("hello world")
    #datafile = DataHandler('D:\Dropbox\PayoutProject.xlsx')
    #datafile.PrintInformation()
    # use it like ordinary open like this:
    w = SafeWriter("filename", "w")
    w.write("can be used among multiple threads")
    w.close()  # it is really important to close or the program would not end

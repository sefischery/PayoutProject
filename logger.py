import logging

DEBUG = False

class ltlogger:
    def __init__(self, file_name):
        self.file_name = file_name
        logger_name = file_name
        formatter = logging.Formatter('%(asctime)s %(module)s %(funcName)s %(message)s')

        file_handler = logging.FileHandler(self.file_name,mode="w")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)


        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(file_handler)

        #fh is the filehandler logger, which means that we
        #could have multiple loggers, one for file, stream, etc.
        #fh = logging.FileHandler(self.file_name,mode='w')
        #fh.setLevel(logging.DEBUG)

        #logging.basicConfig(filename=self.file_name,level=logging.DEBUG,format='%(asctime)s %(module)s %(funcName)s %(message)s') #logging. is the root logger

    def write(self,msg):
        self.logger.log(logging.INFO,msg)

if DEBUG:
    if __name__ == "__main__":
        newlogger = ltlogger("justatest.log")
        newlogger.write("HELLOTEST")
        anotherlogger = ltlogger("alogtest.log")
        anotherlogger.write("HELLOANOTHERTEST")
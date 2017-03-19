import report
import pycurl

class Scan():
    match = False
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        print(self.rules)


    def unpack(self):
        pass

    def generateReport(self):
        print("Report generated")

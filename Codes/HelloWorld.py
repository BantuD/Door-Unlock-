from subprocess import call
from tkinter import *
from os import  *
root=Tk()
#class CallPy(object):
   # dataCollection="C:\\Users\\HP\Desktop\\FACELOCKING-DOOR-USING-PYTHON-AND-ARDUINO-PROGRAMING-master\\code\collecting data face1.py"
   # facelock="C:\\Users\\HP\Desktop\\FACELOCKING-DOOR-USING-PYTHON-AND-ARDUINO-PROGRAMING-master\\code\\facelockdoor.py"

#path1 = "C:\\Users\\HP\Desktop\\FACELOCKING-DOOR-USING-PYTHON-AND-ARDUINO-PROGRAMING-master\\code\collecting data face1.py"
#path2 = "C:\\Users\\HP\Desktop\\FACELOCKING-DOOR-USING-PYTHON-AND-ARDUINO-PROGRAMING-master\\code\\facelockdoor.py"


class LockSystem(object):
    def __init__(self,path2="C:\\Users\\HP\Desktop\\FACELOCKING-DOOR-USING-PYTHON-AND-ARDUINO-PROGRAMING-master\\code\\facelockdoor.py",
                 path1= "C:\\Users\\HP\Desktop\\FACELOCKING-DOOR-USING-PYTHON-AND-ARDUINO-PROGRAMING-master\\code\collecting data face1.py"):
        self.path1=path1
        self.path2=path2

    def call_Collection(self):

        call(["python","{}".format(self.path1)])

    def call_lock(self):
        call(["python","{}".format(self.path2)])




if __name__=="__main__":
    c=LockSystem()
    #c.call_lock()
    #c.call_Collection()

    Label(root,text="Facial Door Unlock")
    cButton=Button(root,text = "Collect Data",padx=40,pady=20,command=c.call_Collection).grid(row=1,column=0)
    lButton=Button(root,text= "Lock System",padx=40,pady=20,command=c.call_lock).grid(row=1,column=2)

    root.mainloop()
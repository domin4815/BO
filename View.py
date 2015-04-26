__author__ = 'domin4815'
from Tkinter import *
import Controller

#CONFIGe
inputWidth = 30
inputHeight = 2
controler = Controller.ProgramParametersManager(0,0,0,0,0,0)

strings = ['Iterations', 'Step len', 'Number of cockroaches', 'Number of jobs', 'Number of machines']
inputs = []
root = Tk()
root.title("BO")

r = 0
for c in strings:
    Label(root, text=c, relief=RIDGE,width=inputWidth, height=inputHeight).grid(row=r,column=0)
    T = Text(root, height=inputHeight, width=inputWidth)
    inputs.append(T)
    T.grid(row=r, column=1)
    r = r + 1

def nextButton():
    try:
        controler.iterations = int(inputs[0].get("1.0",'end-1c'))
        controler.stepLen = int(inputs[1].get("1.0",'end-1c'))
        controler.cockroachesNum = int(inputs[2].get("1.0",'end-1c'))
        controler.jobsNum = int(inputs[3].get("1.0",'end-1c'))
        controler.machinesNum = int(inputs[4].get("1.0",'end-1c'))
    except ValueError:
        print("Value error")
    controler.printParameters()



button = Button(root, text='Next >', width=inputWidth-15, command=nextButton, height=inputHeight).grid(row=r, column=0)
r = r +1

mainloop()

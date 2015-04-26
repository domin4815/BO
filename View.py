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
    controler.iterations = inputs[0]
    controler.stepLen = inputs[1]
    controler.cockroachesNum = inputs[2]
    controler.jobsNum = inputs[3]
    controler.machinesNum = inputs[4]



button = Button(root, text='Next >', width=inputWidth-15, command=nextButton, height=inputHeight).grid(row=r, column=0)
r = r +1

mainloop()

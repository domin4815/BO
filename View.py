__author__ = 'domin4815'
from Tkinter import *
import Algorytm
#CONFIG
inputWidth = 26
inputHeight = 2


buttonWidth = 20
buttonHeight = 2


labelHeight = 2
labelWidth = 23

def frame1(controler):


    strings = ['Iterations', 'Step len', 'Number of cockroaches', 'Number of jobs', 'Number of machines']
    inputs = []
    root = Tk()
    root.title("BO")

    r = 0
    for c in strings:
        Label(root, text=c, width=labelWidth, height=labelHeight).grid(row=r,column=0)
        T = Entry(root)
        inputs.append(T)
        T.grid(row=r, column=1)
        r = r + 1

    def nextButton():
        try:
            controler.iterations = int(inputs[0].get())
            controler.stepLen = int(inputs[1].get())
            controler.cockroachesNum = int(inputs[2].get())
            controler.jobsNum = int(inputs[3].get())
            controler.machinesNum = int(inputs[4].get())
        except ValueError:
            print("Value error")
        #controler.printParameters()
        root.destroy()
        frame2(controler)

    button = Button(root, text='Next', width=buttonWidth, command=nextButton, height=buttonHeight).grid(row=r, column=0)
    button2 = Button(root, text='Next with \ndefault values', width=buttonWidth, command=nextButton, height=buttonHeight).grid(row=r, column=1)

    mainloop()

def frame2(controler):
    root = Tk()
    root.title("BO")
    inputs = []
    r = 0
    for i in range(0, controler.jobsNum):
        Label(root, text='Job ' + str(i+1) + ' time', width=labelWidth, height=labelHeight).grid(row=r,column=0)
        T = Entry(root)
        T.insert(0, str(i+7))
        inputs.append(T)
        T.grid(row=r, column=1)
        r = r + 1
    def goButton():
        try:
            for i in range(0, controler.jobsNum):
                controler.jobs += [int(inputs[i].get())]
        except ValueError:
            print("Value error")
        root.destroy()
        Algorytm.runCockroaches(controler.iterations, controler.stepLen, controler.cockroachesNum, controler.jobsNum, controler.machinesNum, controler.jobs)


    def backButton():
        root.destroy()
        frame1(controler)
    button = Button(root, text='Go', width=buttonWidth, command=goButton, height=buttonHeight).grid(row=r, column=1)
    button2 = Button(root, text='Back', width=buttonWidth, command=backButton, height=buttonHeight).grid(row=r, column=0)

    mainloop()
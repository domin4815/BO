#  -*- coding: latin-1 -*-
import pylab

__author__ = 'domin4815'
from Tkinter import *
import flowshop
from tkFileDialog import askopenfilename
# CONFIG
input_width = 26
input_height = 2

button_width = 20
button_height = 2

label_height = 2
label_width = 23

title = "BO"


def inputChooserFrame(controller):
    root = Tk()
    root.title(title)

    # width x height + x_offset + y_offset:

    def readFromFileButton():
        root.destroy()
        readFromFileFrame(controller)
        pass

    def insertDataMAnuallyButton():
        root.destroy()
        insertDataManuallyFrame1(controller)
        pass

    def readTest():
        root.destroy()
        readFromFileFrame(controller, filename="tai20_5short.txt")

    Label(root, text='\nFlow shop problem... \n'
                     '... by cockroach algorithm.\n', width=label_width, height=label_height+2).pack()

    readFileButton = Button(root, text='Read from file', width=button_width,
                    command=readFromFileButton,
                    height=button_height).pack()
    insertDataManuallyButton = Button(root, text='Insert data manually', width=button_width,
                command=insertDataMAnuallyButton,
                height=button_height).pack()
    readFileTestButton = Button(root, text='tai20_5short.txt', width=button_width, command=readTest, bg="red",
                height=button_height).pack()
    helpButton = Button(root, text='Help', width=button_width, command=readTest,
                height=button_height).pack()
    aboutButton = Button(root, text='About', width=button_width, command=readTest,
                height=button_height).pack()
    exitButton = Button(root, text='Exit', width=button_width, command=readTest,
                height=button_height).pack()

    mainloop()


def insertDataManuallyFrame1(controller):
    strings = [
        'Iterations', 'Step len', 'Number of cockroaches',
        'Number of jobs', 'Number of machines'
    ]
    inputs = []
    root = Tk()
    root.title("BO")

    r = 0
    for c in strings:
        Label(root, text=c, width=label_width, height=label_height).grid(row=r, column=0)
        T = Entry(root)
        inputs.append(T)
        T.grid(row=r, column=1)
        r = r + 1

    def next_button():
        try:
            controller.iterations = int(inputs[0].get())
            controller.step_len = int(inputs[1].get())
            controller.cockroaches_num = int(inputs[2].get())
            controller.jobs_num = int(inputs[3].get())
            controller.machines_num = int(inputs[4].get())
        except ValueError:
            pass
        root.destroy()
        insertDataManuallyFrame2(controller)

    button = Button(root, text='Next', width=button_width, command=next_button,
                    height=button_height).grid(row=r, column=0)
    button2 = Button(
        root, text='Next with \ndefault values',
        width=button_width, command=next_button, height=button_height
    ).grid(row=r, column=1)

    mainloop()


def insertDataManuallyFrame2(controller):
    root = Tk()
    root.title("BO")
    inputs = []
    r = 0
    for i in xrange(0, controller.jobs_num):
        Label(root, text='Job #{0} time'.format(str(i + 1)), width=label_width,
              height=label_height).grid(row=r, column=0)
        T = Entry(root)
        T.insert(0, str(i + 7))
        inputs.append(T)
        T.grid(row=r, column=1)
        r = r + 1

    def go_button():
        try:
            for i in range(0, controller.jobs_num):
                inputsStr = inputs[i].get().split(" ")
                inputsInt = []
                for ia in xrange(len(inputsStr)):
                    inputsInt.append(int(inputsStr[ia]))
                controller.jobs += [inputsInt]
        except ValueError:
            print(controller.jobs)
        root.destroy()
        flowshop.run_cockroaches(
            controller.iterations, controller.step_len,
            controller.cockroaches_num, controller.jobs_num,
            controller.machines_num,
            controller.jobs
        )

    def back_button():
        root.destroy()
        insertDataManuallyFrame1(controller)

    button = Button(root, text='Go', width=button_width, command=go_button,
                    height=button_height).grid(row=r, column=1)
    button2 = Button(root, text='Back', width=button_width, command=back_button,
                     height=button_height).grid(row=r, column=0)

    mainloop()


def readFromFileFrame(controller, filename="none"):
    root = Tk()
    root.title(title)
    if (filename == "none"):
        filename = askopenfilename()
    file = open(filename, 'r')

    inputs = []
    r = 0
    nehCheckboxInt = IntVar()
    Label(root, text="Run NEH before start", width=label_width, height=label_height).grid(row=r, column=0)
    Checkbutton(root, text="NEH", variable=nehCheckboxInt).grid(row=r, column=1)
    r+=1
    Label(root, text='Iterations', width=label_width, height=label_height).grid(row=r, column=0)
    T1 = Entry(root)
    T1.insert(0, controller.iterations)
    inputs.append(T1)
    T1.grid(row=r, column=1)
    r += 1
    Label(root, text='Step len', width=label_width, height=label_height).grid(row=r, column=0)
    T2 = Entry(root)
    T2.insert(0, controller.step_len)
    inputs.append(T2)
    T2.grid(row=r, column=1)
    r += 1
    Label(root, text='Cockroaches', width=label_width, height=label_height).grid(row=r, column=0)
    T3 = Entry(root)
    T3.insert(0, controller.step_len)
    inputs.append(T3)
    T3.grid(row=r, column=1)
    r += 1

    def next_button():
        try:
            controller.iterations = int(inputs[0].get())
        except ValueError:
            pass

        try:
            controller.step_len = int(inputs[1].get())
        except ValueError:
            pass
        try:
            controller.cockroaches_num = int(inputs[2].get())
        except ValueError:
            pass
        root.destroy()
        if nehCheckboxInt.get() == 0:
            controller.isNehEnabled = False
        else:
            controller.isNehEnabled = True
        controller.file = file
        pass

    def back_button():
        print("Not implemented...")
        pass


    buttonBack = Button(root, text='Back', width=button_width, command=back_button,
                    height=button_height).grid(row=r, column=0)
    button = Button(root, text='Start', width=button_width, command=next_button, bg='green',
                    height=button_height).grid(row=r, column=1)

    mainloop()

#jako arg lista [controler]
def presentSolutionsFrame(listOfCtrls):
    root = Tk()
    root.title(title + " - results") #
    r=0 #row
    Label(root, text="Parameter", width=label_width, height=label_height).grid(row=r, column=0)
    Label(root, text="Result", width=(label_width + len(listOfCtrls) + 15), height=label_height).grid(row=r, column=1)
    Label(root, text="Given", width=label_width, height=label_height).grid(row=r, column=2)
    r += 1

    for ctrl in listOfCtrls:
        Label(root, text="Makespan ", width=label_width, height=label_height).grid(row=r, column=0)
        Label(root, text=ctrl.minMakespan, width=label_width, height=label_height).grid(row=r, column=1)
        Label(root, text="Not implemented", width=label_width, height=label_height).grid(row=r, column=2)

        r += 1
        Label(root, text="Order ", width=label_width, height=label_height).grid(row=r, column=0)
        Label(root, text=ctrl.order, width=label_width, height=label_height).grid(row=r, column=1)
        Label(root, text="Not implemented", width=label_width, height=label_height).grid(row=r, column=2)
        r += 1

        Label(root, text="Algorithm time ", width=label_width, height=label_height).grid(row=r, column=0)
        Label(root, text=ctrl.time, width=label_width, height=label_height).grid(row=r, column=1)
        Label(root, text="none", width=label_width, height=label_height).grid(row=r, column=2)
        r += 1

        Label(root, text="With NEH ", width=label_width, height=label_height).grid(row=r, column=0)
        Label(root, text=ctrl.isNehEnabled, width=label_width, height=label_height).grid(row=r, column=1)
        Label(root, text="none", width=label_width, height=label_height).grid(row=r, column=2)
        r += 1
        #dolozyc jeszcze pare statystyk plus wizualizacje


    def next_button():

        pass

    def back_button():
        print("Not implemented...")
        pass
    def showPlots():
        for ctrl in listOfCtrls:
            pylab.plot(ctrl.makespanTable)
            pylab.show()
            #dodac tytul
        pass


    buttonBack = Button(root, text='Again', width=button_width, command=back_button,
                    height=button_height).grid(row=r, column=0)
    buttonShowPlots = Button(root, text='Show Plots', width=button_width, command=showPlots,
                    height=button_height).grid(row=r, column=1)
    button = Button(root, text='Exit', width=button_width, command=next_button,
                    height=button_height).grid(row=r, column=2)
    r +=1

    mainloop()
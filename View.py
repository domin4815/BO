#!/usr/bin/python
#  -*- coding: latin-1 -*-
__author__ = 'domin4815'
from Tkinter import *
import flowshop
import re
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

    def nahButton():
        pass

    def insertDataMAnuallyButton():
        root.destroy()
        insertDataManuallyFrame1(controller)
        pass

    def readTest():
        root.destroy()
        readFromFileFrame(controller, filename="tai20_5.txt")



    logo = PhotoImage(file="images/agh.png")
    w1 = Label(root, image=logo).pack()

    nahButton = Button(root, text='NAH', width=button_width, command=nahButton, bg='green',
                    height=button_height).pack()
    readFileButton = Button(root, text='Read from file', width=button_width, command=readFromFileButton, bg='sea green',
                    height=button_height).pack()
    readFileButton = Button(root, text='Insert data manually', width=button_width, command=insertDataMAnuallyButton, bg='dark olive green',
                height=button_height).pack()
    readFileTestButton = Button(root, text='Read from tai20_5.txt', width=button_width, command=readTest, bg='red',
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
            print("Value error")
        #controler.print_parameters()
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
                controller.jobs += [int(inputs[i].get())]
        except ValueError:
            print("Value error")
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
    pattern = re.compile(r'([0-9]+)')

    try: # nie umiem pythona
        while(file.readline()[0]=='n'): #number of jobs, number of machines, initial seed, upper bound and lower bound :
            str = file.readline()
            out2 = pattern.findall(str)

            jobsNum = int(out2[0])
            machinesNum = int(out2[1])
            initialSpeed = int(out2[2])
            upperBound = int(out2[3])
            liwerBound = int(out2[4])

            jobsTab = []

            for i in range(jobsNum):
                jobsTab.append([])

            file.readline() #processing times :
            for machineN in range(machinesNum):
                str = file.readline()
                jobsTimesOnMachine = pattern.findall(str)
                for jobN in range(jobsNum):
                    jobsTab[jobN].append(jobsTimesOnMachine[jobN])
            print(jobsTab[0])

    except IndexError:
        pass


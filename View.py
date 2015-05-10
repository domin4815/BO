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

        readFromFileFrame(controller, isNehEnabled=False)
        pass

    def nahButton():
        pass

    def insertDataMAnuallyButton():
        root.destroy()
        insertDataManuallyFrame1(controller)
        pass

    def readTest():
        root.destroy()
        readFromFileFrame(controller, isNehEnabled=False, filename="tai20_5short.txt")

    def readTestWithNeh():
        root.destroy()
        readFromFileFrame(controller, isNehEnabled=True, filename="tai20_5short.txt")


    #logo = PhotoImage(file="images/agh.png")
    #w1 = Label(root, image=logo).pack()

    nahButton = Button(root, text='NAH', width=button_width, command=nahButton, bg='green',
                    height=button_height).pack()
    readFileButton = Button(root, text='Read from file', width=button_width, command=readFromFileButton, bg='sea green',
                    height=button_height).pack()
    readFileButton = Button(root, text='Insert data manually', width=button_width, command=insertDataMAnuallyButton, bg='dark olive green',
                height=button_height).pack()
    readFileTestButton = Button(root, text='Read from tai20_5short.txt \n'
                                           'iterations = 400\n'
                                           'step len = 3\n'
                                           'cockroaches = 30', width=button_width, command=readTest, bg='red',
                height=button_height+3).pack()
    readFileTestWithNehButton = Button(root, text='Read from tai20_5short.txt \n'
                                           'iterations = 400\n'
                                           'step len = 3\n'
                                           'cockroaches = 30\n'
                                           'NEH = wlaczony', width=button_width, command=readTestWithNeh, bg='blue',
                height=button_height+3).pack()
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

def readFromFileFrame(controller, isNehEnabled, filename="none"):
    root = Tk()
    root.title(title)
    if (filename == "none"):
        filename = askopenfilename()
    file = open(filename, 'r')

    strings = [
        'Iterations', 'Step len', 'Number of cockroaches'
    ]
    inputs = []
    r = 0
    Label(root, text="Insert data or click start", width=label_width, height=label_height, bg="green").grid(row=r, column=0)
    Label(root, text="to run with default values", width=label_width, height=label_height, bg="green").grid(row=r, column=1)
    r+=1
    for c in strings:
        Label(root, text=c, width=label_width, height=label_height).grid(row=r, column=0)
        T = Entry(root)
        inputs.append(T)
        T.grid(row=r, column=1)
        r += 1

    def next_button():
        #nie umiem pythona2
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
        parseFile(controller, file, isNehEnabled)

    def back_button():
        print("Not implemented...")
        pass


    buttonBack = Button(root, text='Back', width=button_width, command=back_button,
                    height=button_height).grid(row=r, column=0)
    button = Button(root, text='Start', width=button_width, command=next_button, bg='green',
                    height=button_height).grid(row=r, column=1)

    mainloop()


def parseFile(controller, file, isNehEnabled):
    print("Parsing input data...")
    pattern = re.compile(r'([0-9]+)')
    try: # nie umiem pythona
        #plik z instancjami zawiera 10 roznych zestawow danych wejsciowych
        while(file.readline()[0]=='n'): #number of jobs, number of machines, initial seed, upper bound and lower bound :
            str = file.readline()
            out2 = pattern.findall(str)

            controller.jobs_num = int(out2[0])
            controller.machines_num = int(out2[1])
            if controller.iterations == 0:
                controller.iterations = 400
            if controller.step_len == 0:
                controller.step_len = 3
            if controller.cockroaches_num == 0:
                controller.cockroaches_num = 30
            initialSpeed = int(out2[2])
            upperBound = int(out2[3])
            liwerBound = int(out2[4])

            jobsTab = []

            for i in range(controller.jobs_num):
                jobsTab.append([])

            file.readline() #processing times :
            for machineN in range(controller.machines_num):
                str = file.readline()
                jobsTimesOnMachine = pattern.findall(str)
                for jobN in range(controller.jobs_num):
                    jobsTab[jobN].append(int(jobsTimesOnMachine[jobN]))
            controller.jobs = jobsTab
            print("flowshop wystartowany z parametrami:")
            print("iteracje: ", controller.iterations)
            print("step: ", controller.step_len)
            print("karaluchy: ", controller.cockroaches_num)
            startFlowshop(controller, isNehEnabled)


    except IndexError:
        pass


def startFlowshop(controller, isNehEnabled):
    flowshop.startFromGUI(controller, isNehEnabled)

#  -*- coding: latin-1 -*-
import matplotlib.pyplot as plt
from random import shuffle, randint, uniform
from Tkinter import *
import flowshop
from Controller import *
import tkMessageBox

from tkFileDialog import askopenfilename
# CONFIG
input_width = 26
input_height = 2

button_width = 15
button_height = 2

label_height = 2
label_width = 23
inputs22 = []

title = "Cockroach Swarm Optimization in flow-shop job scheduling"


def inputChooserFrame(controller):
    root = Tk()
    root.title(title)

    # width x height + x_offset + y_offset:

    def readFromFileButton():
        root.destroy()
        readFromFileFrame(controller)
        pass
    def help_button_function():
        help_frame()
        pass

    def insertDataMAnuallyButton():
        root.destroy()
        insertDataManuallyFrame1(controller)
        pass

    def readTest():
        root.destroy()
        readFromFileFrame(controller, filename="tai50_20short.txt")

    def exit_program():
        root.destroy()
        controller.exit_now = True
        pass

    def about():
        aboutFrame()
        pass

    Label(root, text='\n Cockroach Swarm Optimization \n'
                     'in flow-shop job scheduling\n', width=label_width, height=label_height+2).pack()

    readFileButton = Button(root, text='Read from file', width=button_width,
                    command=readFromFileButton,
                    height=button_height).pack()
    insertDataManuallyButton = Button(root, text='Insert data manually', width=button_width,
                command=insertDataMAnuallyButton,
                height=button_height).pack()
    readFileTestButton = Button(root, text='tai50_20short.txt', width=button_width, command=readTest, bg="red",
                height=button_height).pack()
    helpButton = Button(root, text='Help', width=button_width, command=help_button_function,
                height=button_height).pack()
    aboutButton = Button(root, text='About', width=button_width, command=about,
                height=button_height).pack()
    exitButton = Button(root, text='Exit', width=button_width, command=exit_program,
                height=button_height).pack()

    mainloop()


def insertDataManuallyFrame1(controller):
    strings = [
        'Iterations', 'Step len', 'Number of cockroaches',
        'Number of jobs', 'Number of machines', 'Visual'
    ]
    inputs = []
    root = Tk()
    root.title("BO")

    r = 0
    nehCheckboxInt = IntVar()
    graphCheckboxInt = IntVar()
    Label(root, text="Run NEH before start", width=label_width, height=label_height).grid(row=r, column=0)
    Checkbutton(root, text=" NEH ", variable=nehCheckboxInt).grid(row=r, column=1)
    r+=1
    Label(root, text="Show graph dynamically", width=label_width, height=label_height).grid(row=r, column=0)
    Checkbutton(root, text="Graph", variable=graphCheckboxInt).grid(row=r, column=1)
    r +=1
    for c in strings:
        Label(root, text=c, width=label_width, height=label_height).grid(row=r, column=0)
        T = Entry(root)
        inputs.append(T)
        T.grid(row=r, column=1)
        r = r + 1
    inputs[0].insert(0, "1000")
    inputs[1].insert(0, "4")
    inputs[2].insert(0, "25")
    inputs[3].insert(0, "10") #jobs
    inputs[4].insert(0, "8") #machines
    inputs[5].insert(0, "10")




    def next_button():
        if nehCheckboxInt.get() == 0:
            controller.isNehEnabled = False
        else:
            controller.isNehEnabled = True

        if graphCheckboxInt.get() == 0:
            controller.showDinamicallyGraph = False
        else:
            controller.showDinamicallyGraph = True

        try:
            controller.iterations = int(inputs[0].get())
            controller.step_len = int(inputs[1].get())
            controller.cockroaches_num = int(inputs[2].get())
            controller.jobs_num = int(inputs[3].get())
            controller.machines_num = int(inputs[4].get())
            controller.visual= int(inputs[5].get())
        except ValueError:
            pass
        root.destroy()
        insertDataManuallyFrame2(controller)

    def back_button():
        root.destroy()
        inputChooserFrame(controller)
        pass

    button2 = Button(
        root, text='< Back',
        width=button_width, command=back_button, height=button_height
    ).grid(row=r, column=0)

    button = Button(root, text='Next >', width=button_width, command=next_button,
                    height=button_height).grid(row=r, column=1)

    mainloop()


def aboutFrame():
    root = Tk()
    root.title(title)
    root.config(bg = 'grey70')
    def exit_about():
        root.destroy()
        pass
    label = Label(root, text="Cockroach Swarm Optimization algorithm in flow-shop job scheduling. \n"
                             "\n"
                             "Flow shop scheduling problems, are a class of scheduling problems with\n"
                             "a workshop or group shop in which the flow control shall enable an appropriate sequencing\n"
                             "for each job and for processing on a set of machines or with other\n"
                             "resources 1,2,...,m in compliance with given processing orders. Especially the maintaining\n"
                             "of a continuous flow of processing tasks is desired with a minimum\n"
                             "of idle time and a minimum of waiting time. Flow shop scheduling is a special\n"
                             "case of job shop scheduling where there is strict order of all operations\n"
                             " to be performed on all jobs. Flow shop scheduling may apply\n"
                             "as well to production facilities as to computing designs.\n"
                             "\n"
                             "Program uses Cockroach Swarm Optimization to solve flow-shop problem\n"
                             "\n"
                             "Authors:\n"
                             "Dominik Przepiora\n"
                             "Rafal Rozak\n"
                             "Grzegorz Kosowicz\n"
                             "", width=label_width+50, height=label_height+15, bg='grey70')


    label.pack()
    exitButton = Button(root, text='Exit', width=button_width, command=exit_about, bg = 'grey60',
                height=button_height).pack()
    mainloop()

def help_frame():
    root = Tk()
    root.title(title)
    root.config(bg = 'grey70')

    def exit_help():
        root.destroy()
        pass

    label = Label(root, text="Project documentation address: \n"
                             "https://docs.google.com/document/d/1Ry-Kql4B4GaYOmJUT56LgnelMhuLrx5RKo0iYm1-na4/edit# \n"
                             "", width=label_width+100, height=label_height+5, bg='grey70')
    label.pack()
    exitButton = Button(root, text='Exit', width=button_width, command=exit_help, bg = 'grey60',
                height=button_height).pack()
    mainloop()

def insertDataManuallyFrame2(controller):
    root = Tk()
    root.title(title)
    root.configure(background='grey60')
    inputs = []
    r = 0

    for i in xrange(0, controller.jobs_num):
        Label(root, text='Job #{0} time'.format(str(i + 1)), width=label_width,
              height=label_height).grid(row=r, column=0)
        entryTab = []
        for m in range(controller.machines_num):
            T = Entry(root)
            T.config(width=4)
            T.grid(row=r, column=m + 2)
            T.insert(0, str(randint(1,1000)))
            entryTab.append(T)
        inputs.append(entryTab)
        r = r + 1

    def go_button():
        try:
            for i in range(0, controller.jobs_num):
                inputsStr = []
                for i2 in range(controller.machines_num):
                    inputsStr.append(inputs[i][i2].get())

                inputsInt = []
                for ia in range(len(inputsStr)):
                    inputsInt.append(int(inputsStr[ia]))
                controller.jobs += [inputsInt]
        except ValueError:
            print("VALUE ERROR",controller.jobs)
        root.destroy()
        # flowshop.run_cockroaches(
        #     controller.iterations, controller.step_len,
        #     controller.cockroaches_num, controller.jobs_num,
        #     controller.machines_num,
        #     controller.jobs
        # )

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
    graphCheckboxInt = IntVar()
    Label(root, text="Run NEH before start", width=label_width, height=label_height).grid(row=r, column=0)
    Checkbutton(root, text=" NEH ", variable=nehCheckboxInt).grid(row=r, column=1)
    r+=1
    Label(root, text="Show graph dynamically  ", width=label_width, height=label_height).grid(row=r, column=0)
    Checkbutton(root, text="Graph", variable=graphCheckboxInt).grid(row=r, column=1)
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
    Label(root, text='Visual', width=label_width, height=label_height).grid(row=r, column=0)
    T4 = Entry(root)
    T4.insert(0, controller.step_len)
    inputs.append(T4)
    T4.grid(row=r, column=1)
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
        try:
            controller.visual = int(inputs[3].get())
        except ValueError:
            pass
        root.destroy()
        if nehCheckboxInt.get() == 0:
            controller.isNehEnabled = False
        else:
            controller.isNehEnabled = True

        if graphCheckboxInt.get() == 0:
            controller.showDinamicallyGraph = False
        else:
            controller.showDinamicallyGraph = True
        controller.file = file
        pass

    def back_button():
        root.destroy()
        inputChooserFrame(controller)
        pass

    buttonBack = Button(root, text='Back', width=button_width, command=back_button,
                    height=button_height).grid(row=r, column=0)
    button = Button(root, text='Start', width=button_width, command=next_button, bg='green',
                    height=button_height).grid(row=r, column=1)

    mainloop()

#jako arg lista [controler]
def presentSolutionsFrame(solution, controller):

    mainloop()


def allInOneFrame(controller, solution = None):
    root = Tk()
    root.title(title)
    img = PhotoImage(file='a.gif')
    root.tk.call('wm', 'iconphoto', root._w, img)

    input_choose_frame = Frame(width=1200, height=50, background="gray40")
####################################
    def readFromFileButton():
        #readFileButton.config(state = "disable")
        #readFromFileFrame(controller)
        filename = "none"
        if (filename == "none"):
            filename = askopenfilename()
        file = open(filename, 'r')
        controller.file = file
        inputs[3].delete(0, 'end')
        inputs[4].delete(0, 'end')
        print("Parsing input data...")
        pattern = re.compile(r'([0-9]+)')
        solutionsTable = []
        str = file.readline()#pierwszza linia do kosza
        str = file.readline()

        out2 = pattern.findall(str)
        controller.jobs_num = int(out2[0])
        print("AAAAAAAAAAAAAAA", controller.jobs_num)
        controller.machines_num = int(out2[1])

        initialSpeed = int(out2[2])
        controller.upperbound = int(out2[3])
        controller.lowerbound = int(out2[4])
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
        print("flowshop startuje z parametrami:")
        print("iteracje: ", controller.iterations)
        print("step: ", controller.step_len)
        print("karaluchy: ", controller.cockroaches_num)
        ###########r = flowshop.startFromGUI(controller)
        #robie nowy tylko do podawania ezultatu obliczen


        inputs[3].insert(0, "From file: "+`controller.jobs_num`) #jobs
        inputs[4].insert(0, "From file: "+`controller.machines_num`) #machines

        inputs[3].config(state = "disable")
        inputs[4].config(state = "disable")

        pass

    def help_button_function():
        help_frame()
        pass

    def insertDataMAnuallyButton():
        insertDataManuallyFrame1(controller)
        pass

    def readTest():

        root.destroy()
        readFromFileFrame(controller, filename="tai50_20short.txt")

    def exit_program():
        root.destroy()
        controller.exit_now = True
        pass

    def about():
        aboutFrame()
        pass

    readFileButton = Button(input_choose_frame, bg = 'grey70', text='Read from file', width=button_width+25,
                    command=readFromFileButton,
                    height=button_height)
    readFileButton.pack(side = LEFT)
    # insertDataManuallyButton = Button(input_choose_frame, text='Insert data manually', width=button_width,
    #             command=insertDataMAnuallyButton, bg = 'grey70',
    #             height=button_height).pack(side = LEFT)


    helpButton = Button(input_choose_frame, text='Help', width=button_width+25, command=help_button_function,
                height=button_height, bg = 'grey70').pack(side = LEFT)
    aboutButton = Button(input_choose_frame, bg = 'grey70', text='About', width=button_width+25, command=about,
                height=button_height).pack(side = LEFT)
    exitButton = Button(input_choose_frame, bg = 'grey70', text='Exit', width=button_width+25, command=exit_program,
                height=button_height).pack(side = LEFT)
    input_choose_frame.pack(side = TOP, fill = X)

####################################
    lab_to_refresh = []

    parameters_frame = Frame(width=200, height=500)

    strings = [
        'Iterations', 'Step len', 'Number of cockroaches',
        'Number of jobs', 'Number of machines', 'Visual'
    ]
    inputs = []


    r = 0
    lab1 = Label(parameters_frame, text="Parameters:", fg="black", font="Verdana 12 bold")
    lab1.grid(row=r, column=0)
    lab_to_refresh.append(lab1)
    r+=1



    nehCheckboxInt = IntVar()
    graphCheckboxInt = IntVar()
    Label(parameters_frame, text="Run NEH before start", width=label_width, height=label_height).grid(row=r, column=0)
    Checkbutton(parameters_frame, text=" NEH ", variable=nehCheckboxInt).grid(row=r, column=1)
    r+=1
    Label(parameters_frame, text="Show graph dynamically  ", width=label_width, height=label_height).grid(row=r, column=0)
    Checkbutton(parameters_frame, text="Graph", variable=graphCheckboxInt).grid(row=r, column=1)
    controller.file = None
    r +=1
    for c in strings:
        Label(parameters_frame, text=c, width=label_width, height=label_height).grid(row=r, column=0)
        T = Entry(parameters_frame)
        inputs.append(T)
        T.grid(row=r, column=1)
        r = r + 1
    inputs[0].insert(0, "1000")
    inputs[1].insert(0, "4")
    inputs[2].insert(0, "25")
    inputs[3].insert(0, "10")
    inputs[4].insert(0, "8")
    inputs[5].insert(0, "10")



    labelsToHide = []
    buttonsToForget = []

    def next_button():
       # buttonApply.config(state = "disable")

        for a in inputs22:
            for b in a:
                b.grid_forget()
        global  inputs22
        inputs22 = []
        for a in labelsToHide:
            a.grid_forget()
        for a in buttonsToForget:
            a.grid_forget()
        for a in lab_to_refresh:
            a.grid_forget()


        if nehCheckboxInt.get() == 0:
            controller.isNehEnabled = False
        else:
            controller.isNehEnabled = True

        if graphCheckboxInt.get() == 0:
            controller.showDinamicallyGraph = False
        else:
            controller.showDinamicallyGraph = True

        try:
            controller.iterations = int(inputs[0].get())
        except ValueError:
            pass
            controller.step_len = int(inputs[1].get())
            controller.cockroaches_num = int(inputs[2].get())
        try:
            if controller.file is None:
                controller.jobs_num = int(inputs[3].get())
        except ValueError:
            pass
        try:
            if controller.file is None:
                controller.machines_num = int(inputs[4].get())
        except ValueError:
            pass
        try:
            controller.visual = int(inputs[5].get())
        except ValueError:
            pass
        #root.destroy()
        #insertDataManuallyFrame2(controller)
        if controller.file is not None:
            print("z pliku")
            tkMessageBox.showinfo("", "Click OK to start algorithm")
            r = flowshop.startFromGUI(controller)
            controller.makespanTable = r[0][2]
            controller.time = r[1]
            controller.order = r[0][1]

            controller.minMakespan = r[0][0]
            controller.makespanTable = r[0][2]
            controller.best_iteration = \
                controller.makespanTable.index(controller.minMakespan)

            solutionsTable = []
            solutionsTable.append(controller)
            for i in xrange(len(solutionsTable)):
                print("Zrobilo sie\n")
                make_solutions_visible()
        else:
            make_input_frame_visible()

    def back_button():
        root.destroy()
        inputChooserFrame(controller)
        pass


    buttonApply = Button(parameters_frame, text='Apply', width=button_width, command=next_button,
                    height=button_height, bg = 'grey85')
    buttonApply.grid(row=r, column=1)
    buttonClear = Button(parameters_frame, text='Clear', width=button_width, command=next_button,
                    height=button_height).grid(row=r, column=0)
    parameters_frame.pack(side = LEFT)
####################################
    input_frame = Frame(width=200, height=288)
    def make_go_button_visible():
        def go_now():
            pass

        buttonGo = Button(input_frame, text='Go', width=button_width, command=go_now,
                        height=button_height)
        buttonGo.grid(1,1)
        pass

    def make_input_frame_visible():

        r = 0

        for i in xrange(0, controller.jobs_num):
            lab = Label(input_frame, text='Job #{0} time'.format(str(i)), width=label_width,
                  height=label_height)
            lab.grid(row=r, column=0)
            labelsToHide.append(lab)
            entryTab = []
            for m in range(controller.machines_num):
                T = Entry(input_frame)
                T.config(width=4)
                T.grid(row=r, column=m + 2)
                T.insert(0, str(randint(1,1000)))
                entryTab.append(T)
            inputs22.append(entryTab)
            r = r + 1

        def go_button():
            print(controller.machines_num , "ssssssssssss", controller.jobs_num)
            try:
                for i in range(0, controller.jobs_num):
                    inputsStr = []
                    for i2 in range(controller.machines_num):
                        inputsStr.append(inputs22[i][i2].get())

                    inputsInt = []
                    for ia in range(len(inputsStr)):
                        inputsInt.append(int(inputsStr[ia]))
                    controller.jobs += [inputsInt]
            except ValueError:
                print("VALUE ERROR",controller.jobs)
            print("flowshop startuje z parametrami:")
            print("iteracje: ", controller.iterations)
            print("step: ", controller.step_len)
            print("karaluchy: ", controller.cockroaches_num)
            tkMessageBox.showinfo("", "Click OK to start algorithm")

            r = flowshop.startFromGUI(controller)
            controller.makespanTable = r[0][2]
            controller.time = r[1]
            controller.order = r[0][1]

            controller.minMakespan = r[0][0]
            controller.makespanTable = r[0][2]
            controller.best_iteration = \
                controller.makespanTable.index(controller.minMakespan)

            solutionsTable = []
            solutionsTable.append(controller)
            for i in xrange(len(solutionsTable)):
                print("Zrobilo sie\n")
                make_solutions_visible()


        #def back_button():
            #button.grid(row=r, column=1)

            # root.destroy()
            # insertDataManuallyFrame1(controller)

        buttonGo = Button(input_frame, text='Go', width=button_width, command=go_button,
                        height=button_height)
        buttonGo.grid(row=r, column=0)
        # button.grid_forget()
        # buttonBack = Button(input_frame, text='Back', width=button_width, command=back_button,
        #                  height=button_height)
        # buttonBack.grid(row=r, column=0)
        buttonsToForget.append(buttonGo)
        # buttonsToForget.append(buttonBack)

    input_frame.pack(side = LEFT)

####################################
    solutions_frame = Frame(width=200, height= 289)

#print(list_of_solutions[0].launch_again)

    lab_to_refresh = []
    def make_solutions_visible():
        r = 0 #row

        lab1 = Label(solutions_frame, text="Solutions:", fg="black", font="Verdana 12 bold")
        lab1.grid(row=r, column=0)
        lab_to_refresh.append(lab1)
        controller.file = None

        inputs[3].config(state = "normal")
        inputs[4].config(state = "normal")
        inputs[3].delete(0, END)
        inputs[4].delete(0, END)

        inputs[3].insert(0, controller.jobs_num)
        inputs[4].insert(0, controller.machines_num)





        r += 1
        l= Label(solutions_frame, text="Parameter", fg="black", font="Verdana 10 bold")
        l.grid(row=r, column=0)
        lab_to_refresh.append(l)
        l = Label(solutions_frame, text="Best result", fg="black", font="Verdana 10 bold")
        l.grid(row=r, column=1)
        lab_to_refresh.append(l)

        r+=1
        l = Label(solutions_frame, text="Makespan ", width=label_width, height=label_height)
        l.grid(row=r, column=0)
        lab_to_refresh.append(l)
        lab1 = Label(solutions_frame, text=solution.minMakespan, width=label_width, height=label_height)
        lab1.grid(row=r, column=1)
        lab_to_refresh.append(lab1)

        r += 1
        l = Label(solutions_frame, text="Iteration", width=label_width, height=label_height)
        l.grid(row=r, column=0)
        lab_to_refresh.append(l)

        l= Label(solutions_frame, text=solution.best_iteration, width=label_width, height=label_height)
        l.grid(row=r, column=1)
        lab_to_refresh.append(l)
        r += 1

        time = str(solution.time) + "s"
        l = Label(solutions_frame, text="Execution time", width=label_width, height=label_height)
        l.grid(row=r, column=0)
        lab_to_refresh.append(l)
        l=Label(solutions_frame, text=time, width=label_width, height=label_height)
        l.grid(row=r, column=1)
        lab_to_refresh.append(l)
        r += 1

        l=Label(solutions_frame, text= "NEH", width=label_width, height=label_height)
        l.grid(row=r, column=0)
        lab_to_refresh.append(l)
        nehEnable = "Disable"
        if solution.isNehEnabled:
            nehEnable = "Enable"
        l=Label(solutions_frame, text=nehEnable, width=label_width, height=label_height)
        l.grid(row=r, column=1)
        lab_to_refresh.append(l)

        r += 1
        l= Label(solutions_frame, text= "Order", width=label_width, height=label_height)
        l.grid(row=r, column=0)
        lab_to_refresh.append(l)

        l=Label(solutions_frame, text=solution.order, wraplength=label_width*label_width)
        l.grid(row=r, column=1)
        lab_to_refresh.append(l)

        r += 1

        def again_button():
            root.destroy()
            plt.close()
            controller.launch_again = True
            pass

        def back_button():
            print("Not implemented...")
            pass
        def showPlots():
            plt.plot(solution.makespanTable)
            plt.plot([0, controller.iterations], [controller.upperbound, controller.upperbound], 'r')
            plt.plot([0, controller.iterations], [controller.lowerbound, controller.lowerbound], 'g')
            plt.show()
            #dodac tytul
            pass

        buttonShowPlots = Button(solutions_frame, text='Show Plots', width=button_width, command=showPlots,
                        height=button_height)

        buttonShowPlots.grid(row=r, column=0)
        lab_to_refresh.append(buttonShowPlots)
        r +=1



    solutions_frame.pack(side = LEFT)


####################################
    #other_frame = Frame(width=200, height=500, background="gray50")

   # other_frame.pack(side = LEFT)

    root.mainloop()
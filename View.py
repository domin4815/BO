__author__ = 'domin4815'
from Tkinter import *
import flowshop
#CONFIG
input_width = 26
input_height = 2

button_width = 20
button_height = 2

label_height = 2
label_width = 23


def frame1(controler):
    strings = [
        'Iterations', 'Step len', 'Number of cockroaches',
        'Number of jobs', 'Number of machines'
    ]
    inputs = []
    root = Tk()
    root.title("BO")

    r = 0
    for c in strings:
        Label(root, text=c, width=label_width, height=label_height)
            .grid(row=r, column=0)
        T = Entry(root)
        inputs.append(T)
        T.grid(row=r, column=1)
        r = r + 1

    def next_button():
        try:
            controler.iterations = int(inputs[0].get())
            controler.step_len = int(inputs[1].get())
            controler.cockroaches_num = int(inputs[2].get())
            controler.jobs_num = int(inputs[3].get())
            controler.machines_num = int(inputs[4].get())
        except ValueError:
            print("Value error")
        #controler.print_parameters()
        root.destroy()
        frame2(controler)

    button = Button(root, text='Next', width=button_width, command=next_button,
        height=button_height).grid(row=r, column=0)
    button2 = Button(
        root, text='Next with \ndefault values',
        width=button_width, command=next_button, height=button_height
    ).grid(row=r, column=1)

    mainloop()


def frame2(controler):
    root = Tk()
    root.title("BO")
    inputs = []
    r = 0
    for i in xrange(0, controler.jobs_num):
        Label(root, text='Job #{0} time'.format(str(i+1)), width=label_width,
            height=label_height).grid(row=r,column=0)
        T = Entry(root)
        T.insert(0, str(i+7))
        inputs.append(T)
        T.grid(row=r, column=1)
        r = r + 1

    def go_button():
        try:
            for i in range(0, controler.jobs_num):
                controler.jobs += [int(inputs[i].get())]
        except ValueError:
            print("Value error")
        root.destroy()
        flowshop.run_cockroaches(
            controler.iterations, controler.step_len,
            controler.cockroaches_num, controler.jobs_num,
            controler.machines_num,
            controler.jobs
        )

    def back_button():
        root.destroy()
        frame1(controler)

    button = Button(root, text='Go', width=button_width, command=go_button,
        height=button_height).grid(row=r, column=1)
    button2 = Button(root, text='Back', width=button_width, command=back_button,
        height=button_height).grid(row=r, column=0)

    mainloop()

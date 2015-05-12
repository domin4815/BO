import re
import flowshop
import View

__author__ = 'domin4815'
def parseFileAndRun(controller):
    isNehEnabled = controller.isNehEnabled
    file = controller.file
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
            print("flowshop startuje z parametrami:")
            print("iteracje: ", controller.iterations)
            print("step: ", controller.step_len)
            print("karaluchy: ", controller.cockroaches_num)
            startFlowshop(controller, isNehEnabled)
    except IndexError:
        pass


def startFlowshop(controller, isNehEnabled):
    flowshop.startFromGUI(controller, isNehEnabled)


class ProgramController(object):

    def __init__(self, iterations, step, cs, jobs, mach, jobsTab):
        self.iterations = iterations
        self.step_len = step
        self.cockroaches_num = cs
        self.jobs_num = jobs
        self.machines_num = mach
        self.jobs = jobsTab
        self.file = None
        self.isNehEnabled = False

    def print_parameters(self):
        print(self.iterations, self.step_len, self.cockroaches_num,
            self.jobs_num, self.machines_num, self.jobs_num)

if __name__ == '__main__':
    controller = ProgramController(0,0,0,0,0,[])
    View.inputChooserFrame(controller)
    parseFileAndRun(controller)



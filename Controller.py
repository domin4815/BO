import re
import flowshop
import View
import pylab

__author__ = 'domin4815'
class ProgramController(object):

    def __init__(self, iterations, step, cs, jobs, mach, jobsTab):
        #input
        self.iterations = iterations
        self.step_len = step
        self.cockroaches_num = cs
        self.jobs_num = jobs
        self.machines_num = mach
        self.jobs = jobsTab
        self.file = None
        self.isNehEnabled = False
        #other parameters
        self.showDinamicallyGraph = None
        #solution
        self.makespanTable = []
        self.time = None
        self.order = []
        self.minMakespan = None

    def print_parameters(self):
        print(self.iterations, self.step_len, self.cockroaches_num,
            self.jobs_num, self.machines_num, self.jobs_num)


def parseFileAndRun(controller):
    file = controller.file
    print("Parsing input data...")
    pattern = re.compile(r'([0-9]+)')
    solutionsTable = []
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
            r = flowshop.startFromGUI(controller)
            #robie nowy tylko do podawania ezultatu obliczen
            solutionKeeperControler = ProgramController(controller.iterations,controller.step_len,
                                                        controller.cockroaches_num,controller.jobs_num,
                                                        controller.machines_num,jobsTab)
            solutionKeeperControler.isNehEnabled = controller.isNehEnabled
            solutionKeeperControler.minMakespan = r[0][0]
            solutionKeeperControler.makespanTable = r[0][2]
            solutionKeeperControler.time = r[1]
            solutionKeeperControler.order = r[0][1]
            solutionsTable.append(solutionKeeperControler)

    except IndexError:
        pass
    View.presentSolutionsFrame(solutionsTable)
    pass







if __name__ == '__main__':
    controller = ProgramController(100,4,30,20,5,[])
    View.inputChooserFrame(controller)
    if(controller.file != None):
        parseFileAndRun(controller)
    else:
        r = flowshop.startFromGUI(controller)
        controller.makespanTable = r[0][2]
        controller.time = r[1]
        controller.order = r[0][1]





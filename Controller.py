import View

__author__ = 'domin4815'


class ProgramController:

    def __init__(self, iterations, step, cs, jobs, mach, jobsTab):
        self.iterations = iterations
        self.stepLen = step
        self.cockroachesNum = cs
        self.jobsNum = jobs
        self.machinesNum = mach
        self.jobs = jobsTab

    def printParameters(self):
        print(self.iterations, self.stepLen, self.cockroachesNum, self.jobsNum, self.machinesNum, self.jobsNum)

if __name__ == '__main__':
    View.frame1(ProgramController(10,10,10,10,10,[]))

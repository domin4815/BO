__author__ = 'domin4815'
class ProgramParametersManager:

    def __init__(self, iterations, step, cs, jobs, mach, jobsTab):
        self.iterations = iterations
        self.stepLen = step
        self.cockroachesNum = cs
        self.jobsNum = jobs
        self.machinesNum = mach
        self.jobs = jobsTab

    def printParameters(self):
        print(self.iterations, self.stepLen, self.cockroachesNum, self.jobsNum, self.machinesNum, self.jobsNum)





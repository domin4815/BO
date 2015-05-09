import View

__author__ = 'domin4815'


class ProgramController(object):

    def __init__(self, iterations, step, cs, jobs, mach, jobsTab):
        self.iterations = iterations
        self.step_len = step
        self.cockroaches_num = cs
        self.jobs_num = jobs
        self.machines_num = mach
        self.jobs = jobsTab

    def print_parameters(self):
        print(self.iterations, self.step_len, self.cockroaches_num,
            self.jobs_num, self.machines_num, self.jobs_num)

if __name__ == '__main__':
    View.inputChooserFrame(ProgramController(0,0,0,0,0,[]))

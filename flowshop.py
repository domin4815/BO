from random import shuffle, randint, uniform
from math import exp
import pprint
import datetime
import neh
import Controller
import matplotlib.pyplot as plt
import numpy
import time
import distance

def calculate_cost(jobs, state):
    cost = [[] for i in xrange(len(jobs))]

    for i, id in enumerate(state):
        job = jobs[id]
        for j in xrange(len(job)):
            up = cost[i-1][j] if i > 0 else 0
            left = cost[i][j-1] if j > 0 else 0
            cost[i].append(job[j] + max(left, up))

    return cost[len(state) - 1][len(jobs[0]) - 1]


def step(a, b):
    for i in xrange(len(a)):
        if a[i] != b[i]:
            j = a.index(b[i])
            a[i], a[j] = a[j], a[i]
            return


def swarm(jobs, states, steps, optimal_cost, optimal_state, visual):
    change = False
    for i, state_i in enumerate(states):
        optimal_state_local = state_i[:]
        optimal_cost_local = calculate_cost(jobs, state_i)
        for j, state_j in enumerate(states):
            if distance.hamming(state_i, state_j) <= visual:
                cost_i = calculate_cost(jobs, state_i)
                cost_j = calculate_cost(jobs, state_j)
                if cost_j < cost_i:
                    for s in xrange(randint(0, steps)):
                        step(state_i, state_j)
                        cost = calculate_cost(jobs, state_i)
                        if cost < optimal_cost_local:
                            optimal_cost_local, optimal_state_local = cost, state_i[:]
            if state_i == optimal_state_local:
                step(state_i, optimal_state)
                cost = calculate_cost(jobs, state_i)
                if cost < optimal_cost:
                    optimal_cost, optimal_state = cost, state_i[:]
                    change = True
    return optimal_cost, change


def disperse(states, jobs, optimal_cost, optimal_state):
    change = False
    for i, state in enumerate(states):
        rand = range(len(jobs))
        shuffle(rand)
        step(state, rand)
        cost = calculate_cost(jobs, state)
        if cost < optimal_cost:
            optimal_cost, optimal_state = cost, state[:]
            change = True
    return optimal_cost, change


def ruthless(states, optimal_state):
    index = randint(0, len(states) - 1)
    states[index] = optimal_state[:]


def acceptance(cost, optimal_cost, iteration):
    return 1.0 if cost < optimal_cost else exp((optimal_cost - cost) / iteration)


def cockroach(iterations, steps, cockroach_count, job_count, machine_count, jobTimes, isNehEnabled, showDynamicallyGraph, controller):
    jobs = {}
    states = []
    optimal_state = []
    optimal_cost = 999999999999999999
    optimals = []
    visual = 10

    # print('Times:')
    if jobTimes is None:
        for i in xrange(job_count):
            times = map(lambda x: int(x), raw_input().split(' ')[:machine_count])
            jobs[i] = times
            #jobs[i] = [jobTimes[i]]
    else:
        for i in xrange(job_count):
            #jobs[i] = times
            jobs[i] = jobTimes[i]

    print(jobs)

    if isNehEnabled == False:
        for i in xrange(cockroach_count):
            state = range(job_count)
            shuffle(state)
            states.append(state)
            cost = calculate_cost(jobs, state)
            # print(cost, state)
            if cost < optimal_cost:
                optimal_cost, optimal_state = cost, state[:]
    else:
        neh_result_state = neh.neh(jobs)
        states.append(neh_result_state)
        cost = calculate_cost(jobs, neh_result_state)

        print "Neh makespan and state: (", cost, "), ", neh_result_state

        if cost < optimal_cost:
            optimal_cost, optimal_state = cost, neh_result_state[:]

        for i in xrange(1, cockroach_count):
            state = range(job_count)
            shuffle(state)
            states.append(state)
            cost = calculate_cost(jobs, state)
            # print(cost, state)
            if cost < optimal_cost:
                optimal_cost, optimal_state = cost, state[:]

    print(optimal_cost, optimal_state)

    counter = 0
    makespan_table = []
    xData = []
    yData = []
    plt.ion()
    if showDynamicallyGraph: #na szybko ten if
        fig = plt.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot([], [],'-k',label='black')
        plt.plot([0, controller.iterations], [controller.upperbound, controller.upperbound], 'r')
        plt.plot([0, controller.iterations], [controller.lowerbound, controller.lowerbound], 'g')
        plt.xlim([0, controller.iterations])

    threshold = iterations / randint(2, 10)

    for i in xrange(iterations):
        yData.append(optimal_cost)
        xData.append(i)
        if showDynamicallyGraph:
           #dynamicznie rysowany wykres 1
            line1.set_ydata(yData)
            line1.set_xdata(range(len(yData)))
            ax.relim()
            ax.autoscale_view()
            plt.draw()

        print optimal_cost
        makespan_table.append(optimal_cost)
        optimal_cost, change_s = swarm(jobs, states, steps, optimal_cost, optimal_state, visual)
        optimal_cost, change_d = disperse(states, jobs, optimal_cost, optimal_state)

        if not change_s and not change_d:
            counter += 1
            if counter > threshold:
                a = randint(0, len(optimal_state) - 1)
                b = randint(0, len(optimal_state) - 1)
                new_state = optimal_state[:]
                new_state[a], new_state[b] = new_state[b], new_state[a]
                new_cost = calculate_cost(jobs, new_state)
                if acceptance(new_cost, optimal_cost, i) > uniform(0, 1):
                    optimals.append((optimal_cost, optimal_state[:]))
                    optimal_state, optimal_cost = new_state[:], new_cost
                    counter = 0
        else:
            counter = 0

        ruthless(states, optimal_state)

    for i in optimals:
        if i[0] < optimal_cost:
            optimal_cost, optimal_state = i
    return (optimal_cost, optimal_state, makespan_table)


def startFromGUI(controller):
    dat1 = datetime.datetime.now()
    print("JobTimes: ")
    print(controller.jobs)

    if (controller.isNehEnabled == True):
        print "Running with NEH"
        r = []
        r = cockroach(
        controller.iterations, controller.step_len, controller.cockroaches_num, controller.jobs_num,
        controller.machines_num, jobTimes=controller.jobs,isNehEnabled=controller.isNehEnabled,
        showDynamicallyGraph=controller.showDinamicallyGraph, controller = controller
        )
    else:
        r = cockroach(
        controller.iterations, controller.step_len, controller.cockroaches_num, controller.jobs_num,
        controller.machines_num, jobTimes=controller.jobs, isNehEnabled=controller.isNehEnabled,
        showDynamicallyGraph=controller.showDinamicallyGraph, controller=controller
        )

    dat2 = datetime.datetime.now()
    execution_time = (dat2-dat1).total_seconds()
    print(r[0], r[1])
    #print(r)

    return r, execution_time



def run_cockroaches(iterations, steps, cockroach_count, job_count,
    machine_count, job_times):
    job_times = neh.neh(job_times)
    r = cockroach(iterations, steps, cockroach_count, job_count, machine_count,
        job_times, True, False)
    print(r[0], r[1])


if __name__ == '__main__':
    print("Insert data")
    iterations = input()#'Iterations: ')
    steps = input()#'Step length: ')
    cockroach_count = input()#'Number of cockroaches: ')
    job_count = input()#'Number of jobs: ')
    machine_count = input()#'Number of machines: ')
    dat1 = datetime.datetime.now()
    r = cockroach(
        iterations, steps, cockroach_count, job_count, machine_count,
        None, True, False
    )
    dat2 = datetime.datetime.now()
    print(dat2-dat1)

    print(r[0], r[1])

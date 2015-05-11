from random import shuffle, randint
import pprint
import datetime
import neh
import Controller


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


def swarm(jobs, states, steps, optimal_cost, optimal_state):
    change = False
    for i, state_i in enumerate(states):
        for j, state_j in enumerate(states):
            cost_i = calculate_cost(jobs, state_i)
            cost_j = calculate_cost(jobs, state_j)
            if cost_j < cost_i:
                for s in xrange(randint(0, steps)):
                    step(state_i, state_j)
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
        for s in xrange(randint(1, 2)):
            step(state, rand)
            cost = calculate_cost(jobs, state)
            if cost < optimal_cost:
                optimal_cost, optimal_state = cost, state[:]
                change = True
    return optimal_cost, change


def ruthless(states, optimal_state):
    index = randint(0, len(states) - 1)
    states[index] = optimal_state[:]


def cockroach(iterations, steps, cockroach_count, job_count, machine_count, jobTimes, isNehEnabled):
    jobs = {}
    states = []
    optimal_state = []
    optimal_cost = 999999999999999999
    optimals = []

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

    for i in xrange(iterations):
        print optimal_cost
        optimal_cost, change_s = swarm(jobs, states, steps, optimal_cost, optimal_state)
        optimal_cost, change_d = disperse(states, jobs, optimal_cost, optimal_state)

        if not change_s and not change_d:
            counter += 1
            if counter > 300:
                optimals.append((optimal_cost, optimal_state[:]))
                a = randint(0, len(optimal_state) - 1)
                b = randint(0, len(optimal_state) - 1)
                optimal_state[a], optimal_state[b] = optimal_state[b], optimal_state[a]
                optimal_cost = calculate_cost(jobs, optimal_state)
                counter = 0
        else:
            counter = 0

        ruthless(states, optimal_state)

    for i in optimals:
        if i[0] < optimal_cost:
            optimal_cost, optimal_state = i

    return (optimal_cost, optimal_state)


def run_cockroaches(iterations, steps, cockroach_count, job_count,
    machine_count, job_times):
    job_times = neh.neh(job_times)
    r = cockroach(iterations, steps, cockroach_count, job_count, machine_count,
        job_times)
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
        None, True
    )
    dat2 = datetime.datetime.now()
    print(dat2-dat1)

    print(r[0], r[1])

def startFromGUI(controller, isNehEnabled):
    dat1 = datetime.datetime.now()
    print("JobTimes: ")
    print(controller.jobs)

    if (isNehEnabled == True):
        print "Running with NEH"

        r = cockroach(
        controller.iterations, controller.step_len, controller.cockroaches_num, controller.jobs_num,
        controller.machines_num, jobTimes=controller.jobs, isNehEnabled = isNehEnabled
        )
    else:
        r = cockroach(
        controller.iterations, controller.step_len, controller.cockroaches_num, controller.jobs_num,
        controller.machines_num, jobTimes=controller.jobs, isNehEnabled = isNehEnabled
        )

    dat2 = datetime.datetime.now()
    print(dat2-dat1)

    print(r[0], r[1])

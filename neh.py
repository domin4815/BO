import operator

def calculate_cost(jobs, state):
    cost = [[] for i in xrange(len(jobs))]

    for i, id in enumerate(state):
        job = jobs[id]
        for j in xrange(len(job)):
            up = cost[i-1][j] if i > 0 else 0
            left = cost[i][j-1] if j > 0 else 0
            cost[i].append(job[j] + max(left, up))

    return cost[len(state) - 1][len(jobs[state[0]]) - 1]

# Step 1: Order the jobs by non-increasing sums of processing times on the machines
# Return: sorted states descending
def sort_jobs(jobs):
    job_sum = {}

    for i in xrange(len(jobs)):
        job_sum[i] = sum(jobs[i])

    sorted_array = sorted(
        job_sum.items(), key=operator.itemgetter(1), reverse=True
    )
    sorted_states = [x[0] for x in sorted_array]

    return sorted_states

def schedule_jobs(jobs, sorted_state):
    optimal_state = []

    #Step 2: Take the first two jobs and schedule them in order to minimise the partial makespan as if there were only these two jobs
    selected_jobs = {}
    selected_jobs[sorted_state[0]] = jobs[sorted_state[0]]
    selected_jobs[sorted_state[1]] = jobs[sorted_state[1]]

    if calculate_cost(selected_jobs, [sorted_state[0], sorted_state[1]]) < \
        calculate_cost(selected_jobs, [sorted_state[1], sorted_state[0]]):
        optimal_state.append(sorted_state[0])
        optimal_state.append(sorted_state[1])
    else:
        optimal_state.append(sorted_state[1])
        optimal_state.append(sorted_state[0])

    #Step 3: For i = 2 to n do Step 4
    for i in xrange(2, len(sorted_state)):
        #Step 4: Insert the i-th job at the place, which minimises the partial makespan among the i-possible ones.
        selected_jobs[sorted_state[i]] = jobs[sorted_state[i]]
        min_makespan = 99999999999

        for j in xrange(len(selected_jobs)):
            tmp_state = optimal_state
            tmp_state.insert(j, sorted_state[i])

            if calculate_cost(selected_jobs, tmp_state) < min_makespan:
                min_makespan = calculate_cost(selected_jobs, tmp_state)
                tmp_optimal_state = tmp_state[:]

            tmp_state.pop(j)

        #Increase size of optimal_state list
        optimal_state.append(999)
        optimal_state = tmp_optimal_state[:]

    return optimal_state

def neh(jobs):
    sorted_state = sort_jobs(jobs)
    return schedule_jobs(jobs, sorted_state)

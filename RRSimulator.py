import numpy as np
import matplotlib.pyplot as plt
import copy


def return_set_list():
    numProcesses = 40
    processes = []
    for x in range(numProcesses):
        processes.append(np.random.normal(8, 3))
    # (wait time, num rotations, execution time left)
    tripple = [[0, 0, x] for x in processes]
    return tripple


def simulator():

    quantumRange = 40
    tripple = return_set_list()
    
    durations = [None] * quantumRange
    waitTime = [None] * quantumRange
    overHead = [None] * quantumRange
    contextSwitchTime = 5
    
    for q in range(1, quantumRange):

        triCopy = copy.deepcopy(tripple)
        outstandingProcesses = len(triCopy)

        switchTime = 0
        timeCounter = 0
        pos = 0
        removed = []

        while outstandingProcesses > 0:
            n = triCopy[pos]
            if n not in removed:
                n[0] += (timeCounter - (n[1] * q))
                n[1] += 1
                n[2] = (n[2] - q)
                timeCounter += (q + contextSwitchTime)
                switchTime += q
                if n[2] <= 0:
                    removed.append(n)
                    outstandingProcesses -= 1
 
            pos += 1
            if pos == len(triCopy):
                pos = 0
        
        waitTime[q] = 0
        for x in removed:
            waitTime[q] += (x[0] / len(removed))

        durations[q] = timeCounter
        overHead[q] = switchTime / timeCounter

    fig, ax = plt.subplots()
    ax.plot(range(quantumRange), waitTime, color='tab:blue', label='Avg wait time')
    ax.plot(range(quantumRange), durations, color='tab:orange', label='Duration')
    #ax.plot(range(quantumRange), overHead, color='tab:red', label='Over head')
    ax.set_ylabel("Time")
    ax.set_xlabel("Quantum size")
    ax.set_title('Duration and wait time, 40 processes, \n mean burst size of 8ms, context switch time 5ms')
    ax.legend()
    plt.show()

simulator()
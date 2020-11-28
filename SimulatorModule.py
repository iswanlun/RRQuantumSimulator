import copy
import numpy as np

class simModule:
    def __init__(self):
        pass

    def return_set_list(self, mean, std):
        numProcesses = 40
        processes = []
        for x in range(numProcesses):
            processes.append(np.random.normal(mean, std))
        # (wait time, num rotations, execution time left)
        return [[0, 0, x] for x in processes]

    def simulator(self, mean, std, switch):

        quantumRange = 40
        tripple = self.return_set_list(mean, std)
        
        durations = [None] * quantumRange
        waitTime = [None] * quantumRange
        overHead = [None] * quantumRange
        contextSwitchTime = switch
        
        for q in range(1, quantumRange):

            triCopy = copy.deepcopy(tripple)
            outstandingProcesses = len(triCopy)
            
            timeCounter = 0
            pos = 0
            switchTime = 0
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

        toReturn = [waitTime[1],1,durations[1],1,overHead[1],1]

        for x in range(2,len(waitTime)):
            if waitTime[x] < toReturn[0]:
                toReturn[0] = waitTime[x]
                toReturn[1] = x
        
        for x in range(2,len(durations)):
            if durations[x] < toReturn[2]:
                toReturn[2] = durations[x]
                toReturn[3] = x
        
        for x in range(2,len(overHead)):
            if overHead[x] < toReturn[4]:
                toReturn[4] = overHead[x]
                toReturn[5] = x

        #[min wait, quantum, min duration , quantum, minOverhead, quanturm]

        return toReturn



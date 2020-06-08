import matplotlib.pyplot as plt
from GenerateInput import InputGenerator
from NearestNeighbor import NearestNeighbor
from BruteForce import BruteForce
from NearestInsertion import NearestInsertion
import numpy as np
import time
from textwrap import wrap
from two_opt import Two_Opt
def fitParobola(x, y):
    a = np.polyfit(x, y, 2)
    return np.poly1d(a)

def analyze(bfFlag=False):
    runTimeStat = {
        "nn": [],
        "bf": [],
        "ni": [],
        "to": []
    }

    solutionStat = {
        "nn": [],
        "bf": [],
        "ni": [],
        "to": []
    }

    maxSize = 500
    if bfFlag:
        maxSize = 12
    '''
    Running experiences ....
    '''
    for size in range(3, maxSize):
        inputGen = InputGenerator(size, maxSize * 2, maxSize * 2)
        inputs = inputGen.generate()

        nn = NearestNeighbor(inputs)
        startTime = time.time()
        nnpath, nntotalDistance = nn.optimise()
        runTime = time.time() - startTime
        runTimeStat["nn"].append(runTime)
        solutionStat["nn"].append(nntotalDistance)

        if bfFlag:
            bf = BruteForce(inputs)
            startTime = time.time()
            bfpath, bftotalDistance = bf.optimise()
            runTime = time.time() - startTime
            runTimeStat["bf"].append(runTime)
            solutionStat["bf"].append(bftotalDistance)

        ni = NearestInsertion(inputs)
        startTime = time.time()
        nipath, nitotalDistance = ni.optimise()
        runTime = time.time() - startTime
        runTimeStat["ni"].append(runTime)
        solutionStat["ni"].append(nitotalDistance)

        to = Two_Opt(inputs)
        startTime = time.time()
        topath, tototalDistance = to.optimise()
        runTime = time.time() - startTime
        runTimeStat["to"].append(runTime)
        solutionStat["to"].append(tototalDistance)

    '''
    Plotting the results
    '''
    x = np.arange(3, maxSize)
    if not bfFlag:
        fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(12, 12), squeeze=False)

        ax[0][0].plot(x, runTimeStat["nn"], '-b', label="NN runtime")
        ax[0][0].plot(x, fitParobola(x, runTimeStat["nn"])(x), '--m', label="Fitting parabola")
        ax[0][0].set_title(title("Runtime of Nearest Neighbor vs fitting parabola"))
        ax[0][0].set_xlabel("Number of nodes")
        ax[0][0].set_ylabel("seconds")
        ax[0][0].legend()

        ax[0][1].plot(x, runTimeStat["ni"], '-r', label="NN runtime")
        ax[0][1].plot(x, fitParobola(x, runTimeStat["ni"])(x), '--m', label="Fitting parabola")
        ax[0][1].set_title(title("Runtime of Nearest Insertion vs fitting parabola"))
        ax[0][1].set_xlabel("Number of nodes")
        ax[0][1].set_ylabel("seconds")
        ax[0][1].legend()

        ax[0][2].plot(x, runTimeStat["to"], '-g', label="2-Opt runtime")
        ax[0][2].plot(x, fitParobola(x, runTimeStat["to"])(x), '--m', label="Fitting parabola")
        ax[0][2].set_title(title("Runtime of 2-Opt vs fitting parabola"))
        ax[0][2].set_xlabel("Number of nodes")
        ax[0][2].set_ylabel("seconds")
        ax[0][2].legend()

        ax[1][1].plot(x, runTimeStat["nn"], '-b', label="NN runtime")
        ax[1][1].plot(x, runTimeStat["ni"], '-r', label="NI runtime")
        ax[1][1].plot(x, runTimeStat["to"], '-g', label="2-opt runtime")

        ax[1][1].set_title(title("Runtime Comparison"))
        ax[1][1].set_xlabel("Number of nodes")
        ax[1][1].set_ylabel("seconds")
        ax[1][1].legend()

        fig.delaxes(ax.flatten()[5])
        fig.delaxes(ax.flatten()[3])
        plt.tight_layout(True)
        plt.savefig("runtime_woBF.png", dpi=800)
        plt.close()
    else:
        fig, ax = plt.subplots()
        ax.plot(x, runTimeStat["nn"], '-b', label="NN runtime")
        ax.plot(x, runTimeStat["ni"], '-r', label="NI runtime")
        ax.plot(x, runTimeStat["to"], '-g', label="2-opt runtime")
        ax.plot(x, runTimeStat["bf"], '--k', label="Brute Force runtime")

        ax.set_title(title("Runtime Comparison"))
        ax.set_xlabel("Number of nodes")
        ax.set_ylabel("seconds")
        ax.legend()
        plt.tight_layout(True)
        plt.savefig("runtime_wBF.png", dpi=800)
        plt.close()
    fig, ax = plt.subplots()
    ax.plot(x, solutionStat["nn"], '-b', label="NN solution")
    ax.plot(x, solutionStat["ni"], '-r', label="NI solution")
    ax.plot(x, solutionStat["to"], '-g', label="2-opt solution")
    if bfFlag:
        ax.plot(x, solutionStat["bf"], '--k', label="Brute Force solution")

    ax.set_title("Total Distance Comparison")
    ax.set_xlabel("Number of nodes")
    ax.set_ylabel("Distance")
    ax.legend()
    plt.tight_layout(True)
    if bfFlag:
        plt.savefig("solution_wBF.png", dpi=800)
    else:
        plt.savefig("solution_woBF.png", dpi=800)
    plt.close()


def example():
    size = 10
    maxSize = 20
    inputGen = InputGenerator(size, maxSize * 2, maxSize * 2)
    inputs = inputGen.generate()

    bf = BruteForce(inputs)
    bfpath, bftotalDistance = bf.optimise()
    bf.plotPath(name="Brute_Force")

    nn = NearestNeighbor(inputs)
    nnpath, nntotalDistance = nn.optimise()
    nn.plotPath(name="NN")

    ni = NearestInsertion(inputs)
    nipath, nitotalDistance = ni.optimise()
    ni.plotPath(name="NI")

    to = Two_Opt(inputs)
    topath, tototalDistance = to.optimise()
    to.plotPath(name="2-opt")


def title(text):
    return "\n".join(wrap(text,30))

def main():
    #this generates the example result of 4 algorithms for the input of size 10
    print("Running example ....")
    example()

    # This will generate the comparison of runtimes and solutions between 4 algorithms
    # in the input of size varying from 3 to 12.
    print("Running analyze 1 ....")
    analyze(True)

    # # This will generate the comparison of runtimes and solutions between 3 algorithms: NN, NI, and 2-opt
    # in the input of size varying from 3 to 12.
    print("Running analyze 2 ....")
    analyze()

if __name__ == '__main__':
    main()
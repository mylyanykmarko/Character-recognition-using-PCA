import numpy
from numpy import linalg


def ev_and_evc(S):
    S = numpy.array(S)
    ev, evc = linalg.eig(S)
    evalues = [i for i in ev]
    evectors = [[num for num in evc[lst]] for lst in range(len(evc))]
    return [evalues, evectors]

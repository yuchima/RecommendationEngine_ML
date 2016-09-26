import numpy as np

#                   1    2    3    4    5    6    7    8    9    10
data = [ np.array([0.0, 2.0, 3.0, 0.0, 5.0, 0.0, 4.0, 1.0, 3.0, 0.0]),
         np.array([2.0, 3.0, 1.0, 5.0, 3.0, 0.0, 2.0, 4.0, 4.0, 4.0]),
         np.array([1.0, 0.0, 2.0, 4.0, 2.0, 5.0, 0.0, 2.0, 4.0, 5.0]),
         np.array([1.0, 2.0, 3.0, 0.0, 0.0, 4.0, 2.0, 1.0, 0.0, 5.0]),
         np.array([5.0, 5.0, 5.0, 5.0, 0.0, 1.0, 1.0, 5.0, 1.0, 5.0])
]

def dis(x,y, data):
    z = np.zeros(len(data[0]))
    for i in xrange(len(z)):
        if x[i] == 0 or y[i] == 0:
            z[i] = 0
        else:
            z[i] = x[i] - y[i]
    r = np.linalg.norm(z)
    if r == 0.0:
        return r
    else:
        return 1/r

def score(data,person):
    for i in xrange(len(person)):
        totals = 0
        sims = 0
        if person[i] == 0.0 :
            for other in data:
                sim = dis(other,person,data)
                total = other[i]*sim
                print 'sim=',sim,',other=',other[i],',total=',total
                totals+= total
                if other[i] != 0.0:
                    sims+= sim
            totals = totals/sims
        print 'i=',i+1,'totals=',totals

print score(data,data[3])


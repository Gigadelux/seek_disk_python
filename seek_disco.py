from enum import Enum

import matplotlib.pyplot as plt

class HDDalgorithm(Enum):
    FCFS = 0
    SSTF = 1
    SCAN = 2
    LOOK = 3
    C_SCAN = 4
    C_LOOK = 5

def values(size, maxRange, algorithm): #FcFs default
    values = []
    points = []
    for i in range(size):
        valueI = int(input(f"insert value {i} :"))
        if(valueI<maxRange[0] or valueI>maxRange[1]):
            raise exec(AttributeError) #values between 0 and 999
        values.append(valueI)
    if(algorithm == HDDalgorithm.SSTF):
        return SSTF(values)
    if(algorithm == HDDalgorithm.LOOK):
        return look(values)
    #FCFS: Default
    k = 0
    for i in range(1,size):
        k+=100
        points.append([values[i-1],values[i],k,k+100])
    return points

def SSTF(values:list): #Starting from the first point, make the greatest and the minors lists and sort them
    sorted = values.copy()
    m = minors(sorted, sorted[0])
    m.sort()
    g = greatest(sorted, sorted[0])
    g.sort()
    points = []
    k=0
    i,j = 0,0
    toComp = sorted[0]
    while i< len(m) and j< len(g):
        if(dis(toComp,g[j])>dis(toComp,m[i])):
            points.append([toComp, m[i], k, k+100])
            toComp = m[i]
            i+=1
        else:
            points.append([toComp, g[j], k, k+100])
            toComp = g[j]
            j+=1
        k += 100
    while i < len(m):
        points.append([toComp, m[i], k, k + 100])
        toComp = m[i]
        i += 1
        k+=100
    while j< len(g):
        points.append([toComp, g[j], k, k + 100])
        toComp = g[j]
        j += 1
        k+=100
    return points

def look(values):
    sorted = values.copy()
    m = minors(sorted, sorted[0])
    m.sort()
    m.reverse()
    g = greatest(sorted, sorted[0])
    g.sort()
    points = []
    k = 0
    toComp = sorted[0]
    for i in g:
        points.append([toComp,i,k,k+100])
        toComp=i
        k+=100
    for j in m:
        points.append([toComp,j,k,k+100])
        toComp=j
        k+=100
    return points

def greatest(l:list, bound):
    return [i for i in l if i>bound]

def minors(l:list, bound):
    return [i for i in l if i<bound]

def dis(num1, num2):
    return module(num2-num1)

def module(num):
    if num>=0:
        return num
    else:
        return -num

if __name__ == '__main__':
    points = values(9, (0,999),HDDalgorithm.SSTF)
    for i in points:
        plt.scatter(i[:2],[i[2], i[3]])
        plt.plot(i[:2],[i[2], i[3]], color="blue")
    # Plotting the line segment
    plt.plot(0, 999, color='blue')
    print("made in japan")
    # Adding labels and title
    plt.xlabel('Cilinders')
    plt.ylabel('Y-axis')
    plt.title('HDD algorithms requests')

    # Display the plot
    plt.show()

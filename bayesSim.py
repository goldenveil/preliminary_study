import random
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))
    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

def sample(count):
    sample_list = []
    for i in range(1,count+1):
        a = random_index([30,70])
        sample_list.append(a)
    return sample_list

def count_1(sample_list,start,end):
    c = 0
    tmp = []
    for i,d in enumerate(sample_list):
        if i >= start and i < end:
            tmp.append(d)
    for d in tmp:
        if d == 1:
            c = c+1
    return c

def plot_beta(ab_pairs):
    x = np.linspace(0, 1, 1002)[1:-1]
    for a, b in ab_pairs:
        print(a, b)
        dist = beta(a, b)
        y = dist.pdf(x)
        plt.plot(x, y, label=r'$\alpha=%.1f,\ \beta=%.1f$' % (a, b))
    plt.title(u'Beta Distribution')
    plt.xlim(0, 1)
    plt.ylim(0,60)
    plt.legend()
    plt.savefig("./beta.svg", format="svg")

def theta(sample_list):
    alpha = 1
    beta = 1
    n = 0
    q = 0
    ab_pairs = []
    theta_list = []
    for i in range(1,len(sample_list)+1):
        if i < 1000:
            n = i
            q = count_1(sample_list,0,n)
        else:
            n = 1000
            q = count_1(sample_list,i-n,i)
        alpha = alpha+q
        beta = beta+n-q
        t = (alpha)/(alpha+beta)
        print(t,end="  ")
        if i%20 == 0:
            print()
        theta_list.append(t)
        if i == 10 or i == 20 or i ==50 or i==100:
            ab_pairs.append((alpha,beta))
    return theta_list,ab_pairs

def plot_theta(theta_list):
    plt.figure()
    x = np.linspace(0, 10001, 10002)[1:-1]
    y = []
    for t in theta_list:
        y.append(t)
    plt.plot(x, y)
    plt.title('Theta value per moment')
    plt.xlim(0, 10002)
    plt.ylim(0, 1)
    plt.legend()
    plt.show()

sample_list = sample(10000)
theta_list,abpairs = theta(sample_list)
plot_beta(abpairs)
plot_theta(theta_list)


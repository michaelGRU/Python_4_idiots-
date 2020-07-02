import numpy as np
from matplotlib import pyplot as plt
from collections import defaultdict
plt.xkcd()
df = np.repeat(1/6,6)
data = np.convolve(df,df,mode = "full")
x = np.arange(2,13)
#plt.bar(x,data)
# plt.show()

def roll():
    '''
    # count = 1000
    # result = defaultdict(int)
    # for num in range(count):
    # dice1 = np.random.randint(1,7,count)
    # dice2 = np.random.randint(1,7,count)
    #     sum = np.add(dice1,dice2)
    #     result[np.add(dice1,dice2)] += 1
    # plt.bar(result.keys(), result.values())
    # plt.show()
    '''
    pass
x = np.arange(10,61)
pdf = np.repeat(1/6,6)
pdf10 = pdf
for num in range (10-1):
    pdf10 = np.convolve(pdf10,pdf)
plt.bar(x/10,pdf10)
plt.tight_layout()
plt.show()

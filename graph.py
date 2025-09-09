# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 10:55:45 2025

@author: Nishu
"""
import statistics
import matplotlib.pyplot as plt
Estimates=[576, 890, 441 ,841, 383, 980, 815, 48, 803, 793, 120, 726, 417, 414, 494, 970, 699, 731, 949, 948, 406, 556, 154, 495, 656, 790, 492, 411, 24, 845, 242, 509, 725, 159, 60, 676, 820, 864, 56, 737, 404, 347, 459, 627, 384, 597, 579, 97, 339, 319, 396, 929, 888, 892, 408, 688, 167, 761, 554, 273, 134, 244, 500, 431, 780, 561, 637, 684, 501, 622, 685, 532, 789, 998, 271]
Estimates.sort()
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]

y=[]
for i in range(len(Estimates)):
    y.append(5)

plt.plot(Estimates,y,'r--,')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.plot([375],[5],'g^')
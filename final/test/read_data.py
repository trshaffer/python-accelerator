#!/usr/bin/env python3
import sys
import os
import matplotlib.pyplot as plt

time_averages=[0,0,0,0,0,0,0,0,0,0,0]
time_averages_bad=[0,0,0,0,0,0,0,0,0,0,0]
times=dict()
times_bad=dict()
for i in range(1, 11):
    lib = "lib"
    if i < 10:
        lib=lib+"0"+str(i)
    else:
        lib=lib+str(i)
    for x in range(0,100):
        f = open("./"+lib+"_result/"+str(x)+".txt", "r")
        f_bad = open("./"+lib+"_bad_result/"+str(x)+".txt", "r")
        line = f.readline().strip().split()
        line_bad = f_bad.readline().strip().split()
        time_averages[i-1]+=float(line[1].split("m")[1][:-1])
        time_averages_bad[i-1]+=float(line_bad[1].split("m")[1][:-1])
        if lib not in times.keys():
            times[lib]=list()
        if lib not in times_bad.keys():
            times_bad[lib]=list()
        times[lib].append(float(line[1].split("m")[1][:-1]))
        times_bad[lib].append(float(line_bad[1].split("m")[1][:-1]))
        f.close()
        f_bad.close()
    time_averages[i-1]=time_averages[i-1]/100
    time_averages_bad[i-1]=time_averages_bad[i-1]/100
print(time_averages)
print(time_averages_bad)
for i in range(10):
    print(time_averages[i] < time_averages_bad[i])

#plt.scatter(time_averages, calls_averages)
#plt.title('Avg time compared to avg number of system calls')
#plt.xlabel('Time(s)')
#plt.ylabel('Instructions')
#plt.show()
#plt.savefig('test.png')
#print("TIME: ", time_averages)
#print("CALLS: ", calls_averages)
#print('max: ', max(time_averages), ' min: ', min(time_averages))
#plt.scatter(times["lib01"], calls["lib01"])
#plt.title('Times v Calls')
#plt.xlabel('Time(s)')
#plt.ylabel('Instructions')
#plt.show()
#plt.savefig('test1.png')

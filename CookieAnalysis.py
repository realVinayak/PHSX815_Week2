#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

def quartile_index_to_value(quartile_index, data_list):
    length = (len(data_list)) * quartile_index / 4
    if isinstance(length, int):
        quartile_value = (data_list[length - 1] + data_list[length])/2
    else:
        quartile_value = data_list[math.ceil(length)-1]
    return quartile_value

def quartiles(data_list):
    first_quartile_value = quartile_index_to_value(1, data_list)
    second_quartile_value = quartile_index_to_value(2, data_list)
    third_quartile_value = quartile_index_to_value(3, data_list)
    return [first_quartile_value, second_quartile_value, third_quartile_value]

def generate_quartile_plot(data_list, quartiles, file_name, nmeas, xlabel, ylabel='Probability'):
    plt.figure()
    y, x, _ = plt.hist(data_list, nmeas+1, density=True, log=True, edgecolor='black', alpha=0.50, linewidth=0.3)
    plt.grid(True)
    plt.vlines(quartiles[0], 0, max(y), color='r', linewidth=3, label='1st quartile')
    plt.vlines(quartiles[1], 0, max(y), color='#CAFF70', linewidth=3, label='2nd quartile')
    plt.vlines(quartiles[2], 0, max(y), color='y', linewidth=3, label='3rd quartile')
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('rate of 1.00 cookies per day')
    plt.show()
    plt.tight_layout()
    plt.savefig(file_name)

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    with open(InputFile) as ifile:
        for line_index, line in enumerate(ifile):
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            print(line_index)
            times_avg.append(t_avg)

    Sorter = MySort()

    #times = Sorter.DefaultSort(times)
    #times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    times_quartile = quartiles(times)
    generate_quartile_plot(
        times, 
        times_quartile, 
        'times_distribution.png', 
        nmeas=Nmeas+1,
        xlabel='Time between missing cookies [days]'
        )

    times_avg_quartile = quartiles(times_avg)
    generate_quartile_plot(
        times_avg, 
        times_avg_quartile, 
        'times_avg_distribution.png', 
        nmeas=Nmeas+1,
        xlabel='Average time between missing cookies [days]' 
        )

    
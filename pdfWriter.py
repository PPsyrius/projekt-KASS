# This Python file uses the following encoding: utf-8
import os
import matplotlib.pyplot as plt

from gvar import *
from newAlgoIntegration import *

def exportPdf(scheduleTableList):
    colLabels = [ 'Location', 'Date', 'Time', 'ClassID', 'Class', 'Lecturer']
    row = scheduleTableList

    nrows, ncols = len(scheduleTableList)+1, len(colLabels)
    hcell, wcell = 0.3, 1.
    hpad, wpad = 0, 0    
    fig=plt.figure(figsize=(ncols*wcell+wpad, nrows*hcell+hpad))
    ax = fig.add_subplot(111)
    ax.axis('off')
    #do the table
    the_table = ax.table(cellText=scheduleTableList,
              colLabels=colLabels,
              loc='center')
    plt.savefig("export_schedule.pdf")
    
        
    

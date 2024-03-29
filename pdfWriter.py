# flake8: noqa

import matplotlib.pyplot as plt

from gvar import scheduleTableList


def exportPdf(scheduleTableList):
    colLabels = ["Location", "Date", "Time", "ClassID", "Class", "Lecturer"]
    row = scheduleTableList

    nrows, ncols = len(scheduleTableList) + 1, len(colLabels)
    hcell, wcell = 0.3, 1.0
    hpad, wpad = 0, 0
    fig = plt.figure(figsize=(ncols * wcell + wpad, nrows * hcell + hpad))
    ax = fig.add_subplot(111)
    ax.axis("off")
    # do the table
    the_table = ax.table(
        cellText=scheduleTableList,
        colLabels=colLabels,
        loc="center",
    )
    plt.savefig("export_schedule.pdf")

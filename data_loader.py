import csv
from process_class import Process

processes = []

with open('processes.csv', encoding="utf8") as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile)
    for pid, cycles, footprint in reader:
        processes.append(Process(int(pid), int(cycles), int(footprint)))
    
def data():
    "data"
    return processes
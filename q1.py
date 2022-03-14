from typing import List
from process_class import Process, ProcessChain
from data_loader import data

def fifo():
    "fifo"
    processes:List[Process] = data()
    for process in processes:
        process.arrival_time = 0
    processor_chains:List[ProcessChain] = [ProcessChain() for _ in range(6)]
    for i, c_process in enumerate(processes[:6]):
        processor_chains[i].add(process=c_process)

    rem_processes = processes[6:]
    current_time = 0
    while rem_processes:
        next_process = rem_processes.pop(0)
        fastest_done = min(processor_chains, key=lambda x: x.tail.cycles_left)
        current_time = fastest_done.tail.turnaround_time
        for processor_chain in processor_chains:
            process = processor_chain.tail
            process.cycles_left = process.cycles + process.waiting_time - current_time
        fastest_done_index = processor_chains.index(fastest_done)
        processor_chains[fastest_done_index].add(next_process)
    
    for processor_chain in processor_chains:
        num_processes = 0
        total_wait = 0
        total_turnaround = 0
        for process in processor_chain:
            num_processes += 1
            total_wait += process.waiting_time 
            total_turnaround += process.turnaround_time

        print(num_processes, total_wait/num_processes, total_turnaround/num_processes)

fifo()


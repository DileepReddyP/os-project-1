# import csv
# from itertools import cycle
# from scipy.stats import truncnorm
# from numpy import floor
# import matplotlib.pyplot as plt

# def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
#     return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


# def process_generator(k: int):
#     colnames = ["PID", "Cycles", "Footprint"]
#     footprints = get_truncated_normal(mean=8*2**10, sd=8*2**10, low=1, upp=16*2**10)
#     cycles = get_truncated_normal(mean=10e3, sd=10e3, low=1, upp=10e6)
#     cycles_out = floor(cycles.rvs(k)).astype(int)
#     footprint_out = floor(footprints.rvs(k)).astype(int)
#     pids = range(10000, 10000+k)
#     processes = zip(pids, cycles_out, footprint_out)
#     with open("processes.csv", "w+") as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(colnames)
#         csvwriter.writerows(processes)
#     plt.hist(footprint_out, density=True)
#     plt.title("Memory Footprint")
#     plt.show()
#     plt.hist(cycles_out, density=True)
#     plt.title("CPU Cycles")
#     plt.show()
#     return

# if __name__ == "__main__":
#     process_generator(250)
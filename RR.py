def round_robin(processes, quantum=3):
    system_time = 0
    waiting_time = [0] * len(processes)
    remaining_burst_time = [p[2] for p in processes]

    while True:
        all_finished = True
        for i in range(len(processes)):
            if remaining_burst_time[i] > 0:
                all_finished = False
                execution_time = min(quantum, remaining_burst_time[i])
                print(f"<system time {system_time}> process {processes[i][0]} is running")
                system_time += execution_time
                remaining_burst_time[i] -= execution_time
                for j in range(len(processes)):
                    if j != i and remaining_burst_time[j] > 0:
                        waiting_time[j] += execution_time
        if all_finished:
            break

    print(f"<system time {system_time}> All processes finish...")
    print("============================================================")
    print(f"Average waiting time: {sum(waiting_time) / len(processes):.2f} units")
    print(f"Average response time: {sum(waiting_time) / len(processes):.2f} units")
    print(f"Average turnaround time: {(sum(waiting_time) + system_time) / len(processes):.2f} units")

processes_rr = [
    [1, 0, 10],
    [2, 0, 9],
    [3, 3, 5],
    [4, 7, 4],
    [5, 10, 6],
    [6, 10, 7]
]
round_robin(processes_rr)
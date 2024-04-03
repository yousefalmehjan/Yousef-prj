def srtf(processes):
    system_time = 0
    waiting_time = [0] * len(processes)
    remaining_burst_time = [p[2] for p in processes]

    while True:
        all_finished = True
        min_remaining_time = float('inf')
        next_process = None

        for i in range(len(processes)):
            if remaining_burst_time[i] > 0:
                all_finished = False
                if remaining_burst_time[i] < min_remaining_time:
                    min_remaining_time = remaining_burst_time[i]
                    next_process = i

        if all_finished:
            break

        execution_time = min(1, remaining_burst_time[next_process])
        print(f"<system time {system_time}> process {processes[next_process][0]} is running")
        system_time += execution_time
        remaining_burst_time[next_process] -= execution_time

        for i in range(len(processes)):
            if i != next_process and remaining_burst_time[i] > 0:
                waiting_time[i] += execution_time

    print(f"<system time {system_time}> All processes finish...")
    print("============================================================")
    print(f"Average waiting time: {sum(waiting_time) / len(processes):.2f} units")
    print(f"Average response time: {sum(waiting_time) / len(processes):.2f} units")
    print(f"Average turnaround time: {(sum(waiting_time) + system_time) / len(processes):.2f} units")


processes_srtf = [
    [1, 0, 10],
    [2, 0, 9],
    [3, 3, 5],
    [4, 7, 4],
    [5, 10, 6],
    [6, 10, 7]
]
srtf(processes_srtf)
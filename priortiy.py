def priority_scheduling(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes based on priority (lower priority value has higher priority)
    processes.sort(key=lambda x: x[2])


    total_waiting_time = 0
    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]
        total_waiting_time += waiting_time[i]

    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]


    print("Priority Scheduling Results:")
    for i in range(n):
        print(f"Process {processes[i][0]}: Waiting Time = {waiting_time[i]}, Turnaround Time = {turnaround_time[i]}")

    average_waiting_time = total_waiting_time / n
    print(f"Average Waiting Time: {average_waiting_time:.2f} units")

# Example usage
processes_priority = [
    [1, 0, 10],
    [2, 0, 9],
    [3, 3, 5],
    [4, 7, 4],
    [5, 10, 6],
    [6, 10, 7]
]
priority_scheduling(processes_priority)
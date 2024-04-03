def fcfs(processes):
    clock = 0
    waiting_time = 0
    free_time = 0

    for i in range(len(processes)):
        waiting_time += clock - processes[i][1]
        for j in range(processes[i][2]):
            print(f"<system time {clock}> process {processes[i][0]} is running")
            clock += 1
        print(f"<system time {clock}> process {processes[i][0]} is finished...")

        while i + 1 < len(processes) and processes[i + 1][1] > clock:
            print(f"<system time {clock}> there is no process running...")
            clock += 1
            free_time += 1

    print(f"<system time {clock}> All processes finish...")
    print("============================================================")
    print(f"Average waiting time: {waiting_time / len(processes):.2f} units")
    print(f"Average response time: {waiting_time / len(processes):.2f} units")
    print(f"Average turnaround time: {(waiting_time + clock - free_time) / len(processes):.2f} units")

processes = [
    [1, 0, 10],
    [2, 0, 9],
    [3, 3, 5],
    [4, 7, 4],
    [5, 10, 6],
    [6, 10, 7]

]
fcfs(processes)
def calculate_metrics(processes, n):
    sjf_processes = sorted(processes, key=lambda x: x['bt'])
    
    print("--- EKSEKUSI FCFS ---")
    run_simulation(processes, n)
    
    print("\n" + "="*30 + "\n")
    
    print("--- EKSEKUSI SJF ---")
    run_simulation(sjf_processes, n)

def run_simulation(proc_list, n):
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_wt = 0
    total_tat = 0

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = proc_list[i-1]['bt'] + waiting_time[i-1]

    for i in range(n):
        turnaround_time[i] = proc_list[i]['bt'] + waiting_time[i]

    print("PID\tBT\tWT\tTAT")
    for i in range(n):
        total_wt += waiting_time[i]
        total_tat += turnaround_time[i]
        print(f"{proc_list[i]['id']}\t{proc_list[i]['bt']}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {total_wt / n:.2f} ms")
    print(f"Average Turnaround Time: {total_tat / n:.2f} ms")
    
    print("\nGantt Chart:")
    for p in proc_list:
        print(f"|  {p['id']}  ", end="")
    print("|")

if __name__ == "__main__":
    data = [
        {'id': 'P1', 'bt': 24},
        {'id': 'P2', 'bt': 3},
        {'id': 'P3', 'bt': 3}
    ]
    
    calculate_metrics(data, len(data))
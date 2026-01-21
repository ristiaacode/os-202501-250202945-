def calculate_metrics(processes, name):
    print(f"\n--- {name} SCHEDULING ---")
    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    
    # Kalkulasi Waiting Time & Turnaround Time
    for i in range(1, len(processes)):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]
        
    for i in range(len(processes)):
        turnaround_time[i] = waiting_time[i] + processes[i][1]
        
    # Tampilkan Tabel
    print("ID\tBT\tWT\tTAT")
    for i in range(len(processes)):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{waiting_time[i]}\t{turnaround_time[i]}")
        
    avg_wt = sum(waiting_time) / len(processes)
    avg_tat = sum(turnaround_time) / len(processes)
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    return avg_wt, avg_tat

# Dataset: (ID, Burst Time)
data = [(1, 10), (2, 5), (3, 8)]

# 1. Jalankan FCFS (Sesuai urutan input)
fcfs_results = calculate_metrics(data, "FCFS")

# 2. Jalankan SJF (Urutkan berdasarkan Burst Time terkecil)
sjf_data = sorted(data, key=lambda x: x[1])
sjf_results = calculate_metrics(sjf_data, "SJF")
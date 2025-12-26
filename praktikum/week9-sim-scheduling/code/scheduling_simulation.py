import csv

def run_sjf_non_preemptive(processes):
    n = len(processes)
    processes.sort(key=lambda x: x['at'])
    
    completed = []
    ready_queue = []
    current_time = 0
    remaining_processes = processes[:]
    
    while len(completed) < n:
        arrived = [p for p in remaining_processes if p['at'] <= current_time]
        for p in arrived:
            ready_queue.append(p)
            remaining_processes.remove(p)
        
        if not ready_queue:
            if remaining_processes:
                current_time = remaining_processes[0]['at']
                continue
            else:
                break
        
        ready_queue.sort(key=lambda x: x['bt'])
        p = ready_queue.pop(0)
        
        start_time = current_time
        completion_time = start_time + p['bt']
        turnaround_time = completion_time - p['at']
        waiting_time = turnaround_time - p['bt']
        
        p['ct'] = completion_time
        p['tat'] = turnaround_time
        p['wt'] = waiting_time
        completed.append(p)
        
        current_time = completion_time
        
    return completed

def main():
    dataset = [
        {'id': 'P1', 'at': 0, 'bt': 6},
        {'id': 'P2', 'at': 1, 'bt': 8},
        {'id': 'P3', 'at': 2, 'bt': 7},
        {'id': 'P4', 'at': 3, 'bt': 3},
    ]

    print("Menjalankan Simulasi SJF Non-Preemptive...")
    results = run_sjf_non_preemptive(dataset)

    print("\n" + "="*52)
    print(f"{'Proses':<8} | {'AT':<4} | {'BT':<4} | {'CT':<4} | {'TAT':<4} | {'WT':<4}")
    print("-" * 52)
    
    total_tat = 0
    total_wt = 0
    
    results.sort(key=lambda x: x['id'])
    
    for r in results:
        print(f"{r['id']:<8} | {r['at']:<4} | {r['bt']:<4} | {r['ct']:<4} | {r['tat']:<4} | {r['wt']:<4}")
        total_tat += r['tat']
        total_wt += r['wt']

    n = len(results)
    print("-" * 52)
    print(f"Rata-rata Turnaround Time (Avg TAT) : {total_tat/n:.2f}")
    print(f"Rata-rata Waiting Time (Avg WT)    : {total_wt/n:.2f}")
    print("="*52)

if __name__ == "__main__":
    main()
def simulasi_genshin_fcfs(processes):
    n = len(processes)

    # Urutkan berdasarkan Arrival Time (FCFS)
    processes.sort(key=lambda x: x[1])

    print("\n" + "=" * 110)
    print("        SIMULASI CPU SCHEDULING FCFS – MASUK GAME GENSHIN IMPACT")
    print("=" * 110)

    header = (
        f"{'Proses':<15} | {'AT':<3} | {'BT':<3} | {'ST':<3} | "
        f"{'FT':<3} | {'WT':<3} | {'TAT':<3}"
    )
    print(header)
    print("-" * 110)

    current_time = 0
    total_wt = 0
    total_tat = 0

    for name, arrival, burst in processes:
        # Start Time
        start_time = max(current_time, arrival)

        # Finish Time
        finish_time = start_time + burst

        # Waiting Time
        waiting_time = start_time - arrival

        # Turnaround Time
        turnaround_time = finish_time - arrival

        total_wt += waiting_time
        total_tat += turnaround_time

        print(
            f"{name:<15} | {arrival:<3} | {burst:<3} | {start_time:<3} | "
            f"{finish_time:<3} | {waiting_time:<3} | {turnaround_time:<3}"
        )

        current_time = finish_time

    print("-" * 110)
    print(f"Rata-rata Waiting Time (WAT)     : {total_wt / n:.2f} detik")
    print(f"Rata-rata Turnaround Time (TAT) : {total_tat / n:.2f} detik\n")


# ================== MAIN ==================
if __name__ == "__main__":
    processes = [
        ["Launcher", 0, 5],
        ["CheckUpdate", 1, 8],
        ["LoadAssets", 2, 12],
        ["InitAudio", 3, 4],
        ["EnterWorld", 4, 10]
    ]

    simulasi_genshin_fcfs(processes)
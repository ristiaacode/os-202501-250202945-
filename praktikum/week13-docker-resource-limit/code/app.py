import time
import os

print("--- Memulai Simulasi Resource Limit ---")
data = []

# Loop 20 kali supaya jalan sekitar 20 detik
for i in range(1, 21):
    print(f"Iterasi ke-{i}: Menambah beban...")
    # Menambah beban memori 10MB tiap detik
    data.append(' ' * (10 * 1024 * 1024))
    time.sleep(1)

print("Selesai!")
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 3

fifo_frames = []
fifo_fault = 0

print("SIMULASI FIFO")
print("STEP | PAGE | FRAME | STATUS")
print("-" * 40)

for step, page in enumerate(reference_string, start=1):
    if page in fifo_frames:
        status = "Hit"
    else:
        status = "Fault"
        fifo_fault += 1
        if len(fifo_frames) < frame_count:
            fifo_frames.append(page)
        else:
            fifo_frames.pop(0)
            fifo_frames.append(page)

    print(f"{step:>4} | {page:>4} | {fifo_frames} | {status}")

print("Total Page Fault FIFO =", fifo_fault)

lru_frames = []
last_used = {}
lru_fault = 0

print("\nSIMULASI LRU")
print("STEP | PAGE | FRAME | STATUS")
print("-" * 40)

for step, page in enumerate(reference_string, start=1):
    if page in lru_frames:
        status = "Hit"
    else:
        status = "Fault"
        lru_fault += 1
        if len(lru_frames) < frame_count:
            lru_frames.append(page)
        else:
            lru_page = min(lru_frames, key=lambda p: last_used.get(p, -1))
            lru_frames[lru_frames.index(lru_page)] = page

    last_used[page] = step
    print(f"{step:>4} | {page:>4} | {lru_frames} | {status}")

print("Total Page Fault LRU =", lru_fault)

print("\nPERBANDINGAN AKHIR")
print("-" * 25)
print("FIFO Page Fault =", fifo_fault)
print("LRU  Page Fault =", lru_fault)

if lru_fault < fifo_fault:
    print("Kesimpulan: LRU lebih efisien dari FIFO")
else:
    print("Kesimpulan: FIFO lebih efisien dari LRU")

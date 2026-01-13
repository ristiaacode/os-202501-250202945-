def simulate_fifo(pages, capacity):
    memory = []
    page_faults = 0
    hits = 0
    print("\n--- Simulasi FIFO ---")
    
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)  
                memory.append(page)
            page_faults += 1
            status = "MISS (Fault)"
        else:
            hits += 1
            status = "HIT"
        print(f"Page: {page} | Memory: {memory} | Status: {status}")
        
    return page_faults

def simulate_lru(pages, capacity):
    memory = []
    page_faults = 0
    hits = 0
    print("\n--- Simulasi LRU ---")
    
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0) 
                memory.append(page)
            page_faults += 1
            status = "MISS (Fault)"
        else:
            memory.remove(page)
            memory.append(page)
            hits += 1
            status = "HIT"
        print(f"Page: {page} | Memory: {memory} | Status: {status}")
        
    return page_faults

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
frame_capacity = 3

fifo_faults = simulate_fifo(reference_string, frame_capacity)
lru_faults = simulate_lru(reference_string, frame_capacity)

print("\n" + "="*30)
print(f"Total Page Fault FIFO: {fifo_faults}")
print(f"Total Page Fault LRU : {lru_faults}")
print("="*30)
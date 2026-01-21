import threading
import time

resource_1 = threading.Lock()
resource_2 = threading.Lock()

def process_a():
    print("Proses A: Mencoba mengambil Resource 1...")
    with resource_1:
        print("Proses A: Berhasil mengunci Resource 1.")
        time.sleep(1)  
        
        print("Proses A: Mencoba mengambil Resource 2...")
        with resource_2:
            print("Proses A: Berhasil mengunci Resource 2!")

def process_b():
    print("Proses B: Mencoba mengambil Resource 2...")
    with resource_2:
        print("Proses B: Berhasil mengunci Resource 2.")
        time.sleep(1) 
        
        print("Proses B: Mencoba mengambil Resource 1...")
        with resource_1:
            print("Proses B: Berhasil mengunci Resource 1!")


if __name__ == "__main__":
    print("--- Simulasi Deadlock Dimulai ---")
    t1 = threading.Thread(target=process_a)
    t2 = threading.Thread(target=process_b)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Simulasi Selesai.") 
import threading, random, time
import start, execcode

if __name__ == "__main__":
    telbi = start.Telbotinterp(test=True)
    def test_procs():
        def addprocs():
            while True:
                n = random.uniform(0.1 , 1.5)
                time.sleep(n)
                rand_num_proc = random.randint(10000, 99999)
                telbi.procs[rand_num_proc] = time.time()
                print(f"{rand_num_proc} Was added with creation time ~{time.time()} ")
        test_thread_procs = threading.Thread(target=addprocs)
        test_thread_procs.start()
        test_thread_checkprocs = threading.Thread(target=telbi.checkprocs, kwargs=({"delay":3}))
        test_thread_checkprocs.start()
        telbi.checkprocs()
    test_procs()

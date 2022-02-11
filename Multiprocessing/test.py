from concurrent.futures import process
from copyreg import constructor
import time
from multiprocessing import Process

start = time.perf_counter()

def do_some(seconds, my_var):
    print(f'Sleep {seconds} seconds... my variable {my_var}')
    time.sleep(seconds)
    print('Done sleep...')


processes = []

for _ in range(10):
    p = Process(target=do_some, args=[1.5, "dhruval"])
    p.start()
    processes.append(p)
    
for pro in processes:
    pro.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')
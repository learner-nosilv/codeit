import time
start_time = time.perf_counter()

print('Hello world')

terminate_time = time.perf_counter()
print("%f" % (terminate_time - start_time))

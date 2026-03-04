import time
print("Press Enter to start the stopwatch")
input()
start_time = time.time()
print("Press Enter to stop the stopwatch")
input()
end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time = round(elapsed_time, 2)
print(f"Elapsed time: {elapsed_time} seconds")
seconds = int(elapsed_time)
minutes = seconds // 60
hours = minutes // 60
print(f"Elapsed time: {hours} hours, {minutes % 60} minutes, {seconds % 60} seconds")
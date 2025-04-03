import time

my_time = int(input("Enter the time in seconds: "))

for counter in range(my_time, 0 ,-1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60 
    hour = int(counter / 60 / 60) 
    print(f"{hour:02}-{minutes:02}-{seconds:02}")
    time.sleep(1)

print("TIME'S UP")
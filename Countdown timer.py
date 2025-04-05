import time

# Input number of seconds (Will convert to hours/mins)
my_time = int(input("Enter the time in seconds: "))

# For loop counting down
for counter in reversed(range(1, my_time)):
    seconds = counter % 60
    minutes = int(counter / 60) % 60 
    hour = int(counter / 60 / 60) 
    print(f"{hour:02}-{minutes:02}-{seconds:02}") # -- Displayed in 00-00-00 Format
    time.sleep(1)

print("TIME'S UP, WRAP IT UP!")